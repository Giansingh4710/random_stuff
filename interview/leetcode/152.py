def ans(nums):
    maxx=0
    curr=0
    for i in range(len(nums)):
        if curr<0:
            curr=0
        curr*=nums[i]
        maxx=max(curr,maxx)
    return maxx
