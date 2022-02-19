# Build a basic calculator

# Addition

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
operation = input("Operator: ")
# operation description (+, addition), (-, subtraction), (*, multiplication), (/, division)
# (**, power)

num_3 = eval(num_1 + operation + num_2)
# eval function converts num_3 from string to a mathematical expression
# It is therefore it does treat the operator as a mathematical operator rather than a string

print("Ans = ", num_3)