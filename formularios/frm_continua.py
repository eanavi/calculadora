import tkinter as tk
from tkinter import ttk, messagebox, font
from config import COLOR_CUERPO_PRINCIPAL, COLOR_CONTROLES, COLOR_BARRA_SUPERIOR

class FormularioContinua(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLOR_CUERPO_PRINCIPAL)
        self.paneles()
        self.crear_widgets()

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=20)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        altura_panel = 130
        self.barra_controles = tk.Frame(self, bg=COLOR_CONTROLES, height=altura_panel)
        self.barra_controles.pack(side=tk.TOP, fill=tk.X)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def crear_widgets(self):
        fuente = font.Font(family="Arial", size=12, weight="bold")
        fuente2 = font.Font(family="Arial", size=10)

        etiqueta_titulo = tk.Label(self.barra_superior, text="Opciones de Distribución Continua", bg=COLOR_BARRA_SUPERIOR, fg="white", font=fuente)
        etiqueta_titulo.pack(pady=10)

        # Aquí se pueden agregar más controles para la distribución continua
        self.boton_calcular = tk.Button(self.barra_controles, text="Calcular Distribución", command=self.calcular)
        self.boton_calcular.pack(pady=5)

        self.resultados_texto = tk.Text(self, state=tk.DISABLED)
        self.resultados_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def calcular(self):
        # Lógica para calcular la distribución continua (implementar)
        resultados = "Resultados de la distribución continua"
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, resultados):
        self.resultados_texto.config(state=tk.NORMAL)
        self.resultados_texto.delete("1.0", tk.END)
        self.resultados_texto.insert(tk.END, resultados)
        self.resultados_texto.config(state=tk.DISABLED)