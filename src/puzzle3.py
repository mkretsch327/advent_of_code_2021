import numpy as np
import pandas as pd

"""
Part 1:Find most common bit at each position (gamma)
Find least common bit (epsilon)

convert resulting numbers to decimal and multiply
"""
data = pd.read_csv('data/puzzle3.txt', sep=" ", converters={'number': lambda x: str(x)})
threshold = data.shape[0]/2
blown_data = data.number.str.split('', expand=True)
blown_data = blown_data[[1,2,3,4,5,6,7,8,9,10,11,12]].astype(int)
counts = blown_data.sum(axis=0)
most_likely = int((counts >= threshold).astype(int).astype(str).sum(), 2)
least_likely = int((counts < threshold).astype(int).astype(str).sum(), 2)

print(f"Gamma is {most_likely}, episilon is {least_likely}, product is {most_likely*least_likely}")


"""
Calculate life support rating by multiplyin gthe oxygen by CO2 scrubber rating

Oxygen: Start with first bit, calculate most common bit, then remove those without this one, till one number left,
convert to int

CO2: Start with first bit, calculate least common bit, then remove those without this one
"""
columns_ = [1,2,3,4,5,6,7,8,9,10,11,12]
data = pd.read_csv('data/puzzle3.txt', sep=" ", converters={'number': lambda x: str(x)})
threshold = data.shape[0]/2
blown_data = data.number.str.split('', expand=True)
blown_data = blown_data[columns_].astype(int)

current_data = blown_data.copy(deep=True)
for col in columns_:
    threshold = current_data.shape[0]/2
    most_common_bit = (current_data[col].sum()>=threshold).astype(int)
    current_data  = current_data[current_data[col] == most_common_bit]
    print(f"Current col = {col}; number of rows is {current_data.shape[0]}")

    if current_data.shape[0] == 1:
        o2_val = int(current_data.astype(str).values.sum(), 2)
        break

current_data = blown_data.copy(deep=True)
for col in columns_:
    threshold = current_data.shape[0]/2
    least_common_bit = ((current_data[col].sum()<threshold)).astype(int)
    current_data  = current_data[current_data[col] == least_common_bit]
    print(f"Current col = {col}; number of rows is {current_data.shape[0]}, ")
    if current_data.shape[0] == 1:
        co2_val = int(current_data.astype(str).values.sum(), 2)
        break

"2621178 too low"
print(f"Final reading product: {o2_val}, {co2_val} and product {o2_val*co2_val}")
