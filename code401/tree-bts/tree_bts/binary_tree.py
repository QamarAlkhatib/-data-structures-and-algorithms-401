
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self,root):
        '''
        Pre-order: root >> left >> right
        '''
        output = []
        # closure function, private function.
        def _traverse(_root):
            if _root is None: 
                return ("root tree is empty")

            output.append(_root.value)
            if _root.left is not None:
                _traverse(_root.left)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse
      
    def in_order(self,root):
        '''
        left >> root >> right
        '''
        output = []
        # closure function, private function.
        def _traverse(_root):
           if _root is None: 
                return ("root tree is empty")


           if _root.left is not None:
               _traverse(_root.left)
        
           output.append(_root.value)

           if _root.right is not None:
               _traverse(_root.right)
           return output
        return _traverse
        
    def post_order(self,root):
        '''
        left >> right >> root
        '''
        output = []
        # closure function, private function.
        def _traverse(_root):
           if _root is None: 
                return ("root tree is empty")
           if _root.left is not None:
               _traverse(_root.left)

           if _root.right is not None:
               _traverse(_root.right)
           output.append(_root.value)
           return output
        return _traverse

class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()


    def add(self,value):
        if self.root is None:
          self.root = Node(value)
          return self.root
        if value < self.root.value:
            self.root.left = self.add(self.root.left,value)
        else:
            self.root.right = self.add(self.root.right,value)
        return self.root

    def contains(self,value):

        while self.root:
            if self.root == value:
                return True
            if self.root.value > value:
                self.root = self.root.left
            else:
                self.root = self.root.right
        return False
