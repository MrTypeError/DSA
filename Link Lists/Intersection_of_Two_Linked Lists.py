class Solution:
    def getIntersectionNode(self, headA , headB):
        s=set()
        while headA :
            s.add(id(headA))
            headA = headA.next
        while headB :
            if id(headB) in s:
                return headB
            headB = headB.next
        return None
            