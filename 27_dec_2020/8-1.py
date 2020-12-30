class Solution:
    def convertToTitle(self, n):
        intercept = []
        carry = 0
        while n != 0:
            result = n % 26 + carry
            carry = 0
            if result <= 0:
                result = 26 + result
                carry = -1

            intercept.insert(0, chr(result + ord('A') - 1))
            n = n // 26


        if carry == -1:
            intercept.pop(0)
            carry = 0
        

        return "".join(intercept)


input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))

for i in range(1, 26 * 27 + 2):
    print(Solution().convertToTitle(i))
