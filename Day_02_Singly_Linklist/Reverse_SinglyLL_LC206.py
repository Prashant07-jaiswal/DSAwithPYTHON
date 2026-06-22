class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr != None:
            # 1. Save the next node so we don't lose the rest of the list
            next_node = curr.next 
            
            # 2. Reverse the link (point backwards to 'prev')
            curr.next = prev 
            
            # 3. Move 'prev' forward one step
            prev = curr 
            
            # 4. Move 'curr' forward one step
            curr = next_node 
            
        # By the end, 'curr' is None, and 'prev' is the new head of the reversed list
        return prev
        