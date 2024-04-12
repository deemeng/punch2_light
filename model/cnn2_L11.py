import numpy as np
import pandas as pd
import torch
import torch.nn as nn

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class Net(nn.Module):
    def __init__(self, in_features, dropout=0.25):
        super().__init__()

        def conv_out_len(layer, length_in):
            return (length_in + 2 * layer.padding[0] - layer.dilation[0] * (layer.kernel_size[0] - 1) - 1) // \
                   layer.stride[0] + 1

        self.conv1 = nn.Conv1d(in_features, 50, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv1d(self.conv1.out_channels, 30, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv1d(self.conv2.out_channels, 30, kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv1d(self.conv3.out_channels, 20, kernel_size=7, stride=1, padding=3)
        self.conv5 = nn.Conv1d(self.conv4.out_channels, 20, kernel_size=7, stride=1, padding=3)
        self.conv6 = nn.Conv1d(self.conv5.out_channels, 20, kernel_size=15, stride=1, padding=7)
        self.conv7 = nn.Conv1d(self.conv6.out_channels, 20, kernel_size=7, stride=1, padding=3)
        self.conv8 = nn.Conv1d(self.conv7.out_channels, 20, kernel_size=7, stride=1, padding=3)
        self.conv9 = nn.Conv1d(self.conv8.out_channels, 10, kernel_size=3, stride=1, padding=1)
        self.conv10 = nn.Conv1d(self.conv9.out_channels, 10, kernel_size=3, stride=1, padding=1)
        self.conv11 = nn.Conv1d(self.conv10.out_channels, 1, kernel_size=1, stride=1, padding=0)

        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = x.squeeze(-1)
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        x = self.relu(self.conv4(x))
        x = self.relu(self.conv5(x))
        x = self.relu(self.conv6(x))
        x = self.relu(self.conv7(x))
        x = self.relu(self.conv8(x))
        x = self.relu(self.conv9(x))
        x = self.relu(self.conv10(x))
        x = self.dropout(x)
        x = self.sigmoid(self.conv11(x))
        x = x.flatten(start_dim=1)
        return x
