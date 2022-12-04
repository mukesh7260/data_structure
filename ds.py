	
			# linklist
		# 1. create a node. 
class Node:
  # constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next
first = Node(3)
print(first.data)

		#node create
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def Lprint(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_pos(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not prsent in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    		
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref        
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")
    def delete_begin(self):
	    if self.head is None:
	     	print("LL is empty !!")
	    else:
    		self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LL is empty ")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete LL is empty")
        if x == self.head.data:
            self.head = self.head.ref
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref 
        if n.ref is None:
            print("Node is not present ") 
        else:
            n.ref = n.ref.ref           
                
LL1 = Linkedlist()

LL1.insert_empty(54)
LL1.add_begin(34)
LL1.delete_begin()

LL1.add_before(353,34)
LL1.add_pos(67,34)
LL1.add_end(43)
LL1.delete_end()
LL1.delete_by_value(54)
LL1.Lprint()
        