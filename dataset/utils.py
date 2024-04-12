import numpy as np
import pandas as pd
import torch

from utils.common import load_np

class PadRightTo(object):
    """Pad the tensor to a given size.

    Args:
        output_size (int): Desired output size.
    """

    def __init__(self, output_size):
        assert isinstance(output_size, int)
        self.output_size = output_size

    def __call__(self, sample):
        padding = self.output_size - sample.size()[-1]
        return torch.nn.functional.pad(sample, (0, padding), 'constant', 0)

def read_plm(plm_path):
    plm = load_np(plm_path)
    # plm = plm.dropna().astype(np.float32)
    plm = torch.tensor(plm, dtype=torch.float32)
    return plm

def parse_target(x):
    target = torch.tensor([int(y) for y in x], dtype=torch.uint8)
    return target
