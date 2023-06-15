class Obra:
    def __init__(self,nombre,cantida) -> None:
        self.nombre = nombre
        self.cantidad = cantida
        
        
    def __format__(self):
        return f'Nombre: {self.nombre} \n Cantidad:{self.cantidad} \n '