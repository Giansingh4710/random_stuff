#3. longest-substring-without-repeating-characters

"""
Given a string s, find the length of the longest substring without repeating character

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        maxStr=""
        for i in range(len(s)):
            newStr=""
            for j in range(i,len(s)):
                if s[j] not in newStr:
                    newStr+=s[j]
                else:
                    break
            if len(newStr)>len(maxStr):
                maxStr=newStr
        print(maxStr)
        return maxStr

a=Solution()
a.lengthOfLongestSubstring("abcabcbb")
            
            
            
                    
                
        