# Definition for singly-linked list.
class ListNode (object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        result = ListNode(c)
        if l1 and l2:
            result.val += l1.val + l2.val

            c = result.val // 10
            result.val = result.val % 10

            result.next = self.addTwoNumbers(l1.next, l2.next, c)

            return result

        if l1:
            result.val += l1.val

            c = result.val // 10
            result.val = result.val % 10

            result.next = self.addTwoNumbers(l1.next, l2, c)

            return result

        if l2:
            result.val += l2.val

            c = result.val // 10
            result.val = result.val % 10

            result.next = self.addTwoNumbers(l1, l2.next, c)

            return result

        if c > 0:
            return result

        return None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l2 = ListNode(1)
l2.next = ListNode(6)
l2.next.next = ListNode(6)
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end='')
    result = result.next

print()
# 7 0 8
