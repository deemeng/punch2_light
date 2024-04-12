import os

def get_pred_label(pred, threshold=0.1):
    '''
    params:
        pred - predicted list
        label - ground truth
        threshold - better to set the threshold which make the precision similar to recall. (a higher F1 score.)
    return:
        pred_label - list, classification label generate from pred given threshold
    '''
    pred_label = [1 if i>threshold else 0 for i in pred]
    return pred_label

def save_prediction(folder, dict_pred_info):
    '''
    >P04637
            1    M    0.892    1
            2    E    0.813    1
    '''
    file_path = os.path.join(folder, f'{dict_pred_info["id"]}.caid')
    seq = dict_pred_info['sequence']
    pred = dict_pred_info['pred']
    pred_label = dict_pred_info['label']
    idx = list(range(1, len(seq)+1))
    
    with open(file_path, 'w') as f:
        f.write(f">{dict_pred_info["id"]}\n")
        for i, r, p, l in zip(idx, seq, pred, pred_label):
            f.write(f"{i}\t{r}\t{round(p, 3)}\t{l}\n")

def save_timing(path_timing, list_id, list_timing, comment=''):
    '''
    Example:
    # Running MobiDB-lite, started Sun Feb  5 10:20:57 CET 2023
    sequence,milliseconds
    P04637,1827
    '''
    with open(path_timing, 'w') as f:
        f.write(f"{comment}\n")
        f.write("sequence,milliseconds\n")
        for i, t in zip(list_id, list_timing):
            f.write(f"{i},{str(t)}\n")