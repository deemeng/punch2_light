import os

import numpy as np
from typing import List

import torch
from dataset.domainLinker_dataset import Sequence
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def trim_padding_and_flat(sequences: List[Sequence], pred):
    all_target = np.array([])
    all_trimmed_pred = np.array([])
    for i, seq in enumerate(sequences):
        tmp_pred = pred[i][:len(seq)].cpu().detach().numpy()
        # tmp_pred = pred[i].cpu().detach().numpy()
        all_target = np.concatenate([all_target, seq.clean_target])
        all_trimmed_pred = np.concatenate([all_trimmed_pred, tmp_pred])
    return all_target, all_trimmed_pred

def concat_target_and_output(sequences: List[Sequence], pred):
    all_target = np.array([])
    all_pred = np.array([])
    for i, seq in enumerate(sequences):
        all_target = np.concatenate([all_target, seq.clean_target])
    all_pred = pred.cpu().detach().numpy()
    return all_target, all_pred

def load_checkpoint(net, optimizer, PATH):
    # Note: Input model & optimizer should be pre-defined.  This routine only updates their states.
    start_epoch = 0
    if os.path.isfile(PATH):
        print("=> loading checkpoint '{}'".format(PATH))
        checkpoint = torch.load(PATH, map_location=device)
        start_epoch = checkpoint['epoch']
        net.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        losslogger = checkpoint['loss']
        
        print("=> loaded checkpoint '{}' (epoch {})"
                  .format(losslogger, checkpoint['epoch']))
    else:
        print("=> no checkpoint found at '{}'".format(PATH))

    return net, optimizer, start_epoch, losslogger

def load_model(net, optimizer, PATH):
    # Note: Input model & optimizer should be pre-defined.  This routine only updates their states.
    start_epoch = 0
    if os.path.isfile(PATH):
        print("=> loading checkpoint '{}'".format(PATH))
        checkpoint = torch.load(PATH, map_location=device)
        start_epoch = checkpoint['epoch']
        net.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        
        print("=> (epoch {})"
                  .format(checkpoint['epoch']))
    else:
        print("=> no checkpoint found at '{}'".format(PATH))

    return net, optimizer, start_epoch