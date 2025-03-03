import math

num = int(input("Enetr a number:"))
sqrt = int(math.sqrt(num))

if sqrt * sqrt == num:
    print(f"{num}is a perfect square")
else:
    print(f"{num}is not a perfect square")    