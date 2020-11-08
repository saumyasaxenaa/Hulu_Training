class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    currentNode = tree
    closest = float('inf')
    while currentNode:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if currentNode.value < target:
            currentNode = currentNode.right
        elif currentNode.value > target:
            currentNode = currentNode.left
        else:
            break
    return closest

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
print(findClosestValueInBst(root, 12))
