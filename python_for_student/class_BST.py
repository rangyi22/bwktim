#class_BST.py
# convert a list of items to a height balanced BST 
class BSTnode:
  def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None
def BST_from_list(Lnum):
   if not Lnum: return None
   Lnum.sort()
   mid_val = len(Lnum)//2
   node = BSTnode(Lnum[mid_val])
   node.left = BST_from_list(Lnum[:mid_val])
   node.right = BST_from_list(Lnum[mid_val+1:])
   return node
def show(node, depth=0):
   if node is not None:
     print(f'{node.val:3d} - ', end='')
     show(node.left, depth+1)
     if node.right is not None:
       print('\n' + ' '*(6*(depth+1)-2) + '- ', end='')     
     show(node.right, depth+1)
