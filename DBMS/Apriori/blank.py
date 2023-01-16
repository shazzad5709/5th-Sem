import pandas as pd

filePath = 'D:/Coding/5th-Sem/DBMS/Apriori/data/transaction.csv'
df = pd.read_csv(filePath)
df = df.drop(["MILK"], axis = 1)
print(df.info)