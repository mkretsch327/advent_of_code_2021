import pandas as pd

"""
Part 1: Given list of readings, calculate how many readings are increasing from previous
"""
data = pd.read_csv('data/puzzle1.txt', sep=" ")
data['previous_reading'] = data['Reading'].shift(1)
data['delta'] = data['Reading'] - data['previous_reading']
data['increasing'] = (data['delta']> 0).astype(int)
print(data['increasing'].sum())

# 1832 increasing

"""
Part 2: Given list of readings, how many sliding 3-reading windows are incresing from previous measurements.
"""
data = pd.read_csv('data/puzzle1.txt', sep=" ")
data['reading_m1'] = data['Reading'].shift(0)
data['reading_m2'] = data['Reading'].shift(-1)
data['reading_m3'] = data['Reading'].shift(-2)
data["reading_sum"] = data['reading_m1'] + data['reading_m2'] + data['reading_m3']
data['previous_sum'] = data['reading_sum'].shift(1)
data['delta_sum'] = data['reading_sum'] - data['previous_sum']
data['increasing'] = (data['delta_sum'] > 0).astype(int)
print(f"When sliding window, there are {data['increasing'].sum()} instances")
# 1858 readings are increasing