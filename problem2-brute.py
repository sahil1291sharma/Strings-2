class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sortedPattern = sorted(p)
        n = len(p)
        # print("Sorted Pattern: ",sortedPattern)
        result = []
        for i in range(len(s)-n+1):
            # print(i)
            temp = ""
            for j in range(i, i+n):
                temp += s[j]
            c = sorted(temp)
            if c == sortedPattern:
                result.append(i)
        return result
    
#time complexity is O(N*MlogM) where N is length of string "s" and M is length of pattern "p"
#Space complexity is O(N)