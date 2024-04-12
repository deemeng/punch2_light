import os
from params.hyperparams import *
from params.utils import create_folder

import params.USER_filePath as u

# 1. Data-Input
path_data = 'data'

if u.user:
    path_input = u.path_input
    path_onehot = u.path_onehot
    path_msaTrans = u.path_msaTrans
    path_protTrans = u.path_protTrans
    path_output = u.path_output
else:
    path_input = os.path.join(path_data, 'input.fasta')
    path_onehot = os.path.join(path_data, 'onehot')
    path_msaTrans = os.path.join(path_data, 'msaTrans')
    path_protTrans = os.path.join(path_data, 'protTrans')
    path_output = 'output' # output folder

path_input_json = os.path.join(path_data, 'input.json')
path_seq = os.path.join(path_data, 'seq')
create_folder(path_seq)

# 2. predictor
path_predictor = 'predictor'

# 3.Output
create_folder(path_output)
path_prediction = os.path.join(path_output, 'disorder')
path_time = os.path.join(path_output, 'timings.csv')
create_folder(path_prediction)