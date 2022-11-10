# generate associations
# return ones with confidence level above the one inputted by user
# maritza
from more_itertools import set_partitions
from utils import calc_set_frequency


def find_strong_association_rules(frequent_itemset: list[list], confidence_level: float, dataset: list) -> dict:
    """
    :param dataset: the entire dataset
    :param frequent_itemset: a list of items that make up a frequent itemset, defined by apriori
    :param confidence_level: a float inputted by the user used to define strong associations
    :return: a dictionary of {partitions (A -> B) : confidence (percentage)}
    """

    strong_rules = dict()
    for f in frequent_itemset:
        partitions = list(set_partitions(f, 2))
        for p in partitions:
            # confidence A -> B = P(B|A) = P(A and B) / P(A)
            A = set(p[0])
            B = set(p[1])
            itemsets = (A, (A.union(B)))
            frequencies = calc_set_frequency(dataset, itemsets)
            confidence = (frequencies[0] / frequencies[1]) * 100
            if confidence > float(confidence_level):
                strong_rules[str(p)] = confidence

    return strong_rules

