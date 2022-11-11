# The main function.
# Asks user for min_support input, etc.
# All interactions with user should go in this file.

# Can also ask for a confidence level and return the strong associations from the most frequent itemset
from utils import *
import time
from pprint import pprint
from apriori import apriori
from associations import find_strong_association_rules


def main():
    dataset = None
    first_set = None
    min_support = None
    confidence_level = None

    # creating dataset from user given data path
    while True:
        try:
            dataset = create_dataset(input("Please enter the data path: "))
            first_set = create_first_set(dataset)
        except FileNotFoundError:
            print("The data path entered is not valid.")
            continue
        else:
            break  # only breaks out of the loop if a valid data path is entered

    # running apriori with user inputted minimum support
    while True:
        try:
            min_support = int(input("Please specify a minimum support: "))
        except ValueError:
            print("You must enter an integer.")
            continue
        else:
            break  # only breaks out of the loop if a valid data path is entered

    apriori_results = apriori(dataset, first_set, min_support)
    print("The most frequent itemset is {}".format(apriori_results[-1]))

    # calculating association rules with user given confidence level
    while True:
        try:
            confidence_level = int(input("Please specify a confidence level (as a percentage): "))
        except ValueError:
            print("You must enter an integer.")
            continue
        else:
            break  # only breaks out of the loop if a valid data path is entered

    associations_results = find_strong_association_rules(apriori_results[-1], confidence_level, dataset)
    print("The most frequent itemset contains the following strong associations: ")
    pprint(associations_results)

    # efficiency testing
    NUM_RUNS = 100
    start = time.time()
    for index in range(NUM_RUNS):
        apriori(dataset, first_set, min_support)
    end = time.time()

    avg_time = float((end - start) / NUM_RUNS)

    print("For the configured settings, execution time averaged over {} runs is:".format(NUM_RUNS),
          f'{avg_time:.2e}', "seconds")


main()
