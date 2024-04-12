import os

import numpy as np
from typing import List

import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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