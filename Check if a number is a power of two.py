num = int (input("Enetr a number:"))

if(num & (num -1)) == 0:
    print(f"{num} is a power of two")
else:
    print(f"{num} is not a power of two")    