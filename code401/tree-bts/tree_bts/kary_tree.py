
from stack_and_queue.queue import Queue,Node


class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

    def add_child(self,value):
        tree_node = Node(value)
        self.children.append(tree_node)

class KAryTree:
    def __init__(self):
        self.root = None
    
    def pre_order(self,node):
        if node is None:
            return ValueError
        
        i = 0 
        temp = None
        print("   ", node.value, end ="")
        while i < len(node.children):
            temp = node.children[i]
            self.pre_order(temp)
            i += 1

def fizzBuzz(n):

   tree = KAryTree()
   result = []
   result.append(n.root)
   while result is not None:
       val_first = result.pop()
       val = val_first.value
        
       if val % 3 == 0 and val % 5 == 0:
           tree.root.add_child(Node('FizzBuzz'))
       elif val % 3 == 0:
           tree.root.add_child(Node('Fizz'))
       elif val % 5 == 0:
           tree.root.add_child(Node('Buzz'))
       else:
            tree.root.add_child(Node(str(val)))
        
   return tree

tree = KAryTree()

tree.root = Node(10)
tree.root.add_child(9)
tree.root.add_child(5)
# adding children to 9
tree.root.children[0].add_child(3)
tree.root.children[0].add_child(7)
tree.root.children[0].add_child(2)

# adding nodes to 7
tree.root.children[0].children[1].add_child(30)
tree.root.children[0].children[1].add_child(11)

# adding children to 5
tree.root.children[1].add_child(15)
tree.root.children[1].add_child(21)
tree.root.children[1].add_child(12)

# adding nodes to 15
tree.root.children[1].children[0].add_child(25)
tree.root.children[1].children[0].add_child(1)

# adding nodes to 12

tree.root.children[1].children[2].add_child(75)
tree.root.children[1].children[2].add_child(41)

tree.pre_order(tree.root)

print(fizzBuzz(tree))




