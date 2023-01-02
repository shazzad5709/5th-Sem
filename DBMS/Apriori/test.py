from apyori import apriori

# The dataset is a list of transactions, where each transaction is a list of items
dataset = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'eggs'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola'],
]

# Use the apriori function to find frequent item sets
# with a minimum support of 50% (support_threshold=0.5)
frequent_item_sets = apriori(dataset, min_support=0.5, max_len=3)

# Print the frequent item sets
for item_set in frequent_item_sets:
    print(item_set)
    print()
