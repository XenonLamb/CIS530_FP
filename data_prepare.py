import numpy as np
import pandas as pd

def cleanupData(data, train=True):
    if train ==True:
        tempdata = data[['sent1','sent2','ending0','ending1','ending2','ending3','label']]
    else:
        tempdata = data[['sent1', 'sent2', 'ending0', 'ending1', 'ending2', 'ending3']]

    tempdata['cand0'] = tempdata[['sent2', 'ending0']].apply(lambda x: ' '.join(x), axis=1)
    tempdata['cand1'] = tempdata[['sent2', 'ending1']].apply(lambda x: ' '.join(x), axis=1)
    tempdata['cand2'] = tempdata[['sent2', 'ending2']].apply(lambda x: ' '.join(x), axis=1)
    tempdata['cand3'] = tempdata[['sent2', 'ending3']].apply(lambda x: ' '.join(x), axis=1)

    if train ==True:
        return tempdata[['sent1','cand0','cand1','cand2','cand3','label']]
    else:
        return tempdata[['sent1', 'cand0', 'cand1', 'cand2', 'cand3']]

def cleanAndDump(swagDir,cacheDir):
    trainData = pd.read_csv(swagDir + 'train.csv', delimiter=',')
    valData = pd.read_csv(swagDir + 'val.csv', delimiter=',')
    testData = pd.read_csv(swagDir + 'test.csv', delimiter=',')

    trainClean = cleanupData(trainData)
    valClean = cleanupData(valData)
    testClean = cleanupData(testData,train=False)

    trainClean.to_csv(cacheDir+'train.csv',sep=',')
    valClean.to_csv(cacheDir + 'val.csv', sep=',')
    testClean.to_csv(cacheDir + 'test.csv', sep=',')

    return