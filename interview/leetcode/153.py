[4,5,6,7,8,9,0,1,2,3]

def findMin(nums):
    left=0
    right=len(nums)-1
    while True:
        mid=(right+left)//2 
        a=changePoint(nums,mid)
        if a!=None:
            return a
        if nums[left]>nums[mid]:
            right=mid
        else:
            left=mid
        
def changePoint(nums,mid):
    if nums[mid-1]>nums[mid]:
        return nums[mid]
    if nums[mid]>nums[mid+1]:
        return nums[mid+1]
    return None
