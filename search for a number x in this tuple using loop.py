nums = (1,2,9,16,25,36,49,64,81,100,36)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding..")
    i += 1        
