# Baseline

We randomly choose from one of the candidates as the predicted label for the input sentence. Using the
evaluation metric in eval.py, we get a score around 0.25, which is expected since there are 4 candidates
for each sample.

# How to run

Use

$ python baseline.py --input_path p1 --pred_path p2

to generate a prediction file.