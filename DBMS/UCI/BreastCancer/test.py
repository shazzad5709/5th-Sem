from numpy import genfromtxt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from test2 import NaiveBayes
from sklearn.metrics import confusion_matrix, f1_score , accuracy_score


if __name__ == '__main__':
    
    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    data = genfromtxt('DBMS/UCI/BreastCancer/Data/wdbc.csv', delimiter=',')
    data = data[:,1:]
    data[:,[30,0]]=data[:,[0,30]]
    df=pd.DataFrame(data)
    # print(df)

    X, y = df.iloc[:, 0:-1], df.iloc[:, -1]
    # print(X.shape)
    # print(y.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=None
    )
    # print(X_train.shape, X_test.shape)

    nb = GaussianNB()
    nb.fit(X_train, y_train)
    # print(nb.score(X_test, y_test))
    predictions = nb.predict(X_test)
    # print("Confusion Matrix: \n", confusion_matrix(y_test, predictions))
    # print("Accuracy: ",accuracy_score(y_test, predictions)*100, "%")
    print(f'Accuracy: {round(accuracy(y_test, predictions), 6)*100}%')