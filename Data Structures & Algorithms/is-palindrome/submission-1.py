class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove whitespace
        s = s.lower()
        s = s.replace(" ", "")
        for i in s: 
            if not i.isalnum():
                s=s.replace(i, "")
        return s == s[::-1]

        