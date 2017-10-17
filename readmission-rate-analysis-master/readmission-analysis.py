import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model, preprocessing
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import AdaBoostClassifier



from parse_data import clean_data

FILE = 'data/diabetic_data.csv'
if __name__ == "__main__":
    data = clean_data(FILE)
    over_sampler = []

    for d in data:
        if d[-1] == 1:
            over_sampler.append(d)
    for i in range(1,8):
        data = np.append(data, over_sampler, axis=0)

    c0 = 0
    c1 = 0
    for dd in data:
        if dd[-1] == 0:
            c0 += 1
        else:
            c1 += 1
    x = data[:,:-1]
    y= data[:,-1]

    parameters = {}
    normalized_x = preprocessing.normalize(x, norm='l2')

    # running adaboost
    print "Running ADADoosting with decision tree"
    clf_adaboost = AdaBoostClassifier(n_estimators=100)
    score_ada = cross_val_score(clf_adaboost, normalized_x, y, cv=10, n_jobs=5)

    avg_score_ada = np.mean(score_ada)
    print "adaptive boosting score is: "+ str( avg_score_ada)

    print "==========="

    print "Running Random Forests"
    clf_rf = RandomForestClassifier(n_estimators=1000, max_depth=20, n_jobs = -1)
    score_rf = cross_val_score(clf_rf, normalized_x, y, cv=10, n_jobs=-1)
    avg_rf_accuracy = np.mean(score_rf)
    print "Random Forest Accuracy is:" + str(avg_rf_accuracy)
    print "==========="



    print "Running KNN for different values of K"
    k = 500
    clf_k = KNeighborsClassifier(n_neighbors=k)

    score_k = cross_val_score(clf_k, normalized_x, y, cv=10, n_jobs=-1)

    avg_score_k = np.mean(score_k)
    print "for the value k: "+ str(k) + "accuracy is: "+ str(avg_score_k)
    print "==========="



    print "Running SVM"
    clf_svm = svm.SVC(kernel='rbf', C=1, cache_size=7000)
    score_svm = cross_val_score(clf_svm, normalized_x, y, cv=10, n_jobs=5)
    avg_svm_score_svm = np.mean(score_svm)
    print "SVM accuracy: " + str(avg_svm_score_svm)
    print "==========="


