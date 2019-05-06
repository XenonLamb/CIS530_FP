import argparse
import csv
import os
import random
import sys
from io import open


import numpy as np

def read_swag_baseline_examples(input_file):
	with open(input_file, 'r', encoding='utf-8') as f:
		reader = csv.reader(f)
		lines = []
		for line in reader:
			if sys.version_info[0] == 2:
				line = list(unicode(cell, 'utf-8') for cell in line)
			lines.append(line)
	return lines

def get_random_baseline_pred(lines):
	pred = [random.randint(0, 3) for _ in range(len(lines)-1)]
	return pred

def write_pred(pred, output_file):
	with open(output_file, 'w') as f:
		for i in pred:
			f.write(str(i)+'\n')

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_path", default=None, type=str, required=True, help="path to input file")
	parser.add_argument("--pred_path", default=None, type=str, required=True, help="path to output pred file")
	args = parser.parse_args()

	lines = read_swag_baseline_examples(args.input_path)
	y_true = np.array([int(line[-1]) for line in lines[1:]])
	y_pred = get_random_baseline_pred(lines)
	write_pred(y_pred, args.pred_path)



	# acc = np.sum(y_pred == y_true) / y_true.shape[0]
	# print('Baseline(random) accuracy: {}'.format(acc))
if __name__ == '__main__':
	main()
	
