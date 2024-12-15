'''#simple calculator
num1 = float(input("Enter frist number:"))
num2 = float(input("Enter secound number;"))
sum_result = num1+num2
print("Sum is: ",sum_result)'''

'''num1 = float(input("Enter a frist number: "))
num2 = float(input("Enter a secound number:"))
sum_result = num1+num2
print("Sum is:",sum_result)'''


'''#simple calculator
num1 =float(input("Enter frost number:"))
num2 =float(input("Enter secound number:"))
sum_result =num1 + num2
print("sum is:" , sum_result)

#Check if number is even or odd
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")'''

'''num = int(input("Enter a number:"))
if num% 2 == 0:
    print(f"{num}is even")
else:
    print(f"{num}is odd")    '''

'''#check if number is even or odd
num = int (input("Enter a number:"))
if num%2 ==0:
    print(f"{num}is even")
else:
    print(f"{num}is odd")'''

'''#check if number is prime
num = int(input("Enter a number:"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")'''

'''#check if number is prime
num = int(input("Enter a number:"))
if num > 1:
 for i in range(2,num):
  if num % i == 0:
   print(f"{num}is not prime")
   break
  else:
   print(f"{num} is prime")
 else:
  print(f"{num}is not prime")'''


'''#factorial of a number
num = int(input("Enter a number:"))
factorial = 1
for i in range(1, num + 1):
    factorial *=i
    print(f"The factorial of{num}is{factorial}")'''

'''#factorial of a number
num = int(input("Enter a number:"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
    print(f"The factorial of {num}is {factorial}")'''        



'''word= input("Enter a word:")
if word == word[::-1]:
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}'is not a palindrome")   

word = input("Enter a word:")
if word == word[::-1]:
    print(f"'{word}'is a palindrome")
else:
    print(f"'{word}'is not palindrome")  

word = input("Enter a word:")
if word == word[::-1]:
    print(f"'{word}'is palindrome")
else:print(f"'{word}is not palindrome")  '''
            