class Solution:
    def lengthOfLongestSubstring(self, s):
        cache = {}
        index = 0
        max_len = 0

        counter = 0
        while index < len(s):
            if s[index] not in cache.keys():
                counter += 1
                cache[s[index]] = True
            else:
                if max_len < counter:
                    max_len = counter
                counter = 0
                cache = {}
                index -= 1
            index += 1
        else:
            if max_len < counter:
                max_len = counter
            counter = 0
            cache = {}

        return max_len


print(Solution().lengthOfLongestSubstring('BBBB'))
