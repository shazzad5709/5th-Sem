from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from DecisionTree import DecisionTree
from numpy import genfromtxt


def _confusion_matrix(y_true, y_pred):
        tp, fp, fn, tn = [np.sum((y_true == 2.0) & (y_pred == 2.0)), 
                            np.sum((y_true == 2.0) & (y_pred == 4.0)), 
                            np.sum((y_true == 4.0) & (y_pred == 2.0)), 
                            np.sum((y_true == 4.0) & (y_pred == 4.0))
                        ]

        return [[tp, fp], [fn, tn]]


def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)



def train_and_test(X=None, y=None, class_names=None, feature_names=None):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

    clf = DecisionTree(max_depth=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)   

    acc = accuracy(y_test, predictions)

    # print("Confusion Matrix: \n", _confusion_matrix(y_test, predictions)[0], "\n", _confusion_matrix(y_test, predictions)[1])
    print(f'Accuracy: {acc*100:.4f}%\n')
    print('-'*20)
    print('\n')
    clf.print_tree(feature_names=feature_names, class_names=class_names)