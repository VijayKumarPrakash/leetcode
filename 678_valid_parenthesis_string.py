class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket_stack = []
        asterisk_stack = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                bracket_stack.append(i)
            elif c == '*':
                asterisk_stack.append(i)
            elif c == ')':
                # Check bracket stack first
                if bracket_stack:
                    bracket_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False

        while bracket_stack and asterisk_stack:
            if asterisk_stack.pop() < bracket_stack.pop():
                return False

        return len(bracket_stack) == 0

# Test cases
solution = Solution()
print(solution.checkValidString("()"))  # True
print(solution.checkValidString("(*)"))  # True
print(solution.checkValidString("(*))"))  # True
print(solution.checkValidString("(*((()))()()()(*"))  # True
print(solution.checkValidString("(*(*"))  # True
print(solution.checkValidString("(((((())()))())())(()())())))((*)))))(()())()"))  # False
print(solution.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")) # True
