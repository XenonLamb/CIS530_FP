import csv
import os
import random
import sys
from io import open

def read_swag_examples(input_file, is_training=True):
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        lines = []
        for line in reader:
            if sys.version_info[0] == 2:
                line = list(unicode(cell, 'utf-8') for cell in line)
            lines.append(line)

    if is_training and lines[0][-1] != 'label':
        raise ValueError(
            "For training, the input file must contain a label column."
        )
    for line in lines:
        print(line[7])
        print(line[8])
        print(line[9])
        print(line[10])

    return

read_swag_examples("./data/train.csv")
