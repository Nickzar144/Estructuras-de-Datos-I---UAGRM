class RelationModel:
    """Modelo para manejar relaciones binarias y sus operaciones."""

    def __init__(self, universe=None):
        self.relations = {}
        self.universe = universe if universe else set()

    def create_relation(self, name, pairs):
        self.relations[name] = set(pairs)

    def delete_relation(self, name):
        if name in self.relations:
            del self.relations[name]

    def get_relation(self, name):
        return self.relations.get(name, set())

    def list_relations(self):
        return list(self.relations.keys())

    def operate(self, op, r1, r2=None):
        A = self.get_relation(r1)
        B = self.get_relation(r2) if r2 else set()

        if op == "Unión":
            return A | B
        if op == "Intersección":
            return A & B
        if op == "Diferencia":
            return A - B
        if op == "Diferencia Simétrica":
            return A ^ B
        if op == "Complemento":
            U = {(a, b) for a in self.universe for b in self.universe}
            return U - A

        raise ValueError(f"Operación no soportada: {op}")
