from collections import defaultdict
from itertools import combinations

movie_data = [
    ['action', 'comedy', 'drama'],
    ['action', 'comedy'],
    ['action', 'drama'],
    ['comedy', 'drama'],
    ['action', 'comedy', 'drama'],
    ['action', 'comedy']
]

'''

The idea is to first create a dict that will hold count of all the distinct genres.
After that we need a new dict to count pairs (combination) of genres.
We calculate the confidence for items ab, and then confidence for items ba.




'''

def create_movie_rules(itemsets, conf_threshold, min_count):
    genre_count = defaultdict(int)
    genre_pair_count = defaultdict(int)
    confidence = {}

    for items in itemsets:
        for genre in items:
            genre_count[genre] += 1

    for items in itemsets:
        for pair in combinations(items, 2):
            pair = tuple(sorted(pair))
            genre_pair_count[pair] += 1

    for a,b in genre_pair_count:
        ab_conf = genre_pair_count[(a,b)] / genre_count[a]
        ba_conf = genre_pair_count[(a,b)] / genre_count[b]

        if genre_count[a] >= min_count and ab_conf >= conf_threshold:
            confidence[(a,b)] = ab_conf
        if genre_count[b] >= min_count and ba_conf >= conf_threshold:
            confidence[(b,a)] = ba_conf

    return confidence

def main():
    print(create_movie_rules(movie_data, 0.72, 1))

    
main()



