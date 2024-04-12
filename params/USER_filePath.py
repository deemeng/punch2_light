import os
from params.utils import create_folder

# !!! IMPORTANT
# Change this to True if you want to manually provide these paths.
user = True
'''
1. Data-Input

an example:
---------------------
path_input = ''
path_onehot = ''
path_msaTrans = ''
path_protTrans = ''
'''
path_input = '/home/dimeng/caid3/test_idr.fasta'
path_onehot = '/home/dimeng/project/idr/data/caid/features/onehot'
path_msaTrans = '/home/dimeng/project/idr/data/caid/features/msaTrans'
path_protTrans = '/home/dimeng/project/idr/data/caid/features/protTrans'
'''
2.Output folder
    All the outputs will be stored in this folder, including
    a. timings.csv
    b. disorder folder, where will keep all the prediction resulds.
an example:
---------------------
path_output = ''
'''
path_output = '/home/dimeng/caid3/punch_idr_output'