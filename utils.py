# Apriori implementation for COMP 5130 final project
# Utility functions
# Maritza Spott, Zelda Wilson, Piper Bedell

# creating initial frequency table
# piper
# L1 = {frequent items}
# return list of individual items
import csv


def create_dataset(file_path):
    dataset = []
    with open(file_path, newline='') as custfile:
        rows = csv.reader(custfile)
        for row in rows:
            items = row[0].split(',')
            dataset.append(set(items))
    return dataset


def create_first_set(dataset):
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


def calc_set_frequency(dataset, itemsets):
    frequency = []
    for index, itemset in enumerate(itemsets):
        frequency.append(0)

    for subset in dataset:
        for index, itemset in enumerate(itemsets):
            if itemset.difference(subset) == set():
                frequency[index] += 1
    return frequency

# prune
# zelda
# L(k+1) = candidates in C(k+1) with min support
# return list of itemsets

# create itemsets after pruning
# zelda
# for (k = 1; Lk != emptyset; k++) do begin
#       C(k+1) = candidates generated from Lk
# returns list of itemsets
