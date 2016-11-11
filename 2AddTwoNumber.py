# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return trans_to_node(trans_to_int(l1),trans_to_int(l2))
        

def getListNode(x,next_node):
    node = ListNode(x)
    node.next = next_node
    return node


def trans_to_int(node):
    curr_node = node
    val_list,sum = [],0

    val_list.append(curr_node.val)

    while curr_node.next:
        val_list.append(curr_node.next.val)
        curr_node = curr_node.next

    for i,num in enumerate(val_list[::-1]):
        sum += num * (10**i)

    return sum


def trans_to_node(num):
    num_str = str(num)
    num_list = []
    for num_char in num_str:
        num_list.append(int(num_char))
    last_node = None
    for num in num_list:
        node = ListNode(num)
        node.next  = last_node
        last_node = node
    return last_node

if __name__ == '__main__':
    #[1,4,5] + [2,6,3]
    node1 = getListNode(3,None)
    node2 = getListNode(4,node1)
    node3 = getListNode(2,node2)

    node4 = getListNode(4,None)
    node5 = getListNode(6,node4)
    node6 = getListNode(5,node5)

    print(trans_to_int(node3))
    print(trans_to_int(node6))
    print(trans_to_int(node3) + trans_to_int(node6))
    print(trans_to_node(807).val)
    # print(trans_to_int(trans_to_node(245)))
    # solution = Solution()
    # result = solution(node3,node6)
