import tkinter as tk
from tkinter import Menu
from formularios.frm_maestro import FormularioMaestro
from formularios.frm_discreta import FormularioDiscreta
from formularios.frm_continua import FormularioContinua

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Números Aleatorios")
        self.geometry("900x800")
        self.create_menu()
        # contenedor para montar los frames (no destruimos el menú)
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        self.show_maestro()

    def create_menu(self):
        menu_bar = Menu(self)
        # Menu for different forms
        form_menu = Menu(menu_bar, tearoff=0)
        form_menu.add_command(label="Generador de Números", command=self.show_maestro)
        form_menu.add_command(label="Distribuciones Aletorias", command=self.show_discreta)
        form_menu.add_command(label="Automata Celular", command=self.show_continua)
        menu_bar.add_cascade(label="Opciones", menu=form_menu)
        self.config(menu=menu_bar)

    def show_maestro(self):
        self.clear_window()
        self.form_maestro = FormularioMaestro(self.container)
        self.form_maestro.pack(fill=tk.BOTH, expand=True)

    def show_discreta(self):
        self.clear_window()
        self.form_discreta = FormularioDiscreta(self.container)
        self.form_discreta.pack(fill=tk.BOTH, expand=True)

    def show_continua(self):
        self.clear_window()
        self.form_continua = FormularioContinua(self.container)
        self.form_continua.pack(fill=tk.BOTH, expand=True)

    def clear_window(self):
        for widget in self.container.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()