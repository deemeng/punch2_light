import os
from typing import List

import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

from dataset.utils import parse_target, read_plm
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence, pad_sequence

class Sequence:
    def __init__(self, seq_id, sequence, target, feature_path=None, data_transform=None,
                 target_transform=None, feature_type='protTrans'):
        
        self.seq_id = seq_id
        self.sequence = sequence
        self._target = parse_target(target)
            
        self.data_transform = data_transform
        self.target_transform = target_transform

        if feature_type=='protTrans':
            self.seq_encoding = read_plm(os.path.join(feature_path, 'protTrans/many2many/{}.npy'.format(self.seq_id)))
        elif feature_type=='onehot':
            self.seq_encoding = read_plm(os.path.join(feature_path, 'onehot/many2many/{}.npy'.format(self.seq_id)))
        elif feature_type=='msa_transformer':
            self.seq_encoding = read_plm(os.path.join(feature_path, 'msa_transformer/many2many/{}.npy'.format(self.seq_id)))

    @property
    def data(self):
        data = self.seq_encoding.mT.squeeze(0)
        if self.data_transform is not None:
            data = self.data_transform(data)
        return data.float()

    @property
    def target(self):
        target = self._target
        if self.target_transform is not None:
            target = self.target_transform(target)
        return target.float()

    @property
    def clean_target(self):
        return self._target.numpy()

    def __len__(self):
        return len(self.sequence)

    def __repr__(self):
        return 'Sequence({}, {})'.format(self.seq_id, self.sequence)

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, i):
        return self.data, self.target

    def as_dict(self):
        return {"seq_id": self.seq_id, "sequence": self.sequence, "target": self.target, "data": self.data}


# Base class for the two datasets, with common functionality
class DomainLinkerDataset(Dataset):
    def __init__(self, data, feature_root, transform=None, target_transform=None, feature_type='protTrans'):

        self.transform = transform
        self.target_transform = target_transform

        self.raw_data = data
        self.feature_type = feature_type
        self.feature_root = feature_root

    def __len__(self):
        return len(self.raw_data)

    def __getitem__(self, idx):
        seq_id, sequence, target, _ = self.raw_data.iloc[idx]
        item = Sequence(seq_id, sequence, target, feature_path=self.feature_root, feature_type=self.feature_type,
                        data_transform=self.transform, target_transform=self.target_transform)
        return item
    
def collate_fn(batch: List[Sequence]):
    data = torch.stack([item.data for item in batch])
    target = torch.stack([item.target for item in batch])
    return batch, data, target

