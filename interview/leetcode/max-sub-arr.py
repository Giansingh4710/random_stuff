class Soulution:
    def maxSubArray(self,nums):
        maxx=0
        for i in range(len(nums)):
            tempMax=0
            for j in range(i+1,len(nums)):
                tempMax=max(tempMax,sum(nums[i:j]))
            maxx=max(tempMax,maxx)
        return maxx


lst=[-2,1,-3,4,-1,2,1,-5,4]
a=Soulution()
b=a.maxSubArray(lst)
print(b)
