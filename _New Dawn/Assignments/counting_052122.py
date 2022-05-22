import pandas as pd

# import data from csv file
# Data was downloaded from the Environment Canada website
climatic_data = pd.read_csv(r"C:\Users\Omotola\Downloads\climate_daily.csv")
print(climatic_data)

print("")
rows = []
for x in climatic_data:
    rows.append(x)
print(rows)

print("")
header = []
for y in climatic_data.columns:
    header.append(y)
print(header)

print("")
precipitation = climatic_data["Total Precipitation (mm)"]
print(precipitation)

print("")
total_precipitation = list(precipitation)
print(total_precipitation)

print("")
# Number of days that precipitation was zero
zero_precipitation = total_precipitation.count(0)
print(zero_precipitation)

# Maximum precipitation
print(max(total_precipitation))
print(total_precipitation.index(25.9))

# Using dictionary to convert integer number to words
num = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
       10: "ten", 11: "eleven", 12: "twelve"}

print(num.get(8))

print("")
print(type(climatic_data))
print(type(precipitation))
print(type(total_precipitation))
print(type(rows))
print(type(zero_precipitation))
print(type(num))

