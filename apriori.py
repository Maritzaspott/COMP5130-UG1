# apriori function
# maritza
# calls individual functions to create algorithm
# returns frequent itemset(s)
from utils import *
def apriori(dataset, min_support):
    """
    :param dataset: The dataset specified by user.
    :param min_support: The min support specified by user.
    :return:
    """
    first_set = create_first_set(dataset)
    frequency = calc_set_frequency(dataset, first_set)
    pruned_sets = pruning(first_set, frequency, min_support)

    if len(pruned_sets) <= 1:
        return []

    next_set = create_next_set(pruned_sets)
    frequent_sets = apriori(dataset, next_set, min_support)
    frequent_sets.insert(0, pruned_sets)

    return frequent_sets

