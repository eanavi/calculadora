# metodos/binomial.py

import tkinter as tk
from tkinter import messagebox, font
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import COLOR_CUERPO_PRINCIPAL, COLOR_CONTROLES 

class BinomialFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=COLOR_CUERPO_PRINCIPAL)
        self.values = []
        self.crear_paneles_pestaña()
        self.crear_control_binomial()
        self.crear_resultados_binomial()

    def crear_paneles_pestaña(self):
        self.control_frame = tk.Frame(self, bg=COLOR_CONTROLES, height=130)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, expand=False, pady=5, padx=5)
        self.control_frame.pack_propagate(False)

        self.result_frame = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.result_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=5, padx=5)

    def crear_control_binomial(self):
        fuente2 = font.Font(family="Arial", size=10)
        
        # Ensayos (n)
        lbl_ensayos = tk.Label(self.control_frame, text="Ensayos (n):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_ensayos.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        self.entry_ensayos = tk.Entry(self.control_frame, width=12)
        self.entry_ensayos.grid(row=0, column=1, padx=8, pady=8)
        self.entry_ensayos.insert(0, "10")

        # Probabilidad (p)
        lbl_p = tk.Label(self.control_frame, text="Prob. de Éxito (p):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_p.grid(row=0, column=2, padx=8, pady=8, sticky="e")
        self.entry_p = tk.Entry(self.control_frame, width=12)
        self.entry_p.grid(row=0, column=3, padx=8, pady=8)
        self.entry_p.insert(0, "0.5")

        # N
        lbl_n = tk.Label(self.control_frame, text="N (Muestras):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_n.grid(row=1, column=0, padx=8, pady=8, sticky="e")
        self.entry_n_muestras = tk.Entry(self.control_frame, width=12)
        self.entry_n_muestras.grid(row=1, column=1, padx=8, pady=8)
        self.entry_n_muestras.insert(0, "100")
        
        # Botón Generar
        self.btn_generar = tk.Button(self.control_frame, text="Generar y Graficar", command=self.generar_y_graficar)
        self.btn_generar.grid(row=1, column=2, columnspan=2, padx=8, pady=8, sticky="we")

    def crear_resultados_binomial(self):
        self.fig = Figure(figsize=(6,4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.ax.set_title("Distribución Binomial")
        self.ax.set_xlabel("Número de Éxitos")
        self.ax.set_ylabel("Frecuencia")
        self.fig.tight_layout()
        self.canvas.draw()


    def generar_y_graficar(self):
        try:
            ensayos = int(self.entry_ensayos.get())
            p = float(self.entry_p.get())
            n_muestras = int(self.entry_n_muestras.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            return

        if n_muestras <= 0 or ensayos <= 0 or not (0 <= p <= 1):
            messagebox.showerror("Error", "N de muestras y ensayos deben ser > 0, y p debe estar entre 0 y 1.")
            return

        self.values = []
        for _ in range(n_muestras):
            # Generación Binomial: suma de 'ensayos' de Bernoullis(p)
            exitos = 0
            for _ in range(ensayos):
                if random.random() < p:
                    exitos += 1
            self.values.append(exitos)

        self.graficar()
        messagebox.showinfo("Generación completa", f"Se generaron {n_muestras} valores aleatorios (Binomial).")

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
        self.ax.set_title(f"Distribución Binomial (n={self.entry_ensayos.get()}, p={self.entry_p.get()})")
        self.ax.set_xlabel("Número de Éxitos")
        self.ax.set_ylabel("Frecuencia")
        self.fig.tight_layout()
        self.canvas.draw()