import csv
#import num.py as np
#import matplotlib.pyplot as plt
#import pandas as pd


def loadDataSet(trainingSetName, testSetName, trainingSet=[], testSet=[]):
    with open(trainingSetName,'rb') as csvfile:
        lines = csv.reader(csvfile)
        print 'Training set loading..'
        for row in lines:
            print ', '.join(row)
    with open(testSetName,'rb') as csvfile:
        lines = csv.reader(csvfile)
        print 'test set loading..'
        for row in lines:
            print ', '.join(row)
