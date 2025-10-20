# metodos/uniforme_discreta.py
import tkinter as tk
from tkinter import messagebox, font
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Importar desde la raíz del proyecto para acceder a config.py
from config import COLOR_CUERPO_PRINCIPAL, COLOR_CONTROLES 

class UniformeDiscretaFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=COLOR_CUERPO_PRINCIPAL)
        self.values = []
        self.crear_paneles_pestaña()
        self.crear_control_uniforme()
        self.crear_resultados_uniforme()

    def crear_paneles_pestaña(self):
        # Panel de Control (Arriba)
        self.control_frame = tk.Frame(self, bg=COLOR_CONTROLES, height=130)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, expand=False, pady=5, padx=5)
        self.control_frame.pack_propagate(False)

        # Panel de Resultados (Abajo)
        self.result_frame = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.result_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=5, padx=5)

    def crear_control_uniforme(self):
        fuente2 = font.Font(family="Arial", size=10)
        
        lbl_min = tk.Label(self.control_frame, text="Mínimo (a):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_min.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        self.entry_min = tk.Entry(self.control_frame, width=12)
        self.entry_min.grid(row=0, column=1, padx=8, pady=8)
        self.entry_min.insert(0, "1")

        lbl_max = tk.Label(self.control_frame, text="Máximo (b):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_max.grid(row=0, column=2, padx=8, pady=8, sticky="e")
        self.entry_max = tk.Entry(self.control_frame, width=12)
        self.entry_max.grid(row=0, column=3, padx=8, pady=8)
        self.entry_max.insert(0, "10")

        lbl_n = tk.Label(self.control_frame, text="N (Muestras):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_n.grid(row=1, column=0, padx=8, pady=8, sticky="e")
        self.entry_n = tk.Entry(self.control_frame, width=12)
        self.entry_n.grid(row=1, column=1, padx=8, pady=8)
        self.entry_n.insert(0, "100")
        
        self.btn_generar = tk.Button(self.control_frame, text="Generar y Graficar", command=self.generar_y_graficar)
        self.btn_generar.grid(row=1, column=2, columnspan=2, padx=8, pady=8, sticky="we")

    def crear_resultados_uniforme(self):
        self.fig = Figure(figsize=(6,4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.ax.bar([], [])
        self.ax.set_title("Distribución de Variables Aleatorias")
        self.ax.set_xlabel("Valor")
        self.ax.set_ylabel("Frecuencia")
        self.fig.tight_layout()
        self.canvas.draw()


    def generar_y_graficar(self):
        try:
            minimo = int(self.entry_min.get())
            maximo = int(self.entry_max.get())
            n = int(self.entry_n.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores enteros válidos para Mínimo, Máximo y N.")
            return

        if n <= 0 or maximo < minimo:
            # Simplificación de validaciones
            messagebox.showerror("Error", "N debe ser > 0 y Máximo >= Mínimo.")
            return

        self.values = [random.randint(minimo, maximo) for _ in range(n)]
        self.graficar()
        messagebox.showinfo("Generación completa", f"Se generaron {n} valores aleatorios (Uniforme Discreta).")

    def graficar(self):
        if not self.values:
            return

        self.ax.clear()
        
        frecuencias = {}
        for val in self.values:
            frecuencias[val] = frecuencias.get(val, 0) + 1
            
        x_vals = sorted(frecuencias.keys())
        y_vals = [frecuencias[x] for x in x_vals]
        
        self.ax.bar(x_vals, y_vals, width=0.8, edgecolor='black')
        self.ax.set_xticks(x_vals)
        self.ax.set_title("Distribución Uniforme Discreta")
        self.ax.set_xlabel("Valor Discreto")
        self.ax.set_ylabel("Frecuencia")
        self.fig.tight_layout()
        self.canvas.draw()