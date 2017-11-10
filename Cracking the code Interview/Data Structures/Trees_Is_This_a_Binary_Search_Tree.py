""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def traverse(tree):
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.left)
        res2 = postordereval(tree.right)
        if res1 > res2:
            return False
def checkBST(root):
    
    print(list(traverse(root)))
    

