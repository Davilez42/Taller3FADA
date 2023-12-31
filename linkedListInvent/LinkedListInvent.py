
from linkedList.Node import Node
from linkedListInvent.Obra import Obra
from linkedListInvent.ValueReplicaError import ValueReplicaError
class LinkedListInvent:
    def __init__(self) -> None:
        self.head = None
        self.size_ = 0
        
    def agregarReplica(self,nombre:str):
        if self.head == None:
            self.head = Node(Obra(nombre,1),None)             
        else:  
            h = self.head
            ant = None
            while h is not None:    
                ant = h
                obra =  h.value
                if  obra.nombre == nombre:
                    obra.cantidad = obra.cantidad + 1
                    return                                
                h = h.next                          
            ant.next = Node(Obra(nombre,1),None)    
        self.size_+=1  
           
    def venderReplica(self,nombre:str):
        if self.head == None:
            raise IndexError
        else:
            h = self.head
            ant = None
            while h is not None and h.value.nombre !=nombre:                    
                ant = h 
                h=h.next     
            if h is None:
                raise ValueReplicaError(f'La obra "{nombre}" no existe en el Inventario \n')
                print(f'La obra "{nombre}" no existe en el Inventario \n')
                return
                
                     
            h.value.cantidad -= 1 
            if h.value.cantidad == 0: #si la cantidad llega a cero se desconecta el nodo
           
                if ant is None:
                    self.head = h.next
                    return     
                ant.next = h.next
        
    def listarReplicas(self):        
        h  =self.head
        if h==None:
            return 'Inventario vacio'
        obras = ""     
        while h is not None:
           obra = h.value
           obras += obra.__format__() + '\n\n'
           h = h.next  
        return obras   
           
           
           
           
