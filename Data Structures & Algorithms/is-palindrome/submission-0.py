class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove whitespace
        s = s.lower()
        s = s.replace(" ", "")
        for i in s: 
            if not i.isalnum():
                print(i)
                s=s.replace(i, "")
        print(s, s[::-1])
        return s == s[::-1]

        