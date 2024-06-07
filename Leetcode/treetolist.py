class Node:
    def __init__(self,val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right



class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        # Do inorder traversal and make new tree
        def inorder(rr, ll):
            if rr:
                inorder(rr.left, ll)
                ll.append(rr.data)
                inorder(rr.right, ll)
        ll = []
        inorder(root, ll)
        head = None
        prev = None
        for elem in ll:
            nn = Node(elem)
            if not head:
                head = nn
            else:
                prev.right = nn
                nn.left = prev
            prev = nn
        prev.right = head
        head.left = prev
        return head
    
def displayTree(head):
    itr = head
    while itr.right != head:
        print(itr.data)
        itr = itr.right
    print(itr.data)
    head = itr
    while itr.left != head:
        print(itr.data)
        itr = itr.left
    print(itr.data)

s = Solution()
displayTree(s.bTreeToClist(Node(10, Node(20, Node(40), Node(60)), Node(30))))