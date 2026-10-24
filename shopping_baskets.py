from itertools import combinations
from collections import defaultdict

shopping_data = [
    ['milk', 'bread', 'eggs'],
    ['milk', 'bread'],
    ['milk', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['bread', 'eggs'],
    ['milk', 'bread', 'eggs'],
    ['milk', 'butter']
]

def make_itemsets(data):
    return data

def create_shopping_rules(source, itemset_maker, conf_threshold, min_count):

    item_count = defaultdict(int)
    pairs_count = defaultdict(int)
    confidence = {}

    itemset_maker = make_itemsets(source)

    for itemset in itemset_maker:
        for item in itemset:
            item_count[item] += 1

    for itemset in itemset_maker:
        for pair in combinations(itemset, 2):
            pair = tuple(sorted(pair))
            pairs_count[pair] += 1

    for a,b in pairs_count:
        ab_confidence = pairs_count[(a,b)] / item_count[a]
        ba_confidence = pairs_count[(a,b)] / item_count[b]

        if item_count[a] >= min_count and ab_confidence >= conf_threshold:
            confidence[(a,b)] = ab_confidence
        if item_count[b] >= min_count and ba_confidence >= conf_threshold:
            confidence[(b,a)] = ba_confidence

    return confidence


def main():

    rules = create_shopping_rules(
    shopping_data,
    make_itemsets(shopping_data),
    0.6,
    4)
    print(rules)

main()



    