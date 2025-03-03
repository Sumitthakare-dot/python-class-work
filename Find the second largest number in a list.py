nums = [int(x) for x in input("Enetr numbers separated by space:").split()]
nums.sort()

if len(nums) >= 2:
    print(f"The second largest number is {nums[-2]}")
else:
    print("List is too short")    