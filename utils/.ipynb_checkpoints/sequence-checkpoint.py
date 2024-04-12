import re

def sequence_mapping_list(list_seq: list) -> list: # !!!ProTrans mapping, used to be sequence_mapping
    '''
    Given a list of sequences, map rarely Amino Acids [U Z O B] to [X].
    
    params:
        list_seq - list of sequences, e.g. ['A E T C Z A O', 'S K T Z P']
        
    return:
        the list of sequences with rarely AAs mapped to X.
    '''
    return [re.sub(f'[UZOB]', 'X', sequence) for sequence in list_seq]

def sequence_mapping_str(seq: str) -> str:
    '''
    Given a aequence, map rarely Amino Acids [U Z O B] to [X].
    
    params:
        seq - str, e.g. 'AETCZAO'
        
    return:
        the sequence with rarely AAs mapped to X.
    '''
    return re.sub(f'[UZOB]', 'X', seq)