# generate associations
# return ones with confidence level above the one inputted by user
# maritza
from more_itertools import set_partitions
from utils import calculate_subset_frequency #or whatever it ends up being called


def find_strong_association_rules(frequent_itemset: list, confidence_level: float) -> dict:
    """
    :param frequent_itemset: a list of items that make up a frequent itemset, defined by apriori
    :param confidence_level: a float inputted by the user used to define strong associations
    :return: a dictionary of {partitions (A -> B) : confidence (percentage)}
    """

    strong_rules = dict()
    for partition_list in set_partitions(frequent_itemset, 2):
        confidence = calculate_confidence(partition_list[0], partition_list[1])
        if confidence > confidence_level:
            strong_rules[partition_list] = confidence

    return strong_rules


def calculate_confidence(list1: list, list2: list) -> float:
    """
    :param list1: the first partitioned list of length one or more
    :param list2: the second partitioned list of length one or more
    :return: a float value, the confidence of list1 -> list2
    """

    # confidence = P(list2|list1) = P(list1 and list2) / P(list1)

    support_count1 = calculate_subset_frequency(list1 + list2)  # P(list1 and list2)
    support_count2 = calculate_subset_frequency(list1)  # P(list1)

    return (support_count1 / support_count2) * 100

