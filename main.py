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
    #error checking for these inputs?
    dataset = create_dataset(input("Please enter the data path: "))
    first_set = create_first_set(dataset)

    min_support = int(input("Please specify a minimum support: "))
    apriori_results = apriori(dataset, first_set, min_support)
    print("The most frequent itemset is {}".format(apriori_results[-1]))

    confidence_level = input("Please specify a confidence level (as a percentage): ")
    associations_results = find_strong_association_rules(apriori_results[-1], confidence_level, dataset)
    print("The most frequent itemset contains the following strong associations: ")
    pprint(associations_results)

    # efficiency testing
    NUM_RUNS = 100
    start = time.time()
    for index in range(NUM_RUNS):
        apriori(dataset, first_set, min_support)
    end = time.time()

    print("For the configured settings, execution time averaged over {} runs is:".format(NUM_RUNS),
          float((end - start) / NUM_RUNS), "seconds")
main()
