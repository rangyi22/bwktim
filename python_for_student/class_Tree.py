#class_Tree.py
class Tree:
  def __init__(self, x, L=None):
     self.val = x
     self.children = L
def show(node, depth=0):
   if node is not None:
     print(f'{node.val:10s} - ', end='')
     if node.children is not None:
       show(node.children[0], depth+1)
       for i in range(1,len(node.children)):
          print('\n' + ' '*(15*(depth+1)-3) + '- ', end='')     
          show(node.children[i], depth+1)
