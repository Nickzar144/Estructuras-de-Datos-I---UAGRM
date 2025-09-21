class SetModel:
    """Modelo para manejar conjuntos y operaciones básicas."""

    def __init__(self):
        self.sets = {}

    def create_set(self, name, elements):
        self.sets[name] = set(elements)

    def delete_set(self, name):
        if name in self.sets:
            del self.sets[name]

    def get_set(self, name):
        return self.sets.get(name, set())

    def list_sets(self):
        return list(self.sets.keys())

    def operate(self, op, s1, s2=None):
        A = self.get_set(s1)
        B = self.get_set(s2) if s2 else set()

        if op == "Unión":
            return A | B
        if op == "Intersección":
            return A & B
        if op == "Diferencia":
            return A - B
        if op == "Diferencia Simétrica":
            return A ^ B

        raise ValueError(f"Operación no soportada: {op}")
