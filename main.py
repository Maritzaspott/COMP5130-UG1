# The main function.
# Asks user for min_support input, etc.
# All interactions with user should go in this file.

# Can also ask for a confidence level and return the strong associations from the most frequent itemset
from utils import *
from apriori import apriori
def main():
    #error checking for these inputs?
    dataset = create_dataset(input("Please enter the data path: "))
    min_support = input("Please specify a minimum support: ")
    print("The most frequent itemset is {}".format(apriori(dataset, min_support)))
    #confidence_level = input("Please specify a confidence level: ")
    #print("The most frequent itemset contains the following strong associations{}".format(confidence_level))

main()