class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        prev = 0
        current = 0
        needleP= 0
    
        while current < len(haystack):
            if haystack[current] == needle[0]:
                while current < len(haystack) and needleP < len(needle) and haystack[current] == needle[needleP]:
                    current += 1
                    needleP += 1
                if needleP == len(needle): return prev
                else:
                    prev +=1
                    current = prev
                    needleP = 0

            else:
                prev +=1
                current = prev
        return -1

#Time complexity O(M*N)