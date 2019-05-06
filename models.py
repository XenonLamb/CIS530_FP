import torch
import torch.nn as nn
import torch.nn.functional as F

class FCBaseline(nn.Module):

    def __init__(self, emb_dim):
        super(FCBaseline, self).__init__()
        self.emb_dim = emb_dim
        self.fc = nn.Linear(2*self.emb_dim,1)
        self.loss = nn.CrossEntropyLoss()

    def forward(self, start_sent, cand0, cand1,cand2, cand3):
        fco0 = self.fc(torch.cat((start_sent,cand0), 1))
        fco1 = self.fc(torch.cat((start_sent, cand1), 1))
        fco2 = self.fc(torch.cat((start_sent, cand2), 1))
        fco3 = self.fc(torch.cat((start_sent, cand3), 1))
        output = torch.cat((fco0,fco1,fco2,fco3),1)

        return output


class BilinearBaseline(nn.Module):

    def __init__(self, emb_dim):
        super(BilinearBaseline, self).__init__()
        self.emb_dim = emb_dim
        self.w = nn.Parameter(torch.randn(self.emb_dim, self.emb_dim))
        self.loss = nn.CrossEntropyLoss()

    def forward(self, start_sent, cand0, cand1, cand2, cand3):
        fco0 = torch.matmul(torch.matmul(start_sent.unsqueeze(1),self.w), cand0).squeeze(1)
        fco1 = torch.matmul(torch.matmul(start_sent.unsqueeze(1),self.w), cand1).squeeze(1)
        fco2 = torch.matmul(torch.matmul(start_sent.unsqueeze(1),self.w), cand2).squeeze(1)
        fco3 = torch.matmul(torch.matmul(start_sent.unsqueeze(1),self.w), cand3).squeeze(1)
        output = torch.cat((fco0, fco1, fco2, fco3), 1)

        return output
