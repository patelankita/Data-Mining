import csv
import numpy as np
import matplotlib.pyplot as p
from implementL2 import *


def cvMethod(filePath):                                 # Method to divide the array into k= 10 folds and
    x_a, y_a = fileInput(filePath)                      # and then calculating the best lambda for each data set
    x = np.array(x_a).astype(np.float)
    y = np.array(y_a).astype(np.float)
    x_size = x.shape[0]
    fold = x_size/10
    train_mse_array =[]
    test_mse_array = []
    lamda =[]
    for l in range(0, 151):
        average = 0
        test_average = 0
        for i in range(0, 10):
            tr_x = list(x[0: (i*fold)]) + list(x[((i+1)*fold):])
            train_matrix_x = np.matrix(tr_x)

            te_x = (list(x[(i*fold): (i+1)*fold]))
            test_matrix_x = np.matrix(te_x)

            tr_y = list(y[0: (i * fold)]) + list(y[((i + 1) * fold):])
            train_matrix_y = np.matrix(tr_y)

            te_y = (list(y[(i * fold): (i + 1) * fold]))
            test_matrix_y = np.matrix(te_y)

            w = lr(train_matrix_x, train_matrix_y, l)

            train_mse = mse(train_matrix_x, train_matrix_y, w)

            test_mse = mse(test_matrix_x, test_matrix_y, w)

            average += train_mse
            test_average += test_mse
        avg = average / 10
        test_avg = test_average / 10
        train_mse_array.append(avg)
        test_mse_array.append(test_avg)
        lamda.append(l)

    min_lamda = test_mse_array.index(np.nanmin(test_mse_array))
    min_mse = np.nanmin(test_mse_array)
    print ("Lambda is: " + str(min_lamda) + " for filePath: " + str(filePath) + " and MSE is:" + str(min_mse))


if __name__ == "__main__":                                  # Call to the method to compute the Cross Validation and
    cvMethod("../Data/train-100-10.csv")                    # calculating the minimum lambda for each data set.
    cvMethod("../Data/train-100-100.csv")
    cvMethod("../Data/train-1000-100.csv")
    cvMethod("../Data/train-(50)1000-100.csv")
    cvMethod("../Data/train-(100)1000-100.csv")
    cvMethod("../Data/train-(150)1000-100.csv")
    cvMethod("../Data/train-wine.csv")