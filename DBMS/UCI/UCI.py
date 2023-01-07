# Step 1, opens a data file in csv, and transform it into a usable format 
import time
import pandas as pd

def load_data():
    data_Set = pd.read_csv(open("data/student.csv"))         # data transformation to usable format using pandas
    
    return data_Set


# Step 2, splits a data set into a training set and hold-out test set
def split_data():
    data_Set = pd.read_csv(open("data/student.csv"))
    
    train_Size = 300
    test_Size  = 649 - train_Size                           # define split size
    
    train_Data = data_Set.iloc[0:train_Size]                # define training data set
    test_Data  = data_Set.iloc[train_Size:]                 # define testing  data set


# Step 3, builds a supervised NB model from training data
def train():
    data_Set = pd.read_csv(open("data/student.csv"))
    
    train_Size = 300
    test_Size  = 649 - train_Size
    
    train_Data = data_Set.iloc[0:train_Size]                # train data set, 0~299 instances
    test_Data  = data_Set.iloc[train_Size:]                 # test data set, 300~649 instances
    
    dic_Att = {}                                            # dictionary for attributes 
    attributes = train_Data.columns                         # attribute names
    
    for x in attributes:
        attributes_Count = train_Data.groupby('Grade')[x].value_counts()  # the number of each grade
        dic_Att[x] = train_Data.groupby('Grade')[x].value_counts()        # the number of each value
    
    return dic_Att


# Step 4, predicts the class for an instance or a set of instances, based on a trained model 
def predict():
    data_Set = pd.read_csv(open("DBMS/UCI/data/student.csv"))
    data = open("DBMS/UCI/data/student.csv").read()
    datalines = data.split('\n')
    datafields = []
    
    for line in datalines:
        datafields.append(line.split(","))
    
    train_Size = 300
    test_Size  = 649 - train_Size
        
    train_Data = data_Set.iloc[0:train_Size]
    test_Data  = data_Set.iloc[train_Size:]
    
    data_Grade = data_Set["Grade"]                          # value of grade attribute
    grade_Count = data_Grade.value_counts()                 # count each grades A+ ~ F
    
    attributes = train_Data.columns[0:29]                   # each attribute names
    attributes_1 = train_Data.columns[0:22]                 # divide the attribute names because some values are integer
    attributes_2 = train_Data.columns[22:28]
    attributes_3 = train_Data.columns[28:29]
    dic_Att = {}
    pred_List = []
    init = 0
    
    for x in attributes:                                                    # training the model
        attributes_Count = data_Set.groupby('Grade')[x].value_counts()      # the number of each grade
        dic_Att[x] = data_Set.groupby('Grade')[x].value_counts()            # the number of each value

    dic_Grade_Count = {'A': 0 , 'A+': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    grade = ['A', 'A+', 'B', 'C', 'D', 'F']
    for a in grade:                                                         # count the number of each grade
        dic_Grade_Count[a] = grade_Count[a]                                 # it will be the denominator of calculation.
        
    pred_Dic = {'A': 0 , 'A+': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    grade = ['A', 'A+', 'B', 'C', 'D', 'F']
    pred_Arr = []
    
    for w in range(1, 650):                                            # predict the test data set
        for y in grade:                                                # for all grades
            init = 0
            sum = 1
            for x in attributes_1:                                     # multiply each probability of value
                if datafields[w][init] not in dic_Att[x][y].keys():
                    sum = sum * 0.0001                                 # epsilon is 0.0001
                else:
                    sum = sum * dic_Att[x][y][datafields[w][init]] / dic_Grade_Count[y]
                init = init + 1
            for x in attributes_2:                                     # change format from str to int to calculate
                if int(datafields[w][init]) not in dic_Att[x][y].keys():
                    sum = sum * 0.0001
                else:
                    sum = sum * dic_Att[x][y][int(datafields[w][init])] / dic_Grade_Count[y]
                init = init + 1
            for x in attributes_3:
                if datafields[w][init] not in dic_Att[x][y].keys():
                    sum = sum * 0.0001
                else:
                    sum = sum * dic_Att[x][y][datafields[w][init]] / dic_Grade_Count[y]
                init = init + 1
            pred_Dic[y] = sum * dic_Grade_Count[y] / len(data_Set)       # calculate probability of each grades 
            Max = 'A'
        for i in grade:                                                  # take the maximum among A+ ~ F
            if pred_Dic[i] > pred_Dic['A']:
                Max = i
        pred_Arr.append(Max)                                             # return the best probability of grade
    return pred_Arr


# Step 5, evaluates a set of predictions in terms of accuracy
def evaluate():
    data_Set = pd.read_csv(open("DBMS/UCI/data/student.csv"))
    
    train_Size = 300
    test_Size  = 649 - train_Size
    pred_Arr = predict()
    
    correct = 0
    wrong   = 0
    accuracy = 0
    
    for i in range(train_Size, 649):
        if pred_Arr[i] == data_Set['Grade'][i]:
            correct = correct + 1
        else:
            wrong = wrong + 1
    
    accuracy = correct / (correct + wrong)
    
    return accuracy


# Step 6, Accuracy
start=time.time()
print("Accuraccy: ", evaluate())
end=time.time()
print(f'{end-start} seconds')