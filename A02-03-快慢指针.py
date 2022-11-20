

"""
142. Linked List Cycle II https://leetcode.com/problems/linked-list-cycle-ii/

快慢指针检测链表里的环
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            # 有环时，这个条件比定成立；否则，一定无环
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                slow = head
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                
                return slow
            
        return None
                
            
    