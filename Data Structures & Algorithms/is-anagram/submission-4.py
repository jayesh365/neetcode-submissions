class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s =set(s)
        s_t =set(t)

        if len(s) != len(t): return False

        # count freq of chars in both strings
        temp_s = {}
        for _, v in enumerate(s):
            if v not in temp_s: temp_s[v] = 1
            else: temp_s[v] += 1
        
        temp_t = {}
        for _, v in enumerate(t):
            if v not in temp_t: temp_t[v] = 1
            else: temp_t[v] += 1
        # print(temp_s)
        # print(temp_t)
        return temp_s == temp_t and s_s == s_t