
from linkedList.LinkedList import LinkedList

""" 
Estudiantes
- Oscar Fernando Rivera Pardo - 2067730 
- Jeferson Aguiar Dominguez Diaz - 2067607 
- Alvaro Andres Hurtado Vallecilla - 1958463
- Jose David Suarez Cardona -2067548 """


def combinarListas(l1:LinkedList,l2:LinkedList)->LinkedList:
    """ este algoritmo conciste en recorrer las 2 listas enlazadas al mismo tiempo y
    guardar en una tercera lista el numero menor del primer elemento de cada una de ellas
    aprovechando que se encuentran ordenadas ascendemente cada una, una vez ya decidido que numero 
    se ingresa a la lista se utilizan indices para controlar el acceso al siguiente elemento a comparar  """
    result =  LinkedList()
    l=0
    z=0
    while l1.size()!=l and l2.size()!=z:
        if l1.get(l)<l2.get(z):
            result.insert(l1.get(l))
            l+=1
        else:
            result.insert(l2.get(z))
            z+=1          
    """
    Por ultimo se verifica si alguna de las dos listas no quedo vacia y
    termina de insertar los elementos restantes en la lista resultado
    """
    
    if l1.size()!=l:
        for i in range(l,l1.size()):
            result.insert(l1.get(i))
            
    if l2.size()!=z:
        for i in range(z,l2.size()):
            result.insert(l2.get(i)) 
    return result
  

#Ejemplos
def ejemplo1():
    lista1  = LinkedList()
    lista1.insert(3)
    lista1.insert(7) 
    lista1.insert(9)  
    lista2  = LinkedList()
    lista2.insert(1)
    lista2.insert(3) 
    lista2.insert(8)      
    result = combinarListas(lista2,lista1)#/listas enlazada esperada / 1 3 3 7 8 9
    
    for i in range(result.size()):
        print(result.get(i),end=" ")#recorro la lsita enlazada para saber si esta ordenada
    print()    

def ejemplo2():
    lista1  = LinkedList()
    lista1.insert(3)
    lista1.insert(3) 
    lista1.insert(6)
    lista1.insert(8)
    lista1.insert(9)
    lista1.insert(20) 
         
    lista2  = LinkedList()
    lista2.insert(2)
    lista2.insert(40) 
    lista2.insert(41)
    lista2.insert(60)
    lista2.insert(100)    
          
    result = combinarListas(lista1,lista2)#lista enlazada esperada /2 3 3 6 8 9 20 40 41 60 100
    for i in range(result.size()):
        print(result.get(i),end=" ") 
    print()

def ejemplo3():
    lista1  = LinkedList()
    lista1.insert(1)
    lista1.insert(4) 
    lista1.insert(6)
    lista1.insert(10)
    lista1.insert(22) 
         
    lista2  = LinkedList()
    lista2.insert(1)
    lista2.insert(1) 
    lista2.insert(5)
    lista2.insert(6)
    lista2.insert(7)    
          
    result = combinarListas(lista1,lista2)#lista enlazada esperada /1 1 1 4 5 6 6 7 10 22
    for i in range(result.size()):
        print(result.get(i),end=" ") 
    print()

ejemplo1()
ejemplo2()
ejemplo3()
  
  
  
  
  
  
  
  
  
       
       
