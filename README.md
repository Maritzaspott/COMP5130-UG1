# Implementation of the Apriori algorithm for COMP 5130
### Undergraduate Group 1: Piper Bedell, Maritza Spott, Zelda Wilson

- Apriori is a Frequent Pattern Mining (FMP) Algorithm used in data mining for finding relationships between different items in a data set. It iterates through a dataset to find items that occur together most often.
- This algorithm has many applications within data analysis such as:
  - Market Basket Analysis - learning consumer behavior by finding relationships between the items that they buy 
  - Cross-Marketing - after finding a correlation between products, promoting those items together to generate more sales
  - Software Bugs - predict defects by learning from an imbalanced dataset

- Assumptions of the apriori algorithm:
  - If there is any itemset which is infrequent, its superset should not be generated or tested (apriori pruning principle).
  - Subsets of a frequent itemset must be frequent and subsets of an infrequent itemset must be infrequent.
  - A minimum support count should be established. The minimum support should be reasonable relative to the number of sets. 

- Strong associations are determined by the minimum confidence.
  - The confidence of `A -> B` is determined by: `P(A and B) / P(A)` which is equivalent to saying the support count of A and B over the support count of A. 
  - The confidence describes the probability of A given B: `P(A|B)`.
