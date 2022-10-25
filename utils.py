# Apriori implementation for COMP 5130 final project
# Utility functions
# Maritza Spott, Zelda Wilson, Piper Bedell

# creating initial frequency table
# piper
# L1 = {frequent items}
# return list of individual items
def create_first_set (dataset):
    first_set = set()
    for itemset in dataset:
        for item in itemset:
            if item not in first_set:
                first_set.add(item)
    return [{item} for item in list(first_set)]

# calculate subset frequency from all itemsets
# piper
# for each transaction t in database do:
#       increment the count of all candidates in C(k+1) that are contained in t
# return list of itemsets


# prune
# zelda
# L(k+1) = candidates in C(k+1) with min support
# return list of itemsets

# create itemsets after pruning
# zelda
# for (k = 1; Lk != emptyset; k++) do begin
#       C(k+1) = candidates generated from Lk
# returns list of itemsets