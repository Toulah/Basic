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
nums = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred",
        300: "three hundred", 400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred",
        800: "eight hundred", 900: "nine hundred", 1000: "one thousand"}

# zero_precipitation = 36

if zero_precipitation in nums:
    ans_1 = nums.get(zero_precipitation)
    print(ans_1)
else:
    units = zero_precipitation % 10
    units = nums.get(units)
    tens = zero_precipitation//10
    tens = tens * 10
    tens = nums.get(tens)
    ans_1 = tens + " " + units
    print(ans_1)


print("")
print(type(climatic_data))
print(type(precipitation))
print(type(total_precipitation))
print(type(rows))
print(type(zero_precipitation))
print(type(nums))
