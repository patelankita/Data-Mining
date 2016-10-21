import csv
import numpy as np
import math as math
import operator as op
from knn_implementation import *


def loadData(filePath):                            # Method to parse the .CSV file and removed the first column
    x = []                                         # and first row. (Heading and data numbers)
    with open(filePath, 'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            if readFile.line_num != 1:
                x.append(row[1:])
        array = np.array(x)
        array_convert_to_float = array.astype(np.float)
    return array_convert_to_float.tolist()


def getMean(train_file):                            # calculates the mean given the train file
    mean = []
    train_numpy = np.asarray(train_file)
    no_of_columns = len(train_numpy[0])
    for i in range(no_of_columns-1):
        each_column = train_numpy[:, i]
        mean_each = each_column.mean()
        mean.append(mean_each)
    return mean


def getSigma(train_file):                            # calculates the sigma i.e the standard deviation
    sigma = []                                       # given the train file
    train_numpy = np.asarray(train_file)
    no_of_columns = len(train_numpy[0])
    for i in range(no_of_columns-1):
        each_column = train_numpy[:, i]
        sigma_each = each_column.std()
        sigma.append(sigma_each)
    return sigma


def getZNormalTrain(train_file, mean, standard_deviation):      # implementing the z-score normalization
    no_of_columns = len(train_file[0])
    for x in train_file:
        for y in range(no_of_columns-1):
            x[y] = (x[y] - mean[y]) / standard_deviation[y]
    return train_file


def call():                                                           # Main method for implementing KNN after z-score
    train_file = loadData("../DM- Assignment-2/Data2/spam_train.csv")   # normalization
    test_file = loadData("../DM- Assignment-2/Data2/spam_test.csv")

    mean = getMean(train_file)
    standard_deviation = getSigma(train_file)
    normalized_train = getZNormalTrain(train_file, mean, standard_deviation)
    normalized_test = getZNormalTrain(test_file, mean, standard_deviation)
    k = [1, 5, 11, 21, 41, 61, 81, 101, 201, 401]
    prediction = []

    for each_row in k:
        for x in normalized_test:
            result = getNearest(x, normalized_train, each_row)
            prediction.append(result)
        accuracy = getAccuracy(test_file, prediction)
        del prediction[:]
        print "Accuracy for k = " + str(each_row) + " is :" + str(accuracy)


call()              #Rum this for KNN implementation with z-score normalization of data
# main()                # Uncomment this to run the KNN implementation without normalization of data.
