# linear search alogrithm
class Solution:
    def getRange(self, arr, target):
        # Fill this in.
        try:
            start_index = arr.index(target)
            last_index = start_index + 1

            try:
                while arr[last_index] == target:
                    last_index += 1
            except IndexError:
                pass

            return [start_index, last_index - 1]
        except ValueError:
            return [-1, -1]


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
