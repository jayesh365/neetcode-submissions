class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2: return False
        stack = []
        other = []

        opens = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
            }

        for i in range(len(s)):
            # print('stack: ', stack)
            # print('curr: ', s[i])

            if s[i] in opens:
                stack.append(s[i])
            
            else:
                other.append(s[i])

                if not stack and other: return False
                # print('other: ', other, 'stack: ', stack)

                if s[i] != opens[stack[-1]]:
                    # print('top of stack: ', stack[-1], 'matching value: ', opens[stack[-1]])
                    return False
                else:
                    stack.pop(-1)
                    other.pop(-1)
        
        if len(other) != len(stack): return False
        
        return True
        