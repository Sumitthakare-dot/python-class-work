num = int(input("Enetr a number:"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("prime number")
else:
    print("Not a prime number")            