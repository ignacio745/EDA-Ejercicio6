import numpy as np

class ColaSecuencial:
    __dimension:int = None
    __primero:int = None
    __ultimo:int = None
    __tipo:type = None
    __cantidad:int = None
    __arreglo:np.ndarray = None

    def __init__(self, dimension:int=20, tipo:type=int) -> None:
        self.__dimension = dimension
        self.__primero = 0
        self.__ultimo = 0
        self.__tipo = tipo
        self.__cantidad = 0
        self.__arreglo = np.empty(dimension, dtype=tipo)
    
    def insertar(self, elemento) -> None:
        assert isinstance(elemento, self.__tipo), "Solo puede insertar elementos del tipo {0}, no {1}".format(self.__tipo, type(elemento))
        if self.__cantidad < self.__dimension:
            self.__arreglo[self.__ultimo] = elemento
            self.__ultimo = (self.__ultimo+1) % self.__dimension
            self.__cantidad += 1
        else:
            raise OverflowError("Limite de cola alcanzado")
    
    def suprimir(self):
        if self.__cantidad <= 0:
            raise Exception("No hay elementos para suprimir")
        else:
            elemento = self.__arreglo[self.__primero]
            self.__primero = (self.__primero+1) % self.__dimension
            self.__cantidad -= 1
            return elemento