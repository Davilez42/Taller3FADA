from queue_.Queue import Queue
class StackWithQueue:
    def __init__(self,size) -> None:
        self.stack =  Queue(size)
        self.size = size

    def estaVaciaPilaConColas(self)-> bool:
        return self.stack.size()==0
    
    def pushPilaConColas(self,element):
        self.stack.enqueue(element)
  
    def popPilaConColas(self):
        cola_aux = Queue(self.size)#se crea una cola del tamaño de la cola actual
        i=0
        while i <self.stack.size()-1:
            cola_aux.enqueue(self.stack.dequeue())
        element = self.stack.dequeue()
        self.stack = cola_aux
        return element    
    
    def mostrarPilaConColas(self):
        print(self.stack.queue)