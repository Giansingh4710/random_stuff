class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap={"I":1,
                 "V":5,
                 "X":10,
                 "L":50,
                 "C":100,
                 "D":500,
                 "M":1000
                }
        ans=0
        for i in range(len(s)):
            ans+=hashMap[s[i]]
            if (s[i]=="V" or s[i]=="X") and s[i-1]=="I":
                ans-=1*2
            if (s[i]=="L" or s[i]=="C") and s[i-1]=="X":
                ans-=10*2
            if (s[i]=="D" or s[i]=="M") and s[i-1]=="C":
                ans-=100
            
            
        return ans
        
        
a=Solution()
b="IV"
b="MMMCDXC"
print(a.romanToInt(b))

