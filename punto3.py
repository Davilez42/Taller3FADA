from stackWithQueue.StackWithQueue import StackWithQueue

def ejemplo1():
    print('-------------------EJEMPLO 1-----------------------')
    pila1 = StackWithQueue(5)#se crea una pila de tamaño 5
    #insertar elementos
    pila1.pushPilaConColas(545)
    pila1.pushPilaConColas(234)
    pila1.pushPilaConColas(666)
    pila1.pushPilaConColas(42)
    pila1.pushPilaConColas(984)
    try:
        pila1.pushPilaConColas(4)#en caso de superar el tamaño asignado nos lanza una excepcion 
    except OverflowError :
        print(True)
            
    pila1.mostrarPilaConColas()
    pila1.popPilaConColas()#elimino un elemento    
    pila1.mostrarPilaConColas()

def ejemplo2():
    print('-------------------EJEMPLO 2-----------------------')
    pila2 =  StackWithQueue(4) 
    pila2.pushPilaConColas(2)
    pila2.pushPilaConColas(22)
    pila2.pushPilaConColas(52)
    pila2.pushPilaConColas(782)
    #elimino y muestro como queda la cola cada vez que se realiza la operacion popPilaConColas()
    pila2.mostrarPilaConColas()
    pila2.popPilaConColas()    
    pila2.mostrarPilaConColas()
    pila2.popPilaConColas()    
    pila2.mostrarPilaConColas()
    pila2.mostrarPilaConColas()
    pila2.popPilaConColas()    
    pila2.mostrarPilaConColas()
    pila2.popPilaConColas()
    pila2.mostrarPilaConColas()#muestra una pila vacia
    
    try:
        pila2.popPilaConColas()#si se intenta eliminar otra vez se lanza una excepcion 
    except Exception as e:
        print(type(e))    
    
    #elimino elementtos

def ejemplo3():
    print('-------------------EJEMPLO 3-----------------------')
    pila3 = StackWithQueue(5)#se crea una pila de tamaño 5
    print("Esta vacia? ",pila3.estaVaciaPilaConColas())
    #insertar elementos
    pila3.pushPilaConColas(545)
    pila3.pushPilaConColas(234)
    pila3.pushPilaConColas(666)
    
    print("Esta vacia? ",pila3.estaVaciaPilaConColas())#retorna true si la pila esta vacia de lo contrario false
   
    pila3.pushPilaConColas(42)
    pila3.pushPilaConColas(984)#lleno la pila complemtamente
    
    pila3.mostrarPilaConColas() 
    print()
    print("Esta vacia? ",pila3.estaVaciaPilaConColas())#retorna true si la pila esta vacia de lo contrario false
    print()
    #vacio la pila complemtamente
    print(984==pila3.popPilaConColas())
    print(42==pila3.popPilaConColas())
    print(666==pila3.popPilaConColas())
    print("Esta vacia? ",pila3.estaVaciaPilaConColas())#retorna true si la pila esta vacia de lo contrario false
    print(234==pila3.popPilaConColas())
    print(545==pila3.popPilaConColas())

    pila3.mostrarPilaConColas()#muestra la pila vacia

    print("Esta vacia? ",pila3.estaVaciaPilaConColas())#retorna true si la pila esta vacia de lo contrario false
    
    

ejemplo1()
ejemplo2()
ejemplo3()