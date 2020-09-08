import itertools

class Solution:
    def largestTimeFromDigits(self, arr):
        arr.sort(reverse=True)
        
        for h, i, j, k in itertools.permutations(arr):
            if h*10+i < 24 and j*10+k < 60:
                return str(h)+str(i)+':'+str(j)+str(k)
        else:
            return ""

print(Solution().largestTimeFromDigits([0,0,1,0]))