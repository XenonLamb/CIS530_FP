import random
from bert_serving.client import BertClient
import torch

def gen_random_sample(data, encoder):
    idx = random.randint(0,len(data)-1)
    start_emb = torch.from_numpy(encoder.encode(data[idx]['sent1']))
    cand0_emb = torch.from_numpy(encoder.encode(data[idx]['cand0']))
    cand1_emb = torch.from_numpy(encoder.encode(data[idx]['cand1']))
    cand2_emb = torch.from_numpy(encoder.encode(data[idx]['cand2']))
    cand3_emb = torch.from_numpy(encoder.encode(data[idx]['cand3']))
    label_tensor = torch.from_numpy(int(data[idx]['label']))

    return start_emb, cand0_emb, cand1_emb, cand2_emb, cand3_emb,label_tensor

def gen_random_batch(data, encoder, batch_size = 32):

    starts,cand0s,cand1s,cand2s,cand3s, labels = gen_random_sample(data, encoder)
    for i in range(batch_size-1):
        start_emb, cand0_emb, cand1_emb, cand2_emb, cand3_emb, label_tensor = gen_random_sample(data, encoder)
        starts = torch.cat((starts,start_emb),0)
        cand0s = torch.cat((cand0s, cand0_emb),0)
        cand1s = torch.cat((cand1s, cand1_emb), 0)
        cand2s = torch.cat((cand2s, cand2_emb), 0)
        cand3s = torch.cat((cand3s, cand3_emb), 0)
        labels = torch.cat((labels, label_tensor),0)

    return starts,cand0s,cand1s,cand2s,cand3s, labels


