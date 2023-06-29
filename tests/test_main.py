
from linkedList.LinkedList import LinkedList
from linkedListInvent.LinkedListInvent import LinkedListInvent
from linkedListInvent.ValueReplicaError import ValueReplicaError
from stackWithQueue.StackWithQueue import StackWithQueue
from queue_.Queue import Queue
from punto1 import combinarListas


def test_linkedList():
    #insertando
    oblinkelist1 = LinkedList()
    oblinkelist1.insert(34)
    oblinkelist1.insert(53)
    oblinkelist1.insert(43)
    oblinkelist1.insert(6)
    oblinkelist1.insert(2)
    
    assert oblinkelist1.get(0) == 34
    assert oblinkelist1.get(1) == 53
    assert oblinkelist1.get(2) == 43
    assert oblinkelist1.get(3) == 6
    assert oblinkelist1.get(4) == 2
    
    try:    
        oblinkelist1.get(5)
        assert False
    except IndexError:
        assert True
    except :
        assert False    
    
    #eliminando 
    oblinkelist1.delete(34)
    oblinkelist1.delete(2)
    oblinkelist1.delete(53)
    
    assert oblinkelist1.get(0) == 43
    assert oblinkelist1.get(1) == 6

    try:    
        oblinkelist1.delete(23)
        assert False
    except ValueError:
        assert True
    except :
        assert False 
    
    oblinkelist1.insert_index(0,100)
    assert oblinkelist1.get(0) == 100
    assert oblinkelist1.get(1) == 43
    assert oblinkelist1.get(2) == 6

def test_punto1():
    ##PRUEBA1
    lista1  = LinkedList()
    lista1.insert(3)
    lista1.insert(7) 
    lista1.insert(9)  
    
    lista2  = LinkedList()
    lista2.insert(1)
    lista2.insert(3) 
    lista2.insert(8)      
    result = combinarListas(lista2,lista1)#/listas enlazada esperada / 1 3 3 7 8 9     
    rest = []
    for i in range(result.size()):
       rest.append(result.get(i))   
    assert rest == [1,3,3,7,8,9]   
    ##PRUEBA2
    lista3  = LinkedList()
    lista3.insert(3)
    lista3.insert(3) 
    lista3.insert(6)
    lista3.insert(8)
    lista3.insert(9)
    lista3.insert(20) 
         
    lista4  = LinkedList()
    lista4.insert(2)
    lista4.insert(40) 
    lista4.insert(41)
    lista4.insert(60)
    lista4.insert(100) 
    result2 = combinarListas(lista3,lista4)#lista enlazada esperada /2 3 3 6 8 9 20 40 41 60 100
    rest2 = []
    for i in range(result2.size()):
       rest2.append(result2.get(i))   
     
    assert rest2 == [2,3,3,6,8,9,20,40,41,60,100]  
    #PRUEBA3
    lista5 = LinkedList()
    lista5.insert(1)
    lista5.insert(4) 
    lista5.insert(6)
    lista5.insert(10)
    lista5.insert(22) 
         
    lista6  = LinkedList()
    lista6.insert(1)
    lista6.insert(1) 
    lista6.insert(5)
    lista6.insert(6)
    lista6.insert(7)    
    rest3 = []    
    result3 = combinarListas(lista5,lista6)#lista enlazada esperada /1 1 1 4 5 6 6 7 10 22
    for i in range(result3.size()):
        rest3.append(result3.get(i))   
    assert rest3 == [1,1,1,4,5,6,6,7,10,22]
    
def test_LinkedListInvent():
    ob1 = LinkedListInvent()
    ob1.agregarReplica("Monalisa")
    ob1.agregarReplica("La ultima cena")
    ob1.agregarReplica("La Virgen de las rocas")    
    
    try:
        ob1.venderReplica("Alegoria") 
    except ValueReplicaError as e:
        print(e)
    
    ob1.venderReplica("Monalisa") 
    
def test_Queue():
    cola = Queue(4)
    
    cola.enqueue(1)    
    cola.enqueue(12)
    cola.enqueue(21)
    cola.enqueue(13)
    try:
        cola.enqueue(21)
    except OverflowError:
        assert True
        
    assert cola.dequeue()==1
    assert cola.dequeue()==12
    assert cola.dequeue()==21
    assert cola.dequeue()==13
   
    try:
        cola.dequeue()
        assert False
    except IndexError:
        assert True
        
    cola.enqueue(54)
    cola.enqueue(13)
    cola.enqueue(43)
    cola.enqueue(2)
    assert cola.dequeue()==54
    assert cola.dequeue()==13  
    cola.enqueue(90)
    cola.enqueue(756)      
    assert cola.dequeue()==43
    assert cola.dequeue()==2
    assert cola.dequeue()==90
    assert cola.dequeue()==756    
            
def test_StackWithQueue():
    stack1 = StackWithQueue(5)
    assert stack1.estaVaciaPilaConColas()
    stack1.pushPilaConColas(4)
    stack1.pushPilaConColas(6)
    stack1.pushPilaConColas(10)
    stack1.pushPilaConColas(66)
    stack1.pushPilaConColas(26)
   
    assert not stack1.estaVaciaPilaConColas()
    try:
        stack1.pushPilaConColas(100)
        assert False
    except OverflowError:
        assert True
    except:
        assert False
        
    assert stack1.popPilaConColas()==26
    assert stack1.popPilaConColas()==66
    assert stack1.popPilaConColas()==10
    assert stack1.popPilaConColas()==6
    assert stack1.popPilaConColas()==4
    
    try:
        stack1.popPilaConColas()
        assert False
    except IndexError:
        assert True
    except:
        assert False   
    assert stack1.estaVaciaPilaConColas()