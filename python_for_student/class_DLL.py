#class_DLL.py
class Node:
  def __init__(self, value=None, next=None, prev=None):
     self.val, self.prev, self.next = value, prev, next
class doubly_linked_list:
def __init__(self):
   self.head, self.tail, self.count = None, None, 0
  def append(self, value):
     new_node = Node(value, None, None)
     if self.head is None: # 텅 빈 DLL이라면 새로운 head/tail로 (d1)
       self.head = new_node # 새 item을 DLL의 head로 지정하고 
       self.tail = self.head # 지금은 하나뿐이므로 head가 곧 tail
     else:  # 새로운 tail로 (d2)
       new_node.prev = self.tail # 뭔가 있다면 꼬리에다 갖다 붙여 
       self.tail.next = new_node
       self.tail = new_node # 새 node가 새로운 꼬리가 되겠지
     self.count += 1     
  def delete(self, value):
     node = self.head  # head부터 출발해서 
     node_deleted = False # 지워질 때까지는 지워진 게 아니다.
     if node is not None: # node(head)에 뭔가 있는 경우에만 
       if node.val==value: # head.val가 바로 value라면 (e1)
         self.head = node.next
         self.head.prev = None
         node_deleted = True
       elif self.tail.val==value: # tail.val가 value라면 (e2)
         self.tail=self.tail.prev # 현 tail의 전 node를 tail로 
         self.tail.next = None # 그 tail의 next를 None으로 
         node_deleted = True
       else: # head도 tail도 아닌 중간 node에 value가 있는 경우 (e3)
         while node: # head부터 tail의 다음 node인 None전까지 
           if node.val == value:
             node.prev.next = node.next
             node.next.prev = node.prev
             node_deleted = True
           node = node.next # value나  None을 만날 때까지
     if node_deleted:   self.count -= 1
  def print(self):
     node = self.head # head부터 출발해서 
     while node: # None을 만날 때까지 계속
       print(node.val, end='-') # 현 node의 value를 print
       node = node.next # 다음 node로 넘어가            
     print('None')   # None으로 마무리
  def insert(self, value, x=None):
     # Insert a node of value after the node of x
     new_node = Node(value, None, None)
     if self.head is None:  # 텅빈 DLL이라면 
       self.head = new_node # 새 node를 DLL의 head로 지정하고 
       self.tail = self.head # 지금은 하나뿐이므로 head이자 tail
     else:
       n = self.head # head부터 출발해서
       while n is not None:
         if n.val == x:  # node n의 값이 x이면
           break
         n = n.next  # 아니면 그 다음 node로 넘어가서 while loop 계속 
       if n is not None: # x가 node n의 value로 찾아졌으면 
         new_node.prev = n # 그 다음에 갖다붙여
         new_node.next = n.next
         n.next = new_node
       else:   # x가 찾아지지 않았으면
         new_node.prev = self.tail # tail에다 갖다 붙여 
         self.tail.next = new_node
         self.tail = new_node  # 그럼 새 node가 새로운 tail이 되겠지
       self.count += 1
