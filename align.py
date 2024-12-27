import pandas as pd

male = pd.read_csv("data/male.gz")
female = pd.read_csv("data/female.gz")
mapping = pd.read_csv("data/benchmark.gz")

domain = {tuple(row[:2]) : row[2] for row in male.values}
codomain = {tuple(row[:2]) : row[2] for row in female.values}

matching = {r[0]: r[1] for r in mapping.values}
alignment = 0

for male_nodes, edge_weight in domain.items():
  female_nodes = (matching[male_nodes[0]], matching[male_nodes[1]])
  alignment += min(edge_weight, codomain.get(female_nodes, 0))
print(f"{alignment=}")