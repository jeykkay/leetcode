def get_sum(nums:list,target:int):
    i=0
    for x in range(len(nums)):
        for y in range(i+1,len(nums)):
            if nums[x]+nums[y]==target:
                return [x,y]
print(get_sum([2,2,3,4],5))