class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            next = False
            for j in range(len(t)):
                if s[i] == t[j]:
                    t = t[:j] + t[j+1:]
                    next = True
                    break
            if next == False:
                return False
        return True