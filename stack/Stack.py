from array import array
class Stack:
    def __init__(self,size) -> None:
        self.stack = [None]*size
        self.size = size
        self.top = 0
        
    def push(self,element):
        if  self.top == self.size:       
            raise IndexError
        self.stack[self.top]=element 
        self.top +=1
        
    def stackempty(self)-> bool:
        return self.top == 0 
    
    def get(self,index):
        if index < self.size:  
            return self.stack[index]
        else:
            raise IndexError
    
    def pop(self):
        if self.top == 0:
            raise IndexError
        
        value =  self.stack[self.top-1]
        self.stack[self.top-1] = None
        self.top -=1         
        return value        
    
