#4. median-of-two-sorted-arrays

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).!!!!


Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        newArr=self.merged(nums1,nums2)
        mid=int(len(newArr)/2)
        ans= (newArr[(mid)-1]+newArr[mid])/2 #for when len is even
        if len(newArr)%2==1:
            ans= newArr[mid]
        print(float(ans))
        return ans
    def merged(self,arr1,arr2):
        newArr=[]
        i=0;
        j=0;
        while(len(newArr)!=len(arr1)+len(arr2)):
            if i>=len(arr1):
                for index in range(j,len(arr2)):
                    newArr.append(arr2[index])
                break
            elif j>=len(arr2):
                for index in range(i,len(arr1)):
                    newArr.append(arr1[index])
                break
            
            if(arr1[i]<arr2[j]):
                newArr.append(arr1[i])
                i+=1;
            else:
                newArr.append(arr2[j])
                j+=1;
        return newArr

def findMedianSortedArrays( nums1, nums2):
    if len(nums2)>len(nums1): #len of num1 will always be more than len of num2
        temp=nums2
        nums1=nums2
        nums2=temp
    mid1=len(nums1)//2
    mid2=((len(nums1)+len(nums2))//2)-mid1
    print(nums1[mid1],nums2[mid2])
    

arr1=[1,3]
arr2=[2]
a=Solution()
# a.findMedianSortedArrays(arr1,arr2)

findMedianSortedArrays(arr1,arr2)

