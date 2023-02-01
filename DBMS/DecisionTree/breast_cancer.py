import numpy as np
import pandas as pd
from test import train_and_test
from numpy import genfromtxt

if __name__ == '__main__':
    data = np.genfromtxt('DBMS/DecisionTree/Data/Breast_cancer_data.csv', dtype='i8', delimiter=',')
    data = data[:,1:]
    data[:,[8,0]]=data[:,[0,8]]
    X, y = data[:, 0:-1], data[:, -1]

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

    classes = {2: 'Bening', 4: 'Malignant'}

    train_and_test(X, y, classes, features)