'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        '''
        using XOR operation
        '''
        
        res = 0
        for ch in s+t:
            res ^= ord(ch)
            
        return chr(res)
        
        # using sorted list
        
#         s = sorted(s)
#         t = sorted(t)
        
#         l = len(s)
        
#         i = 0
#         j = 0
#         while i < l:
            
#             if s[i]==t[i]:
#                 i += 1
#                 j += 1
#             else: return t[j]

print(Solution().findTheDifference('abcdez', 'zedcmba'))