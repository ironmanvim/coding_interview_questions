
import functools


class Solution:
    def longestPalindrome(self, s):
        # Fill this in.
        palindrome_matches = []

        for i in range(0, len(s)):
            palindrome_matches.append(self.longPalindrome(s, i, i))
            try:
                if s[i] == s[i + 1]:
                    palindrome_matches.append(self.longPalindrome(s, i, i + 1))
            except IndexError:
                pass

        palindrome_max_len = max([i[1] - i[0] for i in palindrome_matches])
        palindrome_max_matches = [
            i for i in palindrome_matches if i[1] - i[0] == palindrome_max_len
        ]

        return [s[i[0]: i[1]+1] for i in palindrome_max_matches]

    def longPalindrome(self, s, b, f):
        while b >= 0 and f < len(s):
            if s[b] == s[f]:
                b -= 1
                f += 1
            else:
                break
        return b + 1, f - 1


# Test program
s = "tracecarsaaaaaaaa"
print(str(Solution().longestPalindrome(s)))
# racecar
