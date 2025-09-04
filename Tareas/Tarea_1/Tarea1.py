class NumeroEntero:
    """
    Clase para representar y operar con un número entero.
    """

    def __init__(self, valor: int) -> None:
        """
        Inicializa un número entero.

        Args:
            valor (int): Valor entero inicial.
        """
        self._valor = None  # atributo privado (convención con "_")
        self.valor = valor  # usamos el setter para validar

    @property
    def valor(self) -> int:
        """
        Getter del valor entero.
        
        Returns:
            int: El valor actual.
        """
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor: int) -> None:
        """
        Setter del valor entero (con validación).

        Args:
            nuevo_valor (int): El nuevo valor a asignar.

        Raises:
            ValueError: Si el nuevo valor no es un entero.
        """
        if not isinstance(nuevo_valor, int):
            raise ValueError("El valor debe ser un número entero.")
        self._valor = nuevo_valor

    def es_par(self) -> bool:
        """Verifica si el número es par."""
        return self.valor % 2 == 0

    def es_primo(self) -> bool:
        """Verifica si el número es primo."""
        if self.valor <= 1:
            return False
        for i in range(2, int(self.valor ** 0.5) + 1):
            if self.valor % i == 0:
                return False
        return True

    def sumar(self, otro: int) -> int:
        """Suma otro número al valor actual."""
        return self.valor + otro

    def __str__(self) -> str:
        """Representación en cadena del número entero."""
        return f"NumeroEntero({self.valor})"