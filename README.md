# Association Rule Mining

This project contains two simple implementations of association rule mining in Python. The goal is to find relationships between items that frequently appear together and calculate the confidence of those relationships.

The project uses two examples: movie genres and shopping items.

## What is Association Rule Mining?

Association rule mining is a technique used to find relationships between items in a dataset.

For example, if customers who buy milk also frequently buy bread, we can create a rule:

`milk -> bread`

The confidence of this rule tells us how often bread appears in transactions that contain milk.

## How It Works

Both implementations follow the same general approach:

1. **Count individual items:** Count how many times each genre or item appears in the dataset.
2. **Count pairs:** Count how many times each pair of items appears together.
3. **Calculate confidence:** Calculate the confidence in both directions for each pair.
4. **Apply thresholds:** Keep only the rules that satisfy the minimum count and confidence threshold.

The confidence of a rule is calculated as:

`Confidence(A -> B) = Count(A, B) / Count(A)`

Here, `Count(A, B)` is the number of transactions containing both items, while `Count(A)` is the number of transactions containing item A.

Since the confidence can be different in each direction, `A -> B` and `B -> A` are evaluated separately.

## Files

### 1. Movie Genre Rules

This implementation works with a dataset of movies and their genres.

Each movie is represented as a list of genres, such as:

`['action', 'comedy', 'drama']`

The function `create_movie_rules()` counts the individual genres and genre pairs, calculates confidence, and returns the rules that satisfy the specified thresholds.

Example parameters:

- Confidence threshold: `0.72`
- Minimum count: `1`

### 2. Shopping Association Rules

This implementation uses a dataset of shopping transactions to find relationships between products.

Each transaction contains the items purchased together, such as:

`['milk', 'bread', 'eggs']`

The function `create_shopping_rules()` follows the same approach as the movie genre implementation. It also accepts an `itemset_maker` argument, allowing the function to work with a function that prepares the itemsets.

The current implementation uses `make_itemsets()`, which returns the original data without modifying it.

Example parameters:

- Confidence threshold: `0.6`
- Minimum count: `4`

## Requirements

- Python 3
- Standard Python libraries:
  - `collections`
  - `itertools`

No external libraries are required.

## Running the Code

Run either Python file directly:

```bash
python movie_rules.py
```

or

```bash
python shopping_rules.py
```

The program prints the association rules that satisfy the selected thresholds, along with their confidence values.

## What I Learned

This project helped me practice working with dictionaries, counting item occurrences, generating combinations, and calculating association rule confidence.

It also helped me understand how the same approach can be applied to different types of data, from movie genres to shopping transactions.
