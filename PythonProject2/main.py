import pydp as dp
from pydp.algorithms.laplacian import BoundedSum, BoundedMean, Count, Max
import pandas as pd
import statistics  # for calculating mean without applying differential privacy

# get carrots data from our public github repo
url = "https://raw.githubusercontent.com/OpenMined/PyDP/dev/examples/Tutorial_1-carrots_demo/animals_and_carrots.csv"
df = pd.read_csv(url, sep=",", names=["animal", "carrots_eaten"])
print(df.head())

# calculates mean without applying differential privacy
def mean_carrots() -> float:
    return statistics.mean(list(df["carrots_eaten"]))

# calculates mean applying differential privacy
def private_mean(privacy_budget: float) -> float:
    x = BoundedMean(privacy_budget, 0, 1, 100)
    return x.quick_result(list(df["carrots_eaten"]))

print("Mean: ", mean_carrots())
print("Private Mean: ", private_mean(0.8))

# Calculates number of animals who ate more than "limit" carrots without applying differential privacy.
def count_above(limit: int) -> int:
    return df[df.carrots_eaten > limit].count()[0]

# Calculates number of animals who ate more than "limit" carrots applying differential privacy.
def private_count_above(privacy_budget: float, limit: int) -> int:
    x = Count(privacy_budget, dtype="int")
    return x.quick_result(list(df[df.carrots_eaten > limit]["carrots_eaten"]))

print("Above 70:\t" + str(count_above(70)))
print("private count above:\t" + str(private_count_above(1, 70)))

# Function to return the maximum of the number of carrots eaten by any one animal without appyling differential privacy.
def max() -> int:
    return df.max()[1]

# Function to return the maximum of the number of carrots eaten by any one animal appyling differential privacy.
def private_max(privacy_budget: float) -> int:
    # 0 and 150 are the upper and lower limits for the search bound.
    x = Max(epsilon = privacy_budget, lower_bound = 0, upper_bound = 100, dtype="int")
    return x.quick_result(list(df["carrots_eaten"]))

print("Max:\t" + str(max()))
print("private max:\t" + str(private_max(1)))

# Function to calculate sum of carrots eaten without applying differential privacy.
def sum_carrots() -> int:
    return df.sum()[1]

# Function to calculate sum of carrots eaten applying differential privacy.
def private_sum(privacy_budget: float) -> int:
    x = BoundedSum(epsilon = privacy_budget, delta = 0, lower_bound= 1, upper_bound = 100, dtype="float")
    return x.quick_result(list(df["carrots_eaten"]))

print("Sum:\t" + str(sum_carrots()))
print("Private Sum:\t" + str(private_sum(1)))