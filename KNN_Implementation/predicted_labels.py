import csv
import numpy as np
import math as math
import operator as op


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


def getSigma(train_file):                           # calculates the sigma i.e the standard deviation
    sigma = []                                      # given the train file
    train_numpy = np.asarray(train_file)
    no_of_columns = len(train_numpy[0])
    for i in range(no_of_columns-1):
        each_column = train_numpy[:, i]
        sigma_each = each_column.std()
        sigma.append(sigma_each)
    return sigma


def getZNormalTrain(train_file, mean, standard_deviation):           # implementing the z-score normalization
    no_of_columns = len(train_file[0])
    for x in train_file:
        for y in range(no_of_columns-1):
            x[y] = (x[y] - mean[y]) / standard_deviation[y]
    return train_file


def euclideanDistance(test, train, length):                 # calculates the euclidean distance between two points
    dist = 0                                                # for each row of test and train.
    for x in range(length):
        dist += math.pow((test[x] - train[x]), 2)
    dist_root = math.sqrt(dist)
    return dist_root


def getNearest(test, train, k):                             # calculates the K nearest neighbors for a given test data
    dist = []                                               # and returns the label
    for x in train:
        distance = euclideanDistance(test, x, len(test)-1)
        dist.append((x, distance))
    dist.sort(key=op.itemgetter(1))
    neighbor = dist[:k]

    count_spam = 0
    count_no_spam = 0
    for each_row in neighbor:
        temp = each_row[0]
        label = temp[-1]
        if label == 1:
            count_spam += 1
        else:
            count_no_spam += 1
    if count_spam > count_no_spam:
        return "spam"
    else:
        return "no"


def getAccuracy(test, predict):                      # calculates the accuracy for each test given the prediction value
    correctness =0
    for i in range(len(test)):
        each_row = test[i]

        label = each_row[-1]

        if label == predict[i]:
            correctness += 1
    accuracy = (correctness * 100.00) / len(test)
    return accuracy


def labels():                                                            # Main method for implementing KNN with z-score
    train_file = loadData("../DM- Assignment-2/Data2/spam_train.csv")    # and printing the labels.
    test_file = loadData("../DM- Assignment-2/Data2/spam_test.csv")

    mean = getMean(train_file)
    standard_deviation = getSigma(train_file)
    normalized_train = getZNormalTrain(train_file, mean, standard_deviation)
    normalized_test = getZNormalTrain(test_file, mean, standard_deviation)
    test_50_instances = normalized_test[:50]

    k = [1, 5, 11, 21, 41, 61, 81, 101, 201, 401]
    prediction = []
    index = 1
    for x in test_50_instances:

        for each_row in k:
            result = getNearest(x, normalized_train, each_row)
            prediction.append(result)
        print "t" + str(index) + " " + ', '.join(prediction)
        del prediction[:]
        index += 1


labels()
