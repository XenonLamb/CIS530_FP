# CIS530_FP
CIS530 final project "Bag-of-BERT on SWAG"

# README

### Notice
* the SWAG data can be downloaded from https://github.com/rowanz/swagaf
* the datasets from GLUE can be downloaded from https://gluebenchmark.com/tasks
* the CommonsenseQA data can be downloaded from https://www.tau-nlp.org/commonsenseqa
* all the `eval_results.txt` contain the evaluation result of corresponding models.

### SWAG / CommonsenseQA Multiple choice model with BERT

* usage:

  `python swag_bert_baseline.py `

  `python csQA_bert_baseline.py`

  

* optional parameter arguments:

  `--data_dir`   input data directory (should contain the `train.scv` and `val.csv` )

  `--output_dir`   directory for saving the BERT configurations the model weights, and the evaluation results

  `--bert_model`   can be a string in the following: `bert-base-uncased`, `bert-large-uncased`, `bert-base-cased`, and `bert-base-cased` 

  `--max_seq_length`  the maximum total input sequence length after tokenization. Sequences longer than it will be truncated

  `--do_train`   Boolean for whether to run the training steps

  `--do_eval`   Boolean for whether to run the evaluation on val set

  `--train_batch_size` Default is 16

  `--eval_batch_size` Default is 16

  `--learning_rate` 

  `--num_train_epochs ` number of training epochs. Default is 3

  `--seed` random seed

### Evaluation results

#### SWAG BERT Baseline

##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.755

(Test set has no ground truth label)


#### SWAG BERT finetuned on MRPC

##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.73

(Test set has no ground truth label)

#### SWAG BERT finetuned on MNLI

##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.71

(Test set has no ground truth label)

#### SWAG BERT finetuned on SST-2

##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.51

(Test set has no ground truth label)

#### Ensemble model of Baseline+MRPC+MNLI

##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.7826

(Test set has no ground truth label)

#### BERT Baseline without context sentence in the input

##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.655

(Test set has no ground truth label)


##### 	Hyperparameters

	* batch size: 8
	* BERT model: base, uncased
	* maximum sequence length: 100
	* training epochs: 3

##### Results

Dev set accuracy: 0.73

(Test set has no ground truth label)


#### CommonsenseQA

##### 	Hyperparameters

- batch size: 16
- BERT model: base, uncased
- maximum sequence length: 128
- training epochs: 4

##### Results

Dev set accuracy: 0.5348 (BERTBase implementation by University College London: 0.530)

(Test set has no ground truth label)


### Adversarial Filtering

*`get_candsents.py` extracts the collection of choices from train set.
*`get_cor_ids.py` finds the indices of correct predictions in dev set.
*`swag_ensemble_filter.py` performs adversarial filtering using the ensemble model.
    usage: `python swag_ensemble_filter.py --do_lower_case >filtered_pairs.txt`

#### In `\swag_bert_skpt` folder:
*`all_cands.txt` contains the collection of choices extracted from train set.
*`cor_ids.txt` contains indices of all the correct predictions made by the ensemble model on dev set.
*`filtered_pairs.txt` contains the extraction result of potential substitutions, which is in the form of
    `index in cor_ids.txt` , `index in dev set`, `context sentence` , `start of ending` , `correct answer` , `potential substitution`.
*`collect_stats.py` shows the number of substitutions, average number of substitutions per sample, and the ratio of samples with at least one substitution.

#### Result
* BERT Baseline accuracy: 0.3388

