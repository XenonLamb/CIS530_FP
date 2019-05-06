# The data

## Data format

The data is in .csv files. The collected data are divided into three sets: train.csv, val.csv and test.csv. 
One row of data is in the following format:

Sample id, sentence, cand0, cand1, cand2, cand3, label

The sample id is the serial number of the sample. Sentence is the context sentence. cand0 through cand3 are
all candidate next sentences for the context sentence. label is the true next sentence for the context.

An example of a training/evaluating example:

0,Members of the procession walk down the street holding small horn brass instruments.,A drum line passes by walking down the street playing their instruments.,A drum line has heard approaching them.,A drum line arrives and they're outside dancing and asleep.,A drum line turns the lead singer watches the performance.,0

As you can see each field is separated by a comma. Note that test.csv does not have labels.

## Source

The data is collected from http://rowanzellers.com/swag/