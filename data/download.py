import wget

male = "https://storage.googleapis.com/flywire-data/challenges/vnc_matching/male_connectome_graph.csv.gz"
female = "https://storage.googleapis.com/flywire-data/challenges/vnc_matching/female_connectome_graph.csv.gz"
benchmark = "https://storage.googleapis.com/flywire-data/challenges/vnc_matching/vnc_matching_submission_benchmark_5154247.csv.gz"

male_data = "male.gz"
female_data = "female.gz"
benchmark_data = "benchmark.gz"
wget.download(male, male_data)
wget.download(female, female_data)
wget.download(benchmark, benchmark_data)

print("download successful")