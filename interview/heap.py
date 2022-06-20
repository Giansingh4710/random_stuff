# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        pass
    
class MinHeap:
    def __init__(self,lst):
        self.lst=lst
        self.heapify()
    def add(self,num):
        self.lst.append(num)
        self.heapify()

    def heapify(self):
        for i in range(len(self.lst)):
            self.swap(i,len(self.lst)-1)
            if ((i-1)//2)<0:
                continue;
            while self.lst[(i-1)//2]>self.lst[i]:
                self.swap(i,(i-1)//2)
    def swap(self,i,j):
        temp=self.lst[i]
        self.lst[i]=self.lst[j]
        self.lst[j]=temp
    def heapSort(self):
        sortedLst=[]
        for i in range(len(self.lst)):
            sortedLst.append(self.lst.pop(0))
            self.heapify()
        print(sortedLst)
        
    def __str__(self):
        return str(self.lst)

a=MinHeap([65,81,21,2,3,4,1])
for i in range(10):
    a.add(i)
print(a)
a.heapSort()
        
    
    
        