# Apriori implementation for COMP 5130 final project
# Utility functions
# Maritza Spott, Zelda Wilson, Piper Bedell

# creating initial frequency table
# piper
# L1 = {frequent items}
# return list of individual items
import csv


def create_dataset(file_path):
    """
        :param file_path: a full file directory path to the imported data file used to run the algorithm
        :return: a dataset of items in a comma separated list
    """
    dataset = []
    with open(file_path, newline='') as custfile:
        rows = csv.reader(custfile)
        for row in rows:
            items = row[0].split(',')
            dataset.append(set(items))
    return dataset


def create_first_set(dataset):
    """
        :param dataset: a dataset of items in a comma separated list
        :return: the first list of unique items in itemsets to evaluate
    """
    first_set = set()
    for itemset in dataset:
        for item in itemset:
            first_set.add(item)
    itemsets = [{item} for item in list(first_set)]
    return itemsets


# calculate subset frequency from all itemsets
# piper
# for each transaction t in database do:
#       increment the count of all candidates in C(k+1) that are contained in t
# return list of itemsets

def calc_set_frequency(dataset, itemsets):
    """
        :param dataset: a dataset of items in a comma separated list
        :param itemsets: a list of unique items in itemsets to evaluate
        :return: the number of times an itemset appears in an indexed list
    """
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

def pruning(itemsets, frequency, min_support):
    for index in range(len(itemsets) - 1, -1, -1):
        if frequency[index] < min_support:
            itemsets.pop(index)
            frequency.pop(index)
    return itemsets


# create itemsets after pruning
# zelda
# for (k = 1; Lk != emptyset; k++) do begin
#       C(k+1) = candidates generated from Lk
# returns list of itemsets

def create_next_set(pruned_itemsets):
    dataset = []
    for x, itemset1 in enumerate(pruned_itemsets):
        for y, itemset2 in enumerate(pruned_itemsets):
            if y <= x:
                continue
            if len(itemset1.difference(itemset2)) == 1:
                new_itemset = itemset1.union(itemset2)
                if new_itemset not in dataset:
                    dataset.append(new_itemset)
    return dataset
