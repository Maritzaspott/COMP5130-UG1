# apriori function
# maritza
# calls individual functions to create algorithm
# returns frequent itemset(s)
from utils import *


def apriori(dataset, itemset, min_support):
    """
    :param dataset: The dataset specified by user.
    :param itemset: The itemset to look at.
    :param min_support: The min support specified by user.
    :return: A list of most frequent sets.
    """
    frequency = calc_set_frequency(dataset, itemset)  # calculating the first frequency
    pruned_sets = pruning(itemset, frequency, min_support)

    if len(pruned_sets) < 1:
        return []

    next_set = create_next_set(pruned_sets)  # join step
    frequent_sets = apriori(dataset, next_set, min_support)
    frequent_sets.insert(0, pruned_sets)  # passes minimum support test

    return frequent_sets  # not just the largest set, all the sets that pass

