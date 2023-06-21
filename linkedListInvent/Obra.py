class Obra:
    def __init__(self,nombre,cantida) -> None:
        self.nombre = nombre
        self.cantidad = cantida
        
        
    def __format__(self):
        return f'Nombre: {self.nombre}\nCantidad:{self.cantidad} \n '