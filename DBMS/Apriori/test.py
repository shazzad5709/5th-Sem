from apriori import Apriori

if __name__ == '__main__':
    filePath = 'D:/Coding/5th-Sem/DBMS/Apriori/data/transaction.csv'
    minSup = float(input('Enter Min Support: '))
    minConf = 0.4

    obj = Apriori(minSup, minConf)
    itemCountDict, freqSet = obj.fit(filePath)
    for key, value in freqSet.items():
        print('frequent {}-term set: '.format(key))
        print('-'*20)
        for itemset in value:
            print(list(itemset))

        print()