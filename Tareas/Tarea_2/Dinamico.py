class ConjuntoDinamico:
    """
    Implementación de un Conjunto usando estructura dinámica (lista).
    """

    def __init__(self) -> None:
        self._elementos = []

    @property
    def tamanio(self) -> int:
        return len(self._elementos)

    def insertar(self, elemento: int) -> None:
        if elemento not in self._elementos:
            self._elementos.append(elemento)

    def eliminar(self, elemento: int) -> None:
        if elemento in self._elementos:
            self._elementos.remove(elemento)

    def pertenece(self, elemento: int) -> bool:
        return elemento in self._elementos

    def __str__(self) -> str:
        return f"ConjuntoDinamico: {self._elementos}"
    
# Conjunto Dinámico
c2 = ConjuntoDinamico()
c2.insertar(5)
c2.insertar(15)
c2.insertar(5)   # no se repite
print(c2)
c2.eliminar(15)
print("Después de eliminar:", c2)