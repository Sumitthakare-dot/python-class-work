# age =int(input("Enetr your age:"))
# if age<13:
#     print("child")
# elif age < 20:
#     print("""Teenger""") 
# elif age < 60:
#     print("Adult")
# else:
#     print("senior")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero"
else:
    result = "Invalid operation"

print("Result:", result)
