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


def euclideanDistance(test, train, length):         # calculates the euclidean distance between two points for each row
    dist = 0                                        # of test and train.
    for x in range(length):
        dist += math.pow((test[x] - train[x]), 2)
    dist_root = math.sqrt(dist)
    return dist_root


def getNearest(test, train, k):                     # calculates the K nearest neighbors for a given test data and
    dist = []                                       # returns the label.
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
        return 1
    else:
        return 0


def getAccuracy(test, predict):                     # calculates the accuracy for each test given the prediction value
    correctness = 0
    for i in range(len(test)):
        each_row = test[i]

        label = each_row[-1]

        if label == predict[i]:
            correctness += 1
    accuracy = (correctness * 100.00) / len(test)
    return accuracy


def main():                                                             # Main method for implementing KNN
    train_file = loadData("../DM- Assignment-2/Data2/spam_train.csv")
    test_file = loadData("../DM- Assignment-2/Data2/spam_test.csv")
    k = [1, 5, 11, 21, 41, 61, 81, 101, 201, 401]
    prediction = []

    for each_row in k:
        for x in test_file:
            result = getNearest(x, train_file, each_row)
            prediction.append(result)
        accuracy = getAccuracy(test_file, prediction)
        del prediction[:]
        print "Accuracy for k = " + str(each_row) + " is :" + str(accuracy)



