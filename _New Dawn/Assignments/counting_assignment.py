# import panda
# climatic_data = panda.read_csv(r"C:\Users\Omotola\Downloads\en_climate_daily_ON_6139530_2022_P1D.csv")
# print(climatic_data)

import csv

# import rows as rows

climatic_data = open(r"C:\Users\Omotola\Downloads\climate_daily.csv")
print(climatic_data)

climatic_data_csv = csv.reader(climatic_data)

header = []
header = next(climatic_data_csv)
print(header)

rows = []
for x in climatic_data_csv:
    rows.append(x)
print(rows)

zero_count = rows.count("2022")
# print(zero_count)
if "Longitude (x)" in header:
    print("yes")

if "Total Precipitation (mm)" in header:
        print("yes")

# get the index of Total Precipitation
precipitation_pos = (header.index("Total Precipitation (mm)"))
print(precipitation_pos)

total_precipitation = rows[precipitation_pos]
print(total_precipitation)


