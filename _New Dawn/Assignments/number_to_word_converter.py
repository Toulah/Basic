# Using dictionary to convert integer number to words
nums = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred",
        300: "three hundred", 400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred",
        800: "eight hundred", 900: "nine hundred", 1000: "one thousand", 2000: "two thousand", 3000: "three thousand",
        4000: "four thousand", 5000: "five thousand", 6000: "six thousand", 7000: "seven thousand",
        8000: "nine thousand", 9000: "nine thousand", 10000: "ten thousand", 20000: "twenty thousand"}

specimen = 10999

# numbers in specimen
if specimen in nums:
    ans_1 = nums.get(specimen)
    print(ans_1)
# for numbers less than 100 but not in nums
elif specimen <= 100:
    units = specimen % 10
    units = nums.get(units)
    tens = specimen//10
    tens = tens * 10
    tens = nums.get(tens)
    ans_2 = tens + " " + units
    print(ans_2)
# for numbers greater than 100, not nums and returns a value less than 20 when this
# (specimen - (specimen // 100) * 100) is evaluated e.g 112, 315, 1019
elif (specimen - (specimen // 100) * 100) <= 20:
    tens = (specimen - (specimen // 100) * 100)
    tens = nums.get(tens)
    hundreds = specimen // 100
    hundreds = hundreds * 100
    hundreds = nums.get(hundreds)
    ans_3 = hundreds + " and " + tens
    print(ans_3)
# for numbers greater than 100, not in num but less than 1000 e.g 525, 999
elif specimen < 1000:
    units = specimen % 100
    units = units % 10
    units = nums.get(units)
    tens = specimen % 100
    tens = tens // 10
    tens = tens * 10
    tens = nums.get(tens)
    hundreds = specimen // 100
    hundreds = hundreds * 100
    hundreds = nums.get(hundreds)
    ans_4 = hundreds + " and " + tens + " " + units
    print(ans_4)
# for number greater than a thousand but the hundredth value is zero e.g 3025, 2046
elif (specimen > 1000) and (specimen % 1000) < 100:
    units = specimen % 1000
    units = units % 100
    units = units % 10
    units = nums.get(units)
    tens = specimen % 1000
    tens = tens % 100
    tens = tens // 10
    tens = tens * 10
    tens = nums.get(tens)
    thousands = specimen // 1000
    thousands = thousands * 1000
    thousands = nums.get(thousands)
    ans_6 = thousands + " and " + tens + " " + units
    print(ans_6)
else:
    units = specimen % 1000
    units = units % 100
    units = units % 10
    units = nums.get(units)
    tens = specimen % 1000
    tens = tens % 100
    tens = tens // 10
    tens = tens * 10
    tens = nums.get(tens)
    hundreds = specimen % 1000
    hundreds = hundreds // 100
    hundreds = hundreds * 100
    hundreds = nums.get(hundreds)
    thousands = specimen // 1000
    thousands = thousands * 1000
    thousands = nums.get(thousands)
    ans_5 = thousands + " " + hundreds + " and " + tens + " " + units
    print(ans_5)
