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
    frequency = calc_set_frequency(dataset, itemset)
    pruned_sets = pruning(itemset, frequency, min_support)

    if len(pruned_sets) <= 1:
        return []

    next_set = create_next_set(pruned_sets)
    frequent_sets = apriori(dataset, next_set, min_support)
    frequent_sets.insert(0, pruned_sets)

    return frequent_sets

