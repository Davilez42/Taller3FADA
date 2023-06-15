from linkedList.Node import Node
from copy import deepcopy
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size_ = 0 
             
    def insert(self,n):        
        if self.head == None:
            self.head = Node(n,None)
        else:  
            h = self.head
            while h.next is not None:
               h = h.next           
            h.next = Node(n,None)    
        self.size_+=1    
                                
    def get(self,index)->int:
        if self.head == None:
            raise IndexError
        i = 0
        h = self.head
        while i<index and h is not None:
            h = h.next
            i+=1    
        if h is None:
            raise IndexError
        else:
            return h.value   
        
    def delete(self,value):
        if self.head == None:
            raise IndexError     
        h = self.head
        ant = None
        next = h.next
        
        while h is not None and h.value!=value:
            ant = h
            h = h.next
            next = h.next
                 
        if h is None:
            raise IndexError

        if ant is None :
            self.head = next
            self.size_-=1
            return
        
        if next is None:
            ant.next = None  
         
        if next is not None and ant is not None:
            ant.next = next  
        self.size_-=1                    
        
    def size(self)->int:
        return self.size_ 
    
    def insert_index(self,index,element):
        if self.head == None and index==0:
            self.head = Node(element,None)
        elif self.head == None and index!=0:
            raise IndexError    
        else:
            h = self.head
            ant = None
            i=0
            while i<index and h is not None:
               ant = h
               h = h.next 
               i+=1                  
            if h is None:
                raise IndexError
            if ant is None:
                self.head = Node(element,h)
            else:
                ant.next=  Node(element,h)    
        self.size_+=1    
        
    def copy(self):
        return deepcopy(self)     