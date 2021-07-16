class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        hashMap ={}
        for i in p:
            if i in hashMap:
                hashMap[i] +=1
            else:
                hashMap[i] = 1
        match = 0
        #starting with fast pointer "i" and iterating over the string
        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] -= 1
                if hashMap[s[i]] == 0:
                    match += 1
            if i >= len(p):
                if s[i-len(p)] in hashMap:
                    hashMap[s[i-len(p)]] += 1
                    if hashMap[s[i-len(p)]] == 1:
                        match -= 1
            if match == len(hashMap):
                result.append(i -len(p) + 1)
        return result

#Time complexity is O(M+N) M -> len(s) N -> len(p)
#Space complexity O(1)