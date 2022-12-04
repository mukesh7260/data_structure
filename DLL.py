


class Node:
    def __init__(self , data): 
        self.data = data
        self.nref = None 
        self.pref = None 

class DoublyLL:
    def __init__ (self):
        self.head = None

    def print_LL(self):             # forward direction traversing  DLL
        if self.head is None:
            print("linked list is empty ") 
        
        else:
            n = self.head 
            while n is not None:
                print(n.data, end = " ")
                n = n.nref

    def print_LL_reverse(self):         # backword direction traversing DLL
        print()
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, end = " ")
                n = n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def  add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def  add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty !!")
        else:
            n = self.head
            while n is not None:
                if x == n.data: 
                    break 
                n = n.nref 
            if n is None:
                print("Give node is not present in DLL") 
            else:
                new_node = Node(data) 
                new_node.nref = n.nref
                new_node.pref = n 
                if n.nref is not None:
                    n.nref.pref = new_node 
                n.nref = new_node 

    def add_before(self,data,x): 
        if self.head is None:
            print("LL is empty !!")
        else:
            n = self.head
            while n is not None:
                if x == n.data: 
                    break 
                n = n.nref 
            if n is None:
                print("Give node is not present in DLL") 
            else:
                new_node = Node(data) 
                new_node.nref = n 
                new_node.pref = n.pref 
                if n.pref is not None:
                    n.pref.nref = new_node 
                else:
                    self.head = new_node 
                    n.pref = new_node 

    def delete_beging(self):
        if self.head is None:
            print("DLL is emtpy can't delete ") 
        if self.head.nref is None: 
            self.head = None 
            print("DLL is empty after deleting the node ")
        else:
            self.head = self.head.nref 
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("DDL is empty so, can't delete ") 
        
        if self.head.nref is None:
            self.head = None 
            print("DDL is empty after deleltion the node")

        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref 
                n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x==n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data==x:
                n.pref.nref = None
            else:
                print("x is not present in dll!")
            

DLL = DoublyLL()
DLL.add_begin(35)
# DLL.add_end(323)
# DLL.insert_empty(20)
DLL.add_after(54,35)   
DLL.add_before(67,54)
DLL.add_after(55,54)
DLL.delete_by_value(55)
# DLL.delete_end()
# DLL.delete_beging()    
DLL.print_LL()
DLL.print_LL_reverse()



                                ### Circular linked list. 

class Node:
    def __init__(self , data): 
        self.data = data
        self.nref = None 
        self.pref = None 

class Circular_Linked_List:
    def __init__ (self):
        self.head = None

    def print_LL(self):             # forward direction traversing  DLL
        if self.head is None:
            print("linked list is empty ") 
        
        else:
            n = self.head 
            while n is not None:
                print(n.data, end = " ")
                n = n.nref

    def insert_begin(self,data):
            new_node=Node(data)
            new_node.ref=self.head
            n=self.head
            
            if n is None:
                self.head=new_node
                self.end=new_node
                self.head.ref=new_node
                return
            
            if self.end is not None:
                self.end.ref=new_node
                new_node.ref=self.head
                self.head=new_node
                return     

    def add_after(self,data,x):
        n=self.head
        while n is not self.end:
            if n.data==x:
                break
            n=n.ref 
        
        if n.data != x :
            print("node is not present in Linked List")
            return
        if n.data is self.end:
            self.insert_end
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node           
    
    def add_before(self,data,x):
        n=self.head
        if n is None:
            print("circular linked list is empty")
            return
        if n.data==x:
            self.insert_begin(data)
            return
     
        while n.ref is not self.end:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref.data != x:
            print("node not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node       
                       
    def deleteStart(self):    
            
        if(self.head == None):
            print("linked list is empty")
                
        else:    
              
            if(self.head != self.end ):    
                self.head = self.head.ref;    
                self.end.ref = self.head;    
            
            else:    
                self.head = self.end = None;      
        
    def delete_from_end(self):  
        if(self.head == None):  
            return 
        else:  
            if(self.head != self.end ):  
                n = self.head              
                while(n.ref != self.end):  
                    n = n.ref  
                self.end = n 
                self.end.ref = self.head;  
            else:  
                self.head = self.end = None;           
    
    def delete_any(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if x==self.head.data:
            self.deleteStart()
            return
        n =self.head
        while n.ref is not self.end:
            if x==n.ref.data:
                break
            n=n.ref    
        if n.ref.data != x:
            print("node is not present !!")
        else:
            n.ref=n.ref.ref

circularlist = Circular_Linked_List()
circularlist.insert_begin(10)
circularlist.insert_begin(20)
circularlist.insert_begin(30)
circularlist.insert_begin(40)
circularlist.insert_end(50)
circularlist.add_after(15,50)
circularlist.add_before(15,10)
circularlist.delete_start()
circularlist.delete_from_end()
circularlist.delete_any(50)
circularlist.traverse()