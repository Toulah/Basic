
# Solving quadratic equation using the quadratic formula
# x=(-b+-Sqrt(b^2-4ac))/2a
from math import sqrt

a = 5
b = 6
c = 1

x1 = (-b + (sqrt(b**2 - 4*a*c)))/(2*a)
x2 = (-b - (sqrt(b**2 - 4*a*c)))/(2*a)

print("x1 = ",x1)
print("x2 = ",x2)
