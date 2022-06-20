'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        ans=""
        currentNode=ListNode(self.val,self.next)
        while(True):
            ans+=str(currentNode.val)+" -> "
            if(currentNode.next==None):
                break
            currentNode=currentNode.next
        return ans[:-4]

            
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1=""
        num2=""
        currentNode=l1
        while(True):
            num1+=str(currentNode.val)
            if currentNode.next==None:
                break
            currentNode=currentNode.next
            
        currentNode=l2
      
        while(True):
            num2+=str(currentNode.val)
            if currentNode.next==None:
                break
            currentNode=currentNode.next
       
        intAns=(int(num1[::-1])+int(num2[::-1]))
        ansStr=str(intAns)[::-1]
     
        ansNode=ListNode(ansStr[0])
        headNode=ansNode
        for i in range(1,len(ansStr)):
            ansNode.next=ListNode(ansStr[i])
            ansNode=ansNode.next            
        print(headNode)



a=ListNode(3)
b=ListNode(4,a)
l1=ListNode(2,b)

c=ListNode(4)
d=ListNode(6,c)
l2=ListNode(5,d)

# print(l2)

a=Solution()
a.addTwoNumbers(l1,l2)