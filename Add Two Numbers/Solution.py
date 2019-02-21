#! python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ptr = self.next
        str = "" + self.val.__str__()
        while ptr != None:
            str += " -> " + ptr.val.__str__()
            ptr = ptr.next
        return str

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        carry = False
        p1 = l1
        p2 = l2
        last = None
        while p1 != None and p2 != None:
            sum = p1.val + p2.val
            if carry:
                sum += 1
            if sum >= 10:
                p1.val = sum - 10
                p2.val = sum - 10
                carry = True
            else:
                p1.val = sum
                p2.val = sum
                carry = False
            last = p1
            p1 = p1.next
            p2 = p2.next
        if p1 == None and p2 == None and carry:
            last.next = ListNode(1)
            return l1
        result = None
        if p1 == None:
            self.dealCarray(p2, carry)
            result = l2
        else:
            self.dealCarray(p1, carry)
            result = l1
        return result

    def dealCarray(self, l: 'ListNode', carry: bool):
        if carry != True:
            return
        last = None
        while l != None and carry:
            sum = l.val + 1
            if sum >= 10:
                l.val = sum - 10
                carry = True
            else:
                l.val = sum
                carry = False
            last = l
            l = l.next
        if l == None and carry:
            last.next = ListNode(1)
        


if __name__ == "__main__":
    l1 = ListNode(5)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    print(l1)
    l2 = ListNode(5)
    l2.next = ListNode(9)
    l2.next.next = ListNode(1)
    print(l2)
    solution = Solution()
    result = solution.addTwoNumbers(l2, l1)
    print(result)
