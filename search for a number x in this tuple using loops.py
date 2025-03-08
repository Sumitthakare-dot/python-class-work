nums =(1, 4, 9, 25, 36, 49, 81, 100,81)
x = 81
idx = 0
for el in nums:
    if(el == x):
        print("number found at ind",idx)
        break
        idx += 1 