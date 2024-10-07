class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        ################################################################
class Solution(object):
    def addTwoNumbers(self, l1, l2): 
        carry = 0
        dummy_head = ListNode(0) 
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry
            
            carry = total_sum // 10
            current.next = ListNode(total_sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

l1 = ListNode(2, ListNode(4, ListNode(3)))  
l2 = ListNode(5, ListNode(6, ListNode(4)))  

S = Solution()
result = S.addTwoNumbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output)  