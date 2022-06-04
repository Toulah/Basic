# Exercise 1
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included)
# make them each of the sets into a list


num = []
i = 1500
while i <= 2700:
    # print(i)
    num.append(i)
    i += 5
print(num)
print(len(num))
print(type(num))

print("")
num_2 = []
j = 1500
j = ((j // 7) + 1) * 7
while j <= 2700:
    # print(j)
    num_2.append(j)
    j = ((j // 7) + 1) * 7

print(num_2)
print(len(num_2))



num_range = range(1500, 2700)
num_3 = []
for n in num_range:
    if n % 7 == 0:
        num_3.append(n)
print(num_3)

print("""

""")

# Exercise 2
# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
print("Temperature Conversion to and from celsius to fahrenheit")
temperature_unit = input("If conversion is from celsius, type C, otherwise, type F: ", )
temperature_input = input("input temperature:")
temperature_unit = temperature_unit.upper()

if temperature_unit == "C":
    f = ((int(temperature_input)//5 * 9) + 32)
    print(f), chr(176),"C"
else:
    c = ((int(temperature_input)) - 32) * 5 // 9
    print(c), chr(176), "F"
