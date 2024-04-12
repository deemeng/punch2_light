import os
from typing import List

import numpy as np
import pandas as pd
# import pandas as pd
import torch
import torch.nn as nn
from torch import optim


# from torch.utils.data import DataLoader

# from dataset.domainLinker_dataset import DomainLinkerDataset, Sequence, collate_fn
from dataset.utils import read_plm
from utils.static import bcolors

from utils.common import dump_list2json, read_json2list
import params.filePath as paramF
import params.hyperparams as paramH
from params.utils import get_numFeature

import json

from model.utils import load_checkpoint

# import model
import importlib

# device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)

def generate_models(list_modelInfo: list):
    '''
    Given a list trained models information. Generate a 
    params:
        list_modelInfo - list of dictionaries. [{}, {}, ...]
                        - for cnn model: {'model_name':, 'net_name':, 'dropout':, 'featureType'}
    return:
        modes - list, list of models
    '''
    models = []
    for model_info in list_modelInfo:
        net_name = model_info['net_name']
        
        # import model
        model = importlib.import_module(net_name)
    
        # Instantiate the model
        n_features, _ = get_numFeature(model_info['featureType'])
        net = model.Net(in_features=n_features, dropout=model_info['dropout']).to(device)

        optimizer = optim.Adam(net.parameters(), lr=model_info['lr'])
        model_pth = os.path.join(paramF.path_predictor, model_info['featureType'], model_info['model_name'])
        net, optimizer, start_epoch, losslogger = load_checkpoint(net, optimizer, model_pth)
        # Set all models to evaluation mode
        net.eval()
        models.append(net)
    return models
    
# Prediction
def get_true_pred(model, entity_id, feature_type, path_onehot, path_msaTrans, path_protTrans):
    '''
    Given the embeded file path, generate predictions.
    params:
        path_seq_embedded - path to embedded sequence file, .../entity_id.npy
        
    return:
        pred - the predictor output.
    '''
    if feature_type=='onehot':
        path_f = os.path.join(path_onehot, '{}.npy'.format(entity_id))
    elif feature_type=='protTrans':
        path_f = os.path.join(path_protTrans, '{}.npy'.format(entity_id))
    elif feature_type=='msa_transformer':
        path_f = os.path.join(path_msaTrans, '{}.npy'.format(entity_id))
    if os.path.isfile(path_f):
        seq_embedded = read_plm(path_f)
    else: 
        print(f"{bcolors.WARNING}Warning: cannot find file: {path_f}{bcolors.ENDC}")
        return None

    data = torch.tensor(np.array(seq_embedded)[0].T).unsqueeze(0).to(device)
    pred = model(data).tolist()[0]
    return pred
    
# Define a function to perform ensemble prediction
def ensemble_predict(models, list_modelInfo, entity_id, path_onehot, path_msaTrans, path_protTrans, msaTrans=True):
    '''
    Given the input data, and a list of model, generate the predictions from all of the models, average the predictions as the final output.

    params:
        models - list of models in evaluation mode.
        list_modelInfo - list of dictionaries. [{}, {}, ...]
        entity_id - 
        msaTrans - use msaTrans-based predictor or not. False if the length(seq)>1022
    '''
    predictions = []
    with torch.no_grad():
        for model, model_info in zip(models, list_modelInfo):
            feature_type = model_info['featureType']
            if feature_type=='msa_transformer' and (msaTrans is False):
                continue
            pred = get_true_pred(model, entity_id, feature_type, path_onehot, path_msaTrans, path_protTrans)
            
            # embedded sequence not exist.
            if pred is None:
                continue
                
            predictions.append(pred)
        # Average the predictions (you can use other strategies like weighted averaging)
        ensemble_prediction = torch.tensor(predictions).mean(dim=0)
    return ensemble_prediction