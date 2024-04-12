import torch
import os
import numpy as np
from utils.sequence import sequence_mapping
from utils.common import load_tab, save_np, load_np

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def tokenizing(list_seq: list, tokenizer):
    '''
    Tokenize, encode sequences.
    Tokenize
    1. map AA_letter to number
    2. padding sequences to the langest sequences in this batch
    3. add mask token to distinguish which part is sequences and which part is padding 0s
    
    params:
        list_seq - list of sequences without rarely AAs, e.g. ['A E T C X A X', 'S K T X P']
        tokenizer - object that generated from T5Tokenizer.from_pretrained() function.
    return:
        ids - T5Tokenizer(name_or_path='Rostlab/prot_t5_xl_uniref50', vocab_size=, model_max_length=, is_fast=False, padding_side='right', 
                truncation_side='right', special_tokens={'eos_token': '</s>', 'unk_token': '<unk>', 'pad_token': '<pad>', 'additional_special_tokens': [], ...})
                e.g. {'input_ids': [[3, 9, 11, 22, 23, 3, 23, 1], [7, 14, 11, 23, 13, 1, 0, 0]], 'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0]]}
    '''
    
    ids = tokenizer.batch_encode_plus(list_seq, add_special_tokens=True, padding=True)
    return ids

def get_features_from_embedding(embedding, attention_mask):
    '''
    Given embedding result, remove <pad> & </s> to get only the embedded features.
    params:
        embedding - numpy array, embedding results from ProtTrans. (size_embedding_AA=1024)
                    size: (num_seq, len_seq+num_padding+1_end_token, size_embedding_AA)
        attention_mask - list[list], masking padding parts.
        
    return:
        features - list, embedded features without padding and end tockens, f(num_seq, len_seq, size_embedding_AA)
                    The reason we use list here, is because the lengths of these sequences are different.
    '''
    features = []
    # print(len(embedding))
    for seq_num in range(len(embedding)):
        # seq_len = actural length of the sequence + 1  
        seq_len = sum(attention_mask[seq_num])
        seq_emb = embedding[seq_num][:seq_len-1]
        features.append(seq_emb)
        
    return features

def get_PLM_embedding(list_seq: list, model, tokenizer) -> list[np.array]:
    '''
    Given a list of sequences, generate a list pf PLM embedding of these sequences. 
    
    params:
        list_seq - list of Uniprot sequences.
        model - PLM model
        tokenizer - tokenizing object.
        
    return:
        embedded_seq - list of embedded sequences (numpy arraies). Unequal lengths.
    '''
    # 1. map rarely Amino Acids to X
    list_seq = sequence_mapping(list_seq)
    
    # 2. tokenize the sequences
    ids = tokenizing(list_seq, tokenizer)
    input_ids = torch.tensor(ids['input_ids']).to(device) # input databatch
    attention_mask = torch.tensor(ids['attention_mask']) # mask padding regions
    
    # 3. embedding
    with torch.no_grad():
        embedding = model(input_ids=input_ids, attention_mask=attention_mask)
        
    embedding = embedding.last_hidden_state.cpu().numpy() # save to CPU
    
    # 4. remove paddings & special tokens
    embedded_seq = get_features_from_embedding(embedding, attention_mask)
    
    return embedded_seq

def save_embedded(list_seq_unp: list, list_seqID: list, file_folder: str, model, tokenizer):
    '''
    Embed a list of sequences and save them to files.
    
    params:
        list_seq_unp - list of uniprot sequences.
        list_seqID - file names
        file_folder - the folder to save the sequence
        mdoel - PLM
        tokenizer
    '''
    
    for idx in range(len(list_seq_unp)):
        print(idx)
        seq_embedded = get_PLM_embedding([list_seq_unp[idx]], model, tokenizer)
        file_path = os.path.join(file_folder, f'{list_seqID[idx]}.npy')
        save_np(seq_embedded, file_path)
        