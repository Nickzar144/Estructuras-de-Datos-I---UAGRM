import os

class ConjuntoDisco:
    """
    Implementación de un Conjunto guardado en disco.
    """

    def __init__(self, archivo: str = "conjunto.txt") -> None:
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()

    def _leer(self) -> list:
        with open(self.archivo, "r") as f:
            return list(map(int, f.read().split())) if f.read().strip() else []

    def _escribir(self, elementos: list) -> None:
        with open(self.archivo, "w") as f:
            f.write(" ".join(map(str, elementos)))

    def insertar(self, elemento: int) -> None:
        elementos = self._leer()
        if elemento not in elementos:
            elementos.append(elemento)
            self._escribir(elementos)

    def eliminar(self, elemento: int) -> None:
        elementos = self._leer()
        if elemento in elementos:
            elementos.remove(elemento)
            self._escribir(elementos)

    def pertenece(self, elemento: int) -> bool:
        return elemento in self._leer()

    def __str__(self) -> str:
        return f"ConjuntoDisco: {self._leer()}"

# Conjunto en Disco
c3 = ConjuntoDisco("conjunto.txt")
c3.insertar(100)
c3.insertar(200)
print(c3)
print("Pertenece 100:", c3.pertenece(100))
c3.eliminar(100)
print("Después de eliminar:", c3)