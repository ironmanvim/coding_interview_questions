# Definition for singly-linked list.
class ListNode (object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        l1_node = l1
        l2_node = l2
        result = ListNode(c)
        result_node = result

        while l1_node and l2_node:
            result_node.val = l1_node.val + l2_node.val + c

            c = result_node.val // 10
            result_node.val = result_node.val % 10

            l1_node = l1_node.next
            l2_node = l2_node.next
            if not l1_node and not l2_node:
                break

            result_node.next = ListNode(0)

            result_node = result_node.next

        while l1_node:
            result_node.val = l1_node.val + c

            c = result_node.val // 10
            result_node.val = result_node.val % 10

            l1_node = l1_node.next
            if l1_node is None:
                break

            result_node.next = ListNode(0)
            result_node = result_node.next

        while l2_node:
            result_node.val = l2_node.val + c

            c = result_node.val // 10
            result_node.val = result_node.val % 10

            l2_node = l2_node.next
            if l2_node is None:
                break

            result_node.next = ListNode(0)
            result_node = result_node.next

        if c > 0:
            result_node.next = ListNode(c)

        return result


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(7)
l2.next = ListNode(6)
l2.next.next = ListNode(6)
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end='')
    result = result.next

print()
# 7 0 8
