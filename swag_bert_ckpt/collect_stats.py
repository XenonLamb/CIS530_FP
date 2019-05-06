import numpy as np
import sys
from io import open





count_dict = {}
total_samps = 0
total_ex = 0
total_cor = 15652
with open("./filtered_pairs.txt", 'r', encoding='utf-8') as f:
    for line in f:
        total_ex+=1
        secs = line.strip().split(',')
        temp_id = int(secs[0].strip())
        if not temp_id in count_dict:
            count_dict[temp_id] = 1
            total_samps+=1
        else:
            count_dict[temp_id] +=1

count_count = {}

for item in count_dict:
    if not count_dict[item] in count_count:
        count_count[count_dict[item]]=1
    else:
        count_count[count_dict[item]]+=1

print(count_count)

print(total_samps)

print(total_ex/total_samps)

print(total_ex/total_cor)

print(total_samps/total_cor)