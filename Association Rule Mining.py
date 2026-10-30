import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter', 'Eggs'],
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Eggs'],
    ['Milk', 'Bread', 'Eggs']
]

items = sorted(set(item for transaction in data for item in transaction))
encoded_data = []

for transaction in data:
    row = {}
    for item in items:
        row[item] = 1 if item in transaction else 0
    encoded_data.append(row)

df = pd.DataFrame(encoded_data).astype(bool)
print("Transaction Data:")
print(df)
frequent_itemsets = apriori(
    df,
    min_support=0.3,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets)
rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.6
)
print("\nAssociation Rules:")
print(
    rules[
        ['antecedents', 'consequents', 'support', 'confidence']
    ]
)
