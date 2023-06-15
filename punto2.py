from linkedListInvent.LinkedListInvent import LinkedListInvent



def ejemplo1():#Ejemeplo de agregar obras 
    print('-------------------EJEMPLO 1-----------------------')
    inventario_museo  = LinkedListInvent()
    
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Persistencia de la memoria")
    inventario_museo.agregarReplica("El hombre de Vitrubio")
    inventario_museo.agregarReplica("El hombre de Vitrubio") 
       
    inventario_museo.listarReplicas()

def ejemplo2():#Ejemplo de vender obras
    print('-------------------EJEMPLO 2-----------------------')
    inventario_museo  = LinkedListInvent()
    
    inventario_museo.agregarReplica("Giaconda")
    inventario_museo.agregarReplica("Persistencia de la memoria")
    inventario_museo.agregarReplica("El hombre de Vitrubio")
    inventario_museo.agregarReplica("El hombre de Vitrubio")  
    inventario_museo.agregarReplica("El hombre de Vitrubio") 
     
    inventario_museo.venderReplica("El hombre de Vitrubio")#se vende una replica de "El hombre de Vitrubio" por lo tanto solo hay 2 
    
    inventario_museo.listarReplicas()   


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
    inventario_museo.listarReplicas()


ejemplo1()
ejemplo2()
ejemplo3()