class Solution:
    def isValid(self, s):
        # Fill this in.
        open_braces = tuple("({[")
        close_braces = tuple(")}]")
        stack = []

        for i in s:
            if i in open_braces:
                stack.append(i)
            elif i in close_braces:
                try:
                    if stack[len(stack) - 1] == open_braces[close_braces.index(i)]:
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        
        if len(stack) == 0:
            return True
        return False


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "(heelo){what the}"
# should return True
print(Solution().isValid(s))
