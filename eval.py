import csv
import pandas as pd
import sys
import numpy as np
import argparse

def read_swag(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        lines = []
        for line in reader:
            if sys.version_info[0] == 2:
                line = list(unicode(cell, 'utf-8') for cell in line)
            lines.append(line)


    examples = [
        int(line[11]) for line in lines[1:] # we skip the line with the column names
    ]

    return np.array(examples)

def read_pred(pred_file):
    preds = []
    with open(pred_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            preds.append(int(line))

    return np.array(preds)

def accuracy(pred, gold):
    return np.sum(pred == gold)/pred.shape[0]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred_path",
                        default=None,
                        type=str,
                        required=True,
                        help="path to prediction file")
    parser.add_argument("--gold_path",
                        default=None,
                        type=str,
                        required=True,
                        help="path to ground truth file")
    args = parser.parse_args()
    pred = read_pred(args.pred_path)
    gold = read_swag(args.gold_path)
    print('Accuracy:')
    print(accuracy(pred,gold))


if __name__ == "__main__":
    main()