import csv
import numpy as np
import matplotlib.pyplot as p
from implementL2 import *


def fileInput2(filePath):                               # Method to parse the .CSV file and add 1 to the matrix X.
    matrix = []
    with open(filePath, 'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            if readFile.line_num != 1:
                matrix.append([1] + row)
        return np.matrix(matrix)


def randomMatrix(m, size):                              # Method to randomly choose the datasets and
    x = []                                              # converting them to  a matrix.
    y = []
    randomM = m[np.random.choice(m.shape[0], size, replace=False), :]

    for r in randomM:
        each = np.squeeze(np.asarray(r))
        x.append([each[:-1]])
        y.append([each[-1]])
    x_t = np.array(x)
    x_t = x_t.astype(np.float)
    matrix_x = np.matrix(x_t)

    y_t = np.array(y)
    y_t = y_t.astype(np.float)
    matrix_y = np.matrix(y_t)
    return matrix_x, matrix_y


def calcRandom(matrx, test_x, test_y, lamda):            # Method to calculate the mse for the train and test data set
    train_mse_array = []                                 # and plot the learning curve as a function of training set.
    test_mse_array = []
    data_size = []
    for i in range(50, 1000, 50):
        average = 0
        test_average = 0
        for j in range(0, 10):
            m_x, m_y = randomMatrix(matrx, i)
            w = lr(m_x, m_y, lamda)
            train_mse = mse(m_x, m_y, w)
            test_mse = mse(test_x, test_y, w)

            average += train_mse
            test_average += test_mse
        avg = average/10
        test_avg = test_average/10
        train_mse_array.append(avg)
        test_mse_array.append(test_avg)
        data_size.append(i)

    p.plot(data_size, train_mse_array)
    p.plot(data_size, test_mse_array)
    p.savefig("learningCurve{0}.png".format(lamda))
    p.close()

if __name__ == "__main__":                                  # Calls the method to plot the learning curve
    matrx = fileInput2("../Data/train-1000-100.csv")        # for Lambda = 1, 46, 50
    t_x_a, t_y_a = fileInput("../Data/test-1000-100.csv")
    test_x, test_y = makeMatrix(t_x_a, t_y_a)
    calcRandom(matrx, test_x, test_y, 1)
    calcRandom(matrx, test_x, test_y, 46)
    calcRandom(matrx, test_x, test_y, 150)





