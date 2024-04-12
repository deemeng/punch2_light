import os

def get_numFeature(featureType):
    '''
    return number of features based on the feature type.
    '''
    MAX_seq_length = 400000
    if featureType=='protTrans':
        n_features = 1024
    elif featureType=='msa_transformer':
        n_features = 768
        MAX_seq_length = 1022
    elif featureType=='onehot':
        n_features = 21
    return n_features, MAX_seq_length

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)