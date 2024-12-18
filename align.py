from pandas import read_csv

male_edges = {(r[0], r[1]): int(r[2]) for r in read_csv("data/male.gz")[1:]}
female_edges = {(r[0], r[1]): int(r[2]) for r in read_csv("data/female.gz")[1:]}
matching = {r[0]: r[1] for r in read_csv("data/benchmark.gz")[1:]}
alignment = 0
for male_nodes, edge_weight in male_edges.items():
  female_nodes = (matching[male_nodes[0]], matching[male_nodes[1]])
  alignment += min(edge_weight, female_edges.get(female_nodes, 0))
print(f"{alignment=}")