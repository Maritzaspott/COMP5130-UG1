# generate associations
# return ones with confidence level above the one inputted by user
# maritza
from more_itertools import powerset
from utils import calc_set_frequency


def find_strong_association_rules(frequent_itemsets: list[list], confidence_level: float, dataset: list) -> dict:
    """
    :param dataset: the entire dataset
    :param frequent_itemset: a list of items that make up a frequent itemset, defined by apriori
    :param confidence_level: a float inputted by the user used to define strong associations
    :return: a dictionary of {partitions (A -> B) : confidence (percentage)}
    """

    strong_rules = dict()
    for itemset in frequent_itemsets:
        itemset_list = list()
        itemset_list.append(itemset)
        AuB = (calc_set_frequency(dataset, itemset_list))[0]
        combinations = list(powerset(itemset))[1:-1] #list of lists
        for index in range(len(combinations)):
            combinations[index] = set(combinations[index])
        frequencies = calc_set_frequency(dataset, combinations)
        for index in range(len(frequencies)):
            confidence = (AuB / frequencies[index]) * 100
            if confidence > float(confidence_level):
                difference = (itemset - combinations[index])
                key = "{} -> {}".format(combinations[index], difference)
                strong_rules[key] = confidence

    return strong_rules

