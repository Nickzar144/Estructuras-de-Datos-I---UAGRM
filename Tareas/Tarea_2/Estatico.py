class ConjuntoEstatico:
    """
    Implementación de un Conjunto usando estructura estática (array con tamaño fijo).
    """

    def __init__(self, capacidad: int) -> None:
        self._capacidad = capacidad
        self._elementos = [None] * capacidad
        self._tamanio = 0

    @property
    def tamanio(self) -> int:
        return self._tamanio

    def insertar(self, elemento: int) -> None:
        if self._tamanio < self._capacidad and elemento not in self._elementos:
            self._elementos[self._tamanio] = elemento
            self._tamanio += 1

    def eliminar(self, elemento: int) -> None:
        if elemento in self._elementos:
            idx = self._elementos.index(elemento)
            self._elementos[idx] = None

    def pertenece(self, elemento: int) -> bool:
        return elemento in self._elementos

    def __str__(self) -> str:
        return f"ConjuntoEstatico: {[e for e in self._elementos if e is not None]}"
    
# Conjunto Estático
c1 = ConjuntoEstatico(5)
c1.insertar(10)
c1.insertar(20)
c1.insertar(10)  # no se repite
print(c1)
print("Pertenece 20:", c1.pertenece(20))
