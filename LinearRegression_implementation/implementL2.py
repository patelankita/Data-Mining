import csv
import numpy as np
import matplotlib.pyplot as p

# Method for reading the .CSV file to a list.


def fileInput(filePath):                            # Method to parse the .CSV file and add '1' to the matrix X.
    x = []
    y = []
    with open(filePath, 'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            if readFile.line_num != 1:
                x.append([1] + row[:-1])
                y.append([row[-1]])
        return x, y


def makeMatrix(x,y):                                # Method for converting array to matrix
    x_t = np.array(x)
    x_t = x_t.astype(np.float)
    matrix_x = np.matrix(x_t)

    y_t = np.array(y)
    y_t = y_t.astype(np.float)
    matrix_y = np.matrix(y_t)

    return matrix_x, matrix_y


def method(x, y, x_test, y_test, train_filename):       # Method to plot the training set MSE and test set MSE as a
    train_x, train_y = makeMatrix(x, y)                 # function of lambda (x-ais)
    test_x, test_y = makeMatrix(x_test, y_test)
    lamda_array = []
    mse_train_array = []
    mse_test_array = []

    for lamda in range(0, 151):
        w = lr(train_x, train_y, lamda)

        answer_train = mse(train_x, train_y, w)
        answer_test = mse(test_x, test_y, w)

        mse_train_array.append(answer_train)
        mse_test_array.append(answer_test)
        p.axis([0, 152, 0, 15])
        lamda_array.append(lamda)
    p.plot(lamda_array, mse_train_array)
    p.plot(lamda_array, mse_test_array)
    p.savefig("{0}.png".format(train_filename))
    p.close()

    min_lamda = mse_test_array.index(np.nanmin(mse_test_array))
    min_mse = np.nanmin(mse_test_array)
    print ("Lambda is: "+str(min_lamda) + " for filePath: " + str(train_filename) + " and MSE is:" + str(min_mse))


def lr(x,y,lamda):                                  # Method to calculate the "w" value given the X matrix, Y matrix
    x_t = x.transpose()                             # and lambda values
    first = np.dot(x_t, x)
    identityMatrix= np.identity(first.shape[0])
    second = np.dot(lamda, identityMatrix)
    addBoth = np.add(first, second)
    inverse = np.linalg.inv(addBoth)
    third = np.dot(x_t, y)
    return np.dot(inverse, third)

# Calculate MSE for a given x,y,w


def mse(x,y,w):                                     # Method to calculate the MSE given the X matrix, Y matrix and
    i = 0                                           # and lambda values
    summation = 0
    w_t = w.transpose()
    for eachRow in x:
        x_t = eachRow.transpose()
        product = np.dot(w_t,x_t)
        y_t = product.item(0, 0)
        y_act = y.item(i, 0)
        i += 1
        error = y_act - y_t
        error_square = error * error
        summation += error_square

    final_mse = summation/i
    return final_mse


def part1(train_filename, test_filename):                           # Calling methods
    train_x, train_y = fileInput(train_filename)
    test_x, test_y = fileInput(test_filename)
    method(train_x, train_y, test_x, test_y, train_filename)


if __name__ == "__main__":                                          # Method for running all the files.
    part1("../Data/train-100-10.csv", "../Data/test-100-10.csv")
    part1("../Data/train-100-100.csv", "../Data/test-100-100.csv")
    part1("../Data/train-1000-100.csv", "../Data/test-1000-100.csv")
    part1("../Data/train-(50)1000-100.csv", "../Data/test-1000-100.csv")
    part1("../Data/train-(100)1000-100.csv", "../Data/test-1000-100.csv")
    part1("../Data/train-(150)1000-100.csv", "../Data/test-1000-100.csv")
    part1("../Data/train-wine.csv", "../Data/test-wine.csv")















