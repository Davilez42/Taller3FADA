from linkedListInvent.LinkedListInvent import LinkedListInvent
from linkedListInvent.ValueReplicaError import ValueReplicaError
""" 
Estudiantes
- Oscar Fernando Rivera Pardo - 2067730 
- Jeferson Aguiar Dominguez Diaz - 2067607 
- Alvaro Andres Hurtado Vallecilla - 1958463
- Jose David Suarez Cardona -2067548 """

def ejemplo1():#Ejemeplo de agregar obras 
    print('-------------------EJEMPLO 1-----------------------')
    inventario_museo  = LinkedListInvent()   
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Persistencia de la memoria")
    inventario_museo.agregarReplica("El hombre de Vitrubio")
    inventario_museo.agregarReplica("El hombre de Vitrubio") 
       
    print(inventario_museo.listarReplicas())

def ejemplo2():#Ejemplo de vender obras
    print('-------------------EJEMPLO 2-----------------------')
    inventario_museo  = LinkedListInvent()    
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Persistencia de la memoria")
    inventario_museo.agregarReplica("El hombre de Vitrubio")
    inventario_museo.agregarReplica("El hombre de Vitrubio")  
    inventario_museo.agregarReplica("El hombre de Vitrubio")     
    inventario_museo.venderReplica("El hombre de Vitrubio")#se vende una replica de "El hombre de Vitrubio" por lo tanto solo hay 2 
    
    print(inventario_museo.listarReplicas())   

def ejemplo3():
    print('-------------------EJEMPLO 3-----------------------')
    inventario_museo  = LinkedListInvent()  
    inventario_museo.agregarReplica("Monalisa")
    inventario_museo.agregarReplica("Monalisa")
    inventario_museo.agregarReplica("Monalisa")
    inventario_museo.agregarReplica("La ultima cena")
    inventario_museo.agregarReplica("la batalla final")

    inventario_museo.venderReplica("Monalisa")
    inventario_museo.venderReplica("Monalisa")
    inventario_museo.venderReplica("Monalisa")
    #Al venderse las 3 replicas de la monalisa se elimina el nodo
    print(inventario_museo.listarReplicas())
    try:
        inventario_museo.venderReplica("Monalisa") #no existe la obra 'Monalisa' por que anteriormente fue vendida en su totalidad 
    except ValueReplicaError as e:
        print(e)
        


def ejemplo4():
    print('-------------------EJEMPLO 4-----------------------')
    inventario_museo  = LinkedListInvent()   
    inventario_museo.agregarReplica("Monalisa")
    inventario_museo.agregarReplica("Monalisa")
    inventario_museo.agregarReplica("Monalisa")
    inventario_museo.agregarReplica("La ultima cena")
    
    try:
        inventario_museo.venderReplica("La espada de bolivar")#no existe esta replica    
    except ValueReplicaError as e:
        print(e)
        
    print(inventario_museo.listarReplicas())

def ejemplo5():
    print('-------------------EJEMPLO 5-----------------------')
    inventario_museo  = LinkedListInvent()    
    inventario_museo.agregarReplica("La orca")
    inventario_museo.agregarReplica("La santa")
    inventario_museo.agregarReplica("La ultima cena")   
    inventario_museo.venderReplica("La orca")
    inventario_museo.venderReplica("La ultima cena")
    inventario_museo.venderReplica("La santa")
    
    print(inventario_museo.listarReplicas())#inventario vacio
    
ejemplo1()
ejemplo2()
ejemplo3()
ejemplo4()
ejemplo5() 