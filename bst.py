class BST:
    def __init__(self,key):
        self.key = key 
        self.lchild = None 
        self.rchild = None 


    def insert(self,data):
        if self.key is None:
            self.key = data 
            return 
        
        if self.key == data:
            return 
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data) 
            else:
                self.lchild = BST(data)
        
        else:
            if self.rchild:
                self.rchild.insert(data) 
            else:
                self.rchild = BST(data) 

    def search(self,data):
        if self.key == data:
            print('Node is found ') 
            return 
        if data < self.key:
            if self.lchild:
                self.lchild.search(data) 
            else:
                print("node is not present ") 
        else:
            if self.rchild:
                self.rchild.search(data) 
            else:
                print(" Node is not present in tree !!")

    def preorder(self):
        # print("pre-order")
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        # print("In-order") 
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end = " ") 
        if self.rchild:
            self.rchild.inorder() 

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ") 

    def delete(self,data,curr):
        if self.key is None:
            print(" Tree is empty !! ")
            return 
        
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Given Node is not present in the tree !!") 
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Given Node is not present in the tree") 
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr: 
                    self.key = temp.key 
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild 
                    temp = None 
                    return 
               
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp 
                    self.lchild = temp.lchild 
                    self.rchild = temp.rchild 
                    temp = None 
                    return 
                
            node = self.rchild 
            while node.lchild:
                node = node.lchild 
            self.key = node.key 
            self.rchild = self.rchild.delete(node.key,curr)
        return self 

# def count(node):
#     if node is None:
#         return 0 
#     return 1 + count(node.lchild)+ count(node.rchild) 

    def min_node(self):
        current = self 
        while current.lchild:
            current = current.lchild 
        print("node with smallest key is : !! ",current.key)
    
    def max_node(self):
        current = self 
        while current.rchild:
            current = current.rchild 
        print("node with maximum key is : !! ", current.key)
root = BST(10)
# print(root.key) 
# print(root.lchild)
# print(root.rchild) 
list1 = [12,34,25,46,78,234] 
for i in list1:
    print(root.insert(i))
# print(count(root)) 
# root.search(60) 
print("preorder")
root.preorder() 
print()
root.min_node()
root.max_node() 
# if count(root)>1:
#     root.delete(10) 
# else:
#     print("can't perform deleteion operation !!!")
# print()
# print("in-order",end=" ")
# root.inorder() 
# print("post-order ",end=" ") 
# root.postorder()
# root.delete(6) 
# print("after deleteing : !! ")
# root.preorder()
