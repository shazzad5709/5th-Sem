import numpy as np
import pandas as pd
from numpy import genfromtxt

if __name__ == '__main__':
    cs=genfromtxt('DBMS/DecisionTree/Data/Breast_cancer_data.csv', delimiter=',')
    cs = cs[:,1:]
    data=pd.DataFrame(cs)
    print(data)