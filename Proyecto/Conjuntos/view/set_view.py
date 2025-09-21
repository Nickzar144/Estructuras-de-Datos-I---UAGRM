import tkinter as tk
from tkinter import ttk


class SetView(tk.Tk):
    """Vista simplificada: una sola ventana para conjuntos y operaciones."""

    def __init__(self):
        super().__init__()
        self.title("Simulador de Conjuntos")
        self.geometry("650x450")

        # Lista de conjuntos
        frame_list = ttk.Frame(self)
        frame_list.pack(side="left", padx=10, pady=10)

        tk.Label(frame_list, text="Conjuntos disponibles").pack()
        self.set_listbox = tk.Listbox(frame_list, height=15, exportselection=False)
        self.set_listbox.pack()

        # Área de operaciones
        frame_ops = ttk.Frame(self)
        frame_ops.pack(side="left", fill="y", padx=10, pady=10)

        self.btn_create_set = ttk.Button(frame_ops, text="Crear conjunto")
        self.btn_create_set.pack(pady=5)

        self.btn_delete_set = ttk.Button(frame_ops, text="Eliminar conjunto")
        self.btn_delete_set.pack(pady=5)

        tk.Label(frame_ops, text="Conjunto 1").pack(pady=2)
        self.set1_listbox = tk.Listbox(frame_ops, height=5, exportselection=False)
        self.set1_listbox.pack(pady=2)

        tk.Label(frame_ops, text="Conjunto 2").pack(pady=2)
        self.set2_listbox = tk.Listbox(frame_ops, height=5, exportselection=False)
        self.set2_listbox.pack(pady=2)

        tk.Label(frame_ops, text="Operación").pack(pady=2)
        self.set_op_var = tk.StringVar()
        self.set_op_menu = ttk.Combobox(
            frame_ops,
            textvariable=self.set_op_var,
            values=["Unión", "Intersección", "Diferencia", "Diferencia Simétrica", "Complemento"],
            state="readonly",
        )
        self.set_op_menu.pack(pady=2)

        self.btn_operate_set = ttk.Button(frame_ops, text="Ejecutar operación")
        self.btn_operate_set.pack(pady=5)

        # Área de resultados
        self.txt_result = tk.Text(self, height=15)
        self.txt_result.pack(fill="both", padx=10, pady=10)

    # Métodos auxiliares
    def set_sets_list(self, sets):
        self.set_listbox.delete(0, tk.END)
        self.set1_listbox.delete(0, tk.END)
        self.set2_listbox.delete(0, tk.END)
        for s in sets:
            self.set_listbox.insert(tk.END, s)
            self.set1_listbox.insert(tk.END, s)
            self.set2_listbox.insert(tk.END, s)

    def append_result(self, text):
        self.txt_result.insert(tk.END, text + "\n")
        self.txt_result.see(tk.END)

    def get_selected_set1(self):
        sel = self.set1_listbox.curselection()
        return self.set1_listbox.get(sel[0]) if sel else ""

    def get_selected_set2(self):
        sel = self.set2_listbox.curselection()
        return self.set2_listbox.get(sel[0]) if sel else ""

    def get_selected_set_main(self):
        sel = self.set_listbox.curselection()
        return self.set_listbox.get(sel[0]) if sel else ""
