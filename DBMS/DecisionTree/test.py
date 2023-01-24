from sklearn import datasets
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


if __name__ == '__main__':
    data = np.genfromtxt('DBMS/DecisionTree/Data/Breast_cancer_data.csv', dtype='i8', delimiter=',')
    data = data[:,1:]
    data[:,[8,0]]=data[:,[0,8]]
    X, y = data[:, 0:-1], data[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    clf = DecisionTree(max_depth=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)   

    acc = accuracy(y_test, predictions)

    # print("Confusion Matrix: \n", _confusion_matrix(y_test, predictions)[0], "\n", _confusion_matrix(y_test, predictions)[1])
    print(f'Accuracy: {acc*100:.4f}%\n')
    print('-'*20)
    print('\n')
    
    features = [
        'Clump Thickness',
        'Uniformity of Cell Size',
        'Uniformity of Cell Shape', 
        'Marginal Adhesion', 
        'Single Epithelial Cell Size', 
        'Bare Nuclei', 
        'Bland Chromatin', 
        'Normal Nucleoli', 
        'Mitoses'
    ]

    # feature_iris = [
    #      'sepal length', 'sepal width', 'petal length', 'petal width'
    # ]

    # feature_breast_cancer = [
    #     'mean radius', 'mean texture', 'mean perimeter', 'mean area',
    #     'mean smoothness', 'mean compactness', 'mean concavity',
    #     'mean concave points', 'mean symmetry', 'mean fractal dimension',
    #     'radius error', 'texture error', 'perimeter error', 'area error',
    #     'smoothness error', 'compactness error', 'concavity error',
    #     'concave points error', 'symmetry error',
    #     'fractal dimension error', 'worst radius', 'worst texture',
    #     'worst perimeter', 'worst area', 'worst smoothness',
    #     'worst compactness', 'worst concavity', 'worst concave points',
    #     'worst symmetry', 'worst fractal dimension'
    # ]

    clf.print_tree(feature_names=features)
