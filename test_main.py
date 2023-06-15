from linkedList.LinkedList import LinkedList
from stack.Stack import Stack
from punto1 import combinarListas
import numpy

def test_getindex():
    lista1 = LinkedList()
    lista1.insert(123)#0
    lista1.insert(23)#1
    lista1.insert(34)#2
    lista1.insert(54)#3
    lista1.insert(73)#4
    
    assert 123 == lista1.get(0)
    assert 23 == lista1.get(1)
    assert 73 == lista1.get(4)
    assert 54 == lista1.get(3)         
    try:
        lista1.get(9)
        assert False
    except IndexError:
        assert True
    except:
        assert False   
    
def test_deleteValue():
    lista1 = LinkedList()
    lista1.insert(123)#0
    lista1.insert(23)#1
    lista1.insert(34)#2
    lista1.insert(54)#3
    lista1.insert(73)#4
    
    lista1.delete(123)
    lista1.delete(73)
    
    assert 23 == lista1.get(0)
    assert 54 == lista1.get(2)
    assert 34 == lista1.get(1)
    
    try:
        lista1.get(3)
        assert False
    except IndexError:
        assert True
    except:
        assert False 
    
    lista1.delete(34)
    assert 23 == lista1.get(0)
    assert 54 == lista1.get(1)
    
    try:
        lista1.get(2)
        assert False
    except IndexError:
        assert True
    except:
        assert False 

def test_size():
    lista1 = LinkedList()
    assert 0 == lista1.size()
    lista1.insert(123)#0
    assert 1 == lista1.size()
    lista1.insert(23)#1
    lista1.insert(34)#2
    lista1.insert(54)#3
    lista1.insert(73)#4
    assert 5 == lista1.size()
    
def test_combinarListas1():
    lista1 = LinkedList()
    lista1.insert(1)
    lista1.insert(3)
    lista1.insert(3)
    lista1.insert(4)
    lista1.insert(6)
    lista1.insert(7)
      
    lista2 = LinkedList()
    lista2.insert(3)
    lista2.insert(8)
    lista2.insert(9) 
    lista2.insert(20)           
    l3 = combinarListas(lista1,lista2)
    assert 1== l3.get(0)
    assert 3== l3.get(1)
    assert 3== l3.get(2)
    assert 3== l3.get(3)
    assert 4== l3.get(4)
    assert 6== l3.get(5)
    assert 7== l3.get(6)
    assert 8== l3.get(7)
    assert 9== l3.get(8)
    assert 20== l3.get(9) 

    
    """ try:
        l3.get(6)
        assert False
    except IndexError:
        assert True
    except:
        assert False """
    
def test_insertindex(): 
    
    lista1 = LinkedList()
    lista1.insert(123)#0
    lista1.insert(23)#1
    lista1.insert(34)#2

    assert 123 == lista1.get(0)
    assert 23 == lista1.get(1)
    assert 34 == lista1.get(2)
    
    lista1.insert_index(0,19)
    lista1.insert_index(1,13)
    
    assert 19 == lista1.get(0)
    assert 13 == lista1.get(1)
    assert 123 == lista1.get(2)
    assert 23 == lista1.get(3)
    assert 23 == lista1.get(3)
    
def test_combinarLista2():
    lista1  = LinkedList()
    lista1.insert(3)
    lista1.insert(7) 
    lista1.insert(9)  
    lista2  = LinkedList()
    lista2.insert(1)
    lista2.insert(3) 
    lista2.insert(8)      
    result = combinarListas(lista2,lista1)
      
    assert 1 == result.get(0)
    assert 3 == result.get(1)
    assert 3 == result.get(2)
    assert 7 == result.get(3)
    assert 8 == result.get(4)
    assert 9 == result.get(5) 
        
def test_combinarLista3():
    lista1  = LinkedList()
    lista1.insert(3)
    lista1.insert(20)
    lista1.insert(40) 
    lista1.insert(100)  
    
    lista2  = LinkedList()
    lista2.insert(1)
    lista2.insert(3) 
    lista2.insert(8)
    lista2.insert(29)  
    
    result  = combinarListas(lista2,lista1)
    
    assert 1 == result.get(0)
    assert 3 == result.get(1)
    assert 3 == result.get(2)
    assert 8 == result.get(3)
    assert 20 == result.get(4)
    assert 29 == result.get(5)
    assert 40 == result.get(6)
    assert 100 == result.get(7)                
      
    try:
        result.get(8)
        assert False
    except IndexError:
        assert True
    except :
        assert False   
        
def test_superCallejero():
    valores1 = numpy.sort(numpy.random.randint(10000,size =1000))
    valores2 = numpy.sort(numpy.random.randint(10000,size =2000))
    lista1 = LinkedList()
    lista2 = LinkedList()
    
    r = []   
    for i in valores1:
        lista1.insert(i)
        r.append(i)
        
    for i in valores2:
        lista2.insert(i)
        r.append(i)
    r.sort()  
    h = [] 
    result = combinarListas(lista1,lista2)
    
    for i in range(0,result.size()):
        h.append(result.get(i))
        
    assert r == h    
    
def test_stack():
    pila1 = Stack(5)
    pila1.push(1)
    pila1.push(2)
    pila1.push(3)
    pila1.push(4)
    pila1.push(4)
    
 
    assert 4 == pila1.pop()
    assert 4 == pila1.pop()
    assert 3 == pila1.pop()
    assert 2 == pila1.pop()
    assert 1 == pila1.pop()

    
    pila1.push(1)
    pila1.push(2)
    pila1.push(3)
    pila1.push(4)
    pila1.push(4)

    



    
    
    
    
        
    
        
        