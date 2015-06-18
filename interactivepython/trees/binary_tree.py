class Node:
    def __init__(self, rootValue=None, left=None, right=None):
        self.data = rootValue
        self.leftChild = left
        self.rightChild = right
    
    def __str__(self):
        return str(self.data)
        
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, nodeValue):
        if self.root is None:
            self.root = Node(nodeValue)
        else:
            self._insertNode(self.root, nodeValue)
    
    def _insertNode(self, node, nodeValue):
        if nodeValue <= node.data:
            if node.leftChild is None:
                node.leftChild = Node(nodeValue)
            else:
                self._insertNode(node.leftChild, nodeValue)
        else:
            if node.rightChild is None:
                node.rightChild = Node(nodeValue)
            else:
                self._insertNode(node.rightChild, nodeValue)
        
    def preorder(self, node):
        if node:
            print(str(node.data))
            self.preorder(node.leftChild)
            self.preorder(node.rightChild)
            
    def levelorder(self):
        alist = [self.root]
        while len(alist) > 0:
            print([node.data for node in alist])
            alist = [node.leftChild for node in alist if node.leftChild] + [node.rightChild for node in alist if node.rightChild]

    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.leftChild), self.height(node.rightChild))
        
    def isBalancedNaive(self, node): # O(n^2)
        ''' compute heights of each subtree '''
        if node is None: # base case
            return True
        else:
            if abs(self.height(node.leftChild) - self.height(node.rightChild)) > 1:
                return False
            else:
                return self.isBalancedNaive(node.leftChild) and self.isBalancedNaive(node.rightChild)
            
    def _checkHeight(self, node):
        ''' 
        check the height of each subtree as we recurse down from the root 
        if subtree is balanced: return its height, else: return -1
        '''
        if node is None: return 0
        
        leftHeight = self._checkHeight(node.leftChild)
        rightHeight = self._checkHeight(node.rightChild)
        
        if leftHeight == -1: return -1
        if rightHeight == -1: return -1

        if abs(leftHeight - rightHeight) > 1: return -1
        else: return max(leftHeight, rightHeight) + 1

    def isBalanced(self, node): # O(n)
        if self._checkHeight(node) == -1:
            return False
        else:
            return True
        
if __name__ == '__main__':
    #tree = BinaryTree(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))))
    tree = BinaryTree()
    #alist = [1, 0, 2, -1, 1.5, 3, 4, 5]
    alist = [15, 3, 20, 2, 4, 18, 1, 16, 21]
    for x in alist:
        tree.insert(x)
    #tree.preorder(tree.root)
    tree.levelorder()
    print("Height of the tree is " + str(tree.height(tree.root)))
    print(tree.isBalancedNaive(tree.root))
    print(tree.isBalanced(tree.root))