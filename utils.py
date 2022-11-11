# Apriori implementation for COMP 5130 final project
# Utility functions
# Maritza Spott, Zelda Wilson, Piper Bedell

# creating initial frequency table
# piper

import csv


def create_dataset(file_path: str) -> list:
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


def create_first_set(dataset: list) -> list:
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

def calc_set_frequency(dataset: list, itemsets: list) -> list:
    """
        :param dataset: a dataset of items in a comma separated list
        :param itemsets: a list of unique items in itemsets to evaluate
        :return: a list of the frequencies associated with the given itemsets
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

def pruning(itemsets: list, frequency: list, min_support: int) -> list:
    """
    :param itemsets: a list of itemsets to prune
    :param frequency: a list of frequencies of each itemset
    :param min_support: the minimum support specified by the user that each itemset must have to pass
    :return: the list of itemsets with a support count greater than the minimum support
    """
    for index in range(len(itemsets) - 1, -1, -1):
        if frequency[index] < min_support:
            itemsets.pop(index)
            frequency.pop(index)
    return itemsets


# create itemsets after pruning
# zelda

def create_next_set(pruned_itemsets: list) -> list:
    """
    :param pruned_itemsets: a list generated from `pruning`
    :return: the new list of itemsets to go through, using only the pruned itemsets from previous step
    """
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
