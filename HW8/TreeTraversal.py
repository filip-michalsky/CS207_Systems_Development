
class BinaryTree():
    """
    This class creates a binary tree. We 
    
    """
    def __init__(self):
        #self.parent = None #initialize parent node
        self.key = None #initializing the Center of Activity (CoA)
        self.left = None #pointer to left child
        self.right = None #pointer to the right child
        self.min = None #initialize minimum
        self.parent = None
        self.current_depth = 0 #initialize current depth
    
    def find_max(self):
        #find min of the subtree
        if self.key is None:
            return None
        node = self
        while node.right is not None:
            node = node.right
        return node
        
    def insert(self,val):
        "Insert the value into the tree according to the BST property"
        if self.key == None: #base case
            self.key = val
        
        node = self
        
        while node.key != val:
            if node.key > val:
                if node.left is None: #if there is no child on the left, I need to create that subtree
                    node.left = self.__class__()
                    node.left.key = val
                    node.left.parent = node
                node = node.left
                    
            else:
                if node.right is None: #if there is no child on the right, I need to create that subtree
                    node.right = self.__class__()
                    node.right.key = val
                    node.right.parent = node
                #node.parent = node
                node = node.right
                
    def delete(self):
        "Deletes self's key from subtree and returns parent of removed node"
        node = self
        if (self.left is not None) and (self.right is not None):
            node = self.left.find_max()
            self.key = node.key
            
        if node.right is not None:
            node.replace(node.right)
        elif node.left is not None:
            node.replace(node.left)
            
        else:
            if node.parent is None:
                node.key = None
            elif node.parent.right is node:
                node.parent.right = None
            elif node.parent.left is node:
                node.parent.left = None
                
        return node
    
    def replace(self, node):
        "Replaces self's key, left, and right with node's key, left, and right"
        self.key = node.key
        self.left = node.left
        self.right = node.right
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self
            
    def remove(self,val):
        #print(self.key)
        if self.key == val:
            self.delete()

        else: #if we are not on the correct node, recurse either left or right
            if self.key > val:
                if self.left:
                    self.left.remove(val)
                    
            else:
                if self.right:
                    self.right.remove(val)
        
    def getValues(self,counter=0,depth=0,a=[]):
        
        #print("Current key:", self.key)
        if counter == depth: #base case
            a.append(self.key)
            return
        
        else:
            counter = counter + 1
            if self.left:
                #print("going left")
                self.left.getValues(counter,depth,a)
            else:
                b =pow(2,(depth-counter))
                #print(c*b)
                c=["None"]
                for i in c*b:
                    a.append(i)
            if self.right:
                self.right.getValues(counter,depth,a)
            else:
                b =pow(2,(depth-counter))
                c=["None"]
                #print(c*b)
                for i in c*b:
                    a.append(i)
        
        return a
    
    def print_postorder(self,a=[]):
        
        if self != None:
            if self.left:
                self.left.print_postorder()
            if self.right:
                self.right.print_postorder()
            #print(self.key)
            a.append(self.key)
            
        return a
    
    def print_preorder(self,a=[]):
        
        if self != None:
            #print(self.key)
            a.append(self.key)
            if self.left:
                self.left.print_preorder()
            if self.right:
                self.right.print_preorder()
        
        return a
    
    def print_inorder(self,a=[]):
        
        if self != None:
            if self.left:
                self.left.print_inorder()
            #print(self.key)
            a.append(self.key)
            if self.right:
                self.right.print_inorder()
        
        return a
    
    def __str__(self):
        "Returns ASCII drawing of the tree"
        s = str(self.key)
        if (self.left is not None) or (self.right is not None):
            ws = len(s)
            sl, wl, cl = [''], 0, 0
            if self.left is not None:
                sl = str(self.left).splitlines()
                wl = len(sl[0])
                cl = len(sl[0].lstrip(' _'))
            sr, wr, cr = [''], 0, 0
            if self.right is not None:
                sr = str(self.right).splitlines()
                wr = len(sr[0])
                cr = len(sr[0].rstrip(' _'))
            while len(sl) < len(sr):
                sl.append(' ' * wl) 
            while len(sr) < len(sl):
                sr.append(' ' * wr)
            s = s.rjust(ws + cl, '_').ljust(ws + cl + cr, '_')
            s = [s.rjust(ws + wl + cr).ljust(ws + wl + wr)]
            s = '\n'.join(s + [l + (' ' * ws) + r for (l,r) in zip(sl, sr)])
        return s
    
from enum import Enum
class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal:
    
    def __init__(self, tree, traversalType):
        self.tree = tree
        #self.leftS = tree.left
        #self.rightS = tree.right
        
        self.traversal = traversalType
        self.printlist= None
        self.index = 0
    
    def changeTraversalType(self,traversalType):
        self.traversal = traversalType
        #print(self.traversal.value)
    
    def __iter__(self):
        #create the tree traversal here
        if self.traversal.value == 1:
            self.printlist = self.tree.print_preorder()
        
        #in-order case
        elif self.traversal.value == 2:
            self.printlist = self.tree.print_inorder()
        
        else:
            self.printlist = self.tree.print_postorder()
        
        return self
    
    def __next__(self):
        try:
            tree = self.printlist[self.index]
            #tree = self.tree[self.index] 
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return tree