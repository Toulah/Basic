# Arithmetic Operators '+', '-', '*', '/', '**', '%', '//'

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x % y)
print(x // y)

# Assignment Operators '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=',
# '>>=', '<<=',
x += 5
print(x)

# x is now 20
x -= 5
print(x)

# x is now 15
x *= 5
print(x)

# x is now 75
x /= 5
print(x)

# x is now 15
x //= 2
print(x)

# x is now 7
x %= 4
print(x)

# x is now 3
x //= 4
print(x)

x = 3
x **= 4
print(x)

# Bitwise operators. Not entirely sure how the next two operators work

# x &= 3
# print(x)

# x |= 3
# print(x)

# x ^= 3
# print(x)

# x >>= 3
# print(x)

# x <<= 3
# print(x)

# python comparison operators '==', '!=', '>', '<', '>=', '<='
a = 5
b = 17

print(bool(a == b))
print(bool(a != b))
print(bool(a > b))
print(bool(a < b))
print(bool(a >= b))
print(bool(a <= b))