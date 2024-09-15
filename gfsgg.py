nums = [1,3,4,2,5,4,5,5,5,6,7,8,5,5,6]
count = 1
max1 = []
for n in range(len(nums)):
    if nums[n] == nums[n-1]:
        count +=1
    else:
        max1.append(count)
        count = 1
print(max(max1))