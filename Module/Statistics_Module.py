#* =================== STATISTICS MODULE ===================

#^ import the statistics module
import statistics

#! basic dataset for examples
numbers = [10, 20, 30, 40, 50]
scores = [85, 90, 88, 92, 85, 78, 88]

#* ---------- MEAN (average) ----------
#? mean() returns arithmetic average
mean_val = statistics.mean(numbers)
print("Mean:", mean_val)

mean_scores = statistics.mean(scores)
print("Mean of scores:", mean_scores)

#* ---------- MEDIAN ----------
#& median() returns middle value
median_val = statistics.median(numbers)
print("Median:", median_val)

#! median with even count of items
data = [1, 2, 3, 4, 5, 6]
print("Median of even dataset:", statistics.median(data))

#~ median_low() returns lower middle value (for even count)
print("Median low:", statistics.median_low(data))

#? median_high() returns higher middle value (for even count)
print("Median high:", statistics.median_high(data))

#* ---------- MODE ----------
#& mode() returns most frequent value
mode_val = statistics.mode(scores)
print("Mode (most frequent):", mode_val)

data_with_mode = [1, 1, 2, 2, 2, 3, 3, 3, 3]
print("Mode:", statistics.mode(data_with_mode))

#* ---------- VARIANCE ----------
#! variance() is for sample data (divides by n-1)
var_sample = statistics.variance(numbers)
print("Variance (sample):", var_sample)

#? pvariance() is for population data (divides by n)
var_pop = statistics.pvariance(numbers)
print("Variance (population):", var_pop)

#* ---------- STANDARD DEVIATION ----------
#& stdev() for sample standard deviation
std_sample = statistics.stdev(scores)
print("Standard Deviation (sample):", std_sample)

#! pstdev() for population standard deviation
std_pop = statistics.pstdev(scores)
print("Standard Deviation (population):", std_pop)

#~ ---------- QUANTILES (Python 3.8+) ----------
#todo quantiles() divides data into equal groups
data_large = list(range(1, 101))
quant = statistics.quantiles(data_large, n=4)
print("Quartiles:", quant)

#* ---------- EXAMPLE: ANALYZING TEST SCORES ----------
test_scores = [78, 85, 92, 88, 76, 95, 89, 91, 83, 87]

#^ summary statistics
print("\n#*=== TEST SCORES ANALYSIS ===")
print("Data:", test_scores)
print("Mean:", statistics.mean(test_scores))
print("Median:", statistics.median(test_scores))
print("Stdev:", round(statistics.stdev(test_scores), 2))
print("Min:", min(test_scores))
print("Max:", max(test_scores))

#! ---------- EXAMPLE: HANDLING EDGE CASES ----------
#? single value
single = [42]
print("\nSingle value mean:", statistics.mean(single))

#& identical values
identical = [5, 5, 5, 5]
print("Identical values variance:", statistics.variance(identical))

#~ floats with statistics
floats = [1.5, 2.7, 3.2, 4.8]
print("Float mean:", statistics.mean(floats))

#todo empty data would raise StatisticsError
# statistics.mean([])  # ERROR!

#* ---------- COMPARISON: MEAN vs MEDIAN ----------
normal = [1, 2, 3, 4, 5]
with_outlier = [1, 2, 3, 4, 100]

print("\nNormal data:")
print("  Mean:", statistics.mean(normal), "Median:", statistics.median(normal))

print("With outlier:")
print("  Mean:", statistics.mean(with_outlier), "Median:", statistics.median(with_outlier))

#^ end of statistics module examples