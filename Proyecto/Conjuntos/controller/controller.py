from tkinter import simpledialog, messagebox


class Controller:
    """Controlador simplificado para la nueva vista."""

    def __init__(self, model, rel_model, view):
        self.model = model
        self.rel_model = rel_model
        self.view = view
        self._bind_events()
        self._refresh_lists()

    def _bind_events(self):
        self.view.btn_create_set.config(command=self.create_set)
        self.view.btn_delete_set.config(command=self.delete_set)
        self.view.btn_operate_set.config(command=self.operate_set)

    def _refresh_lists(self):
        self.view.set_sets_list(self.model.list_sets())

    def create_set(self):
        name = simpledialog.askstring("Crear conjunto", "Nombre del conjunto:")
        if not name:
            return
        raw = simpledialog.askstring("Elementos", "Ingrese elementos separados por comas:")
        if raw is None:
            return
        elements = [e.strip() for e in raw.split(",") if e.strip()]
        self.model.create_set(name, elements)
        self._refresh_lists()
        self.view.append_result(f"Conjunto {name}: {sorted(self.model.get_set(name))}")

    def delete_set(self):
        s = self.view.get_selected_set_main()
        if not s:
            messagebox.showinfo("Info", "Seleccione un conjunto")
            return
        self.model.delete_set(s)
        self._refresh_lists()
        self.view.append_result(f"Conjunto {s} eliminado")

    def operate_set(self):
        op = self.view.set_op_var.get()
        s1 = self.view.get_selected_set1()
        s2 = self.view.get_selected_set2() if op != "Complemento" else None
        if not s1 or (op != "Complemento" and not s2) or not op:
            return
        result = self.model.operate(op, s1, s2)
        self.view.append_result(f"{op} de {s1}" + (f" y {s2}" if s2 else "") + f": {sorted(result)}")
