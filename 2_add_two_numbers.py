# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        result = dummy
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            result.next = ListNode(sum)
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
    
# Example usage:
sol = Solution()
# Create linked list for l1: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
# Create linked list for l2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
# Add the two numbers
result = sol.addTwoNumbers(l1, l2)
# Print the result linked list: 7 -> 0 -> 8
while result:
    print(result.val, end=' ')
    result = result.next
# Output: 7 0 8
