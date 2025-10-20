# metodos/kerlang.py

import tkinter as tk
from tkinter import messagebox, font
import random
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import COLOR_CUERPO_PRINCIPAL, COLOR_CONTROLES 

class KErlangFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=COLOR_CUERPO_PRINCIPAL)
        self.values = []
        self.crear_paneles_pestaña()
        self.crear_control_kerlang()
        self.crear_resultados_kerlang()
        
    def crear_paneles_pestaña(self):
        self.control_frame = tk.Frame(self, bg=COLOR_CONTROLES, height=130)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, expand=False, pady=5, padx=5)
        self.control_frame.pack_propagate(False)

        self.result_frame = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.result_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=5, padx=5)

    def crear_control_kerlang(self):
        fuente2 = font.Font(family="Arial", size=10)
        
        lbl_k = tk.Label(self.control_frame, text="Parámetro k (fase):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_k.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        self.entry_k = tk.Entry(self.control_frame, width=12)
        self.entry_k.grid(row=0, column=1, padx=8, pady=8)
        self.entry_k.insert(0, "2")
        
        lbl_lambda = tk.Label(self.control_frame, text="Tasa (λ):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_lambda.grid(row=0, column=2, padx=8, pady=8, sticky="e")
        self.entry_lambda = tk.Entry(self.control_frame, width=12)
        self.entry_lambda.grid(row=0, column=3, padx=8, pady=8)
        self.entry_lambda.insert(0, "1.0")

        lbl_n = tk.Label(self.control_frame, text="N (Muestras):", bg=COLOR_CONTROLES, fg="white", font=fuente2)
        lbl_n.grid(row=1, column=0, padx=8, pady=8, sticky="e")
        self.entry_n = tk.Entry(self.control_frame, width=12)
        self.entry_n.grid(row=1, column=1, padx=8, pady=8)
        self.entry_n.insert(0, "100")
        
        self.btn_generar = tk.Button(self.control_frame, text="Generar y Graficar", command=self.generar_y_graficar)
        self.btn_generar.grid(row=1, column=2, columnspan=2, padx=8, pady=8, sticky="we")

    def crear_resultados_kerlang(self):
        self.fig = Figure(figsize=(6,4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.ax.bar([], [])
        self.ax.set_title("Distribución K-Erlang (Discreta por truncamiento)")
        self.ax.set_xlabel("Valor (Truncado)")
        self.ax.set_ylabel("Frecuencia")
        self.fig.tight_layout()
        self.canvas.draw()


    def generar_y_graficar(self):
        try:
            k = int(self.entry_k.get())
            lamda = float(self.entry_lambda.get())
            n = int(self.entry_n.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            return

        if n <= 0 or k <= 0 or lamda <= 0:
            messagebox.showerror("Error", "N, k y Tasa (λ) deben ser mayores que 0.")
            return

        self.values = []
        for _ in range(n):
            producto_r = 1.0
            for _ in range(k):
                r = random.random()
                while r == 0:
                    r = random.random()
                producto_r *= r
                
            x_erlang_continuo = - (1.0 / lamda) * math.log(producto_r)
            val = math.floor(x_erlang_continuo)
            self.values.append(val)

        self.graficar()
        messagebox.showinfo("Generación completa", f"Se generaron {n} valores aleatorios (K-Erlang).")

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
        self.ax.set_title(f"Distribución K-Erlang (k={self.entry_k.get()})")
        self.ax.set_xlabel("Valor Discreto (Truncado)")
        self.ax.set_ylabel("Frecuencia")
        self.fig.tight_layout()
        self.canvas.draw()