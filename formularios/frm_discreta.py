# distribucion_discreta.py

import tkinter as tk
from tkinter import ttk, font
from config import COLOR_CUERPO_PRINCIPAL, COLOR_BARRA_SUPERIOR

# Importar las clases de distribución desde la carpeta/paquete 'metodos'
from .metodos.kerlang import KErlangFrame
from .metodos.uniforme_discreta import UniformeDiscretaFrame
from .metodos.exponencial import ExponencialFrame  # <-- NUEVA IMPORTACIÓN
from .metodos.gamma import GammaFrame
from .metodos.normal import NormalFrame
from .metodos.weibull import WeibullFrame
from .metodos.uniforme_continua import UniformeContinuaFrame # <-- NUEVA IMPORTACIÓN
from .metodos.bernoulli import BernoulliFrame                 # <-- NUEVA IMPORTACIÓN
from .metodos.binomial import BinomialFrame                   # <-- NUEVA IMPORTACIÓN
from .metodos.poisson import PoissonFrame

class FormularioDiscreta(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLOR_CUERPO_PRINCIPAL)
        self.paneles()
        self.crear_notebook()
        
    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=40)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)
        fuente = font.Font(family="Arial", size=12, weight="bold")
        titulo = tk.Label(self.barra_superior, text="Generación de Distribuciones Discretas", bg=COLOR_BARRA_SUPERIOR, fg="white", font=fuente)
        titulo.pack(pady=6)

    def crear_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 1. Uniforme (DISCRETA)
        self.uniforme_discreta_frame = UniformeDiscretaFrame(self.notebook)
        self.notebook.add(self.uniforme_discreta_frame, text="Uniforme Discreta")
        
        # 2. Bernoulli (DISCRETA)
        self.bernoulli_frame = BernoulliFrame(self.notebook)
        self.notebook.add(self.bernoulli_frame, text="Bernoulli")        # <-- NUEVA PESTAÑA

        # 3. Binomial (DISCRETA)
        self.binomial_frame = BinomialFrame(self.notebook)
        self.notebook.add(self.binomial_frame, text="Binomial")          # <-- NUEVA PESTAÑA

        # 4. Poisson (DISCRETA)
        self.poisson_frame = PoissonFrame(self.notebook)
        self.notebook.add(self.poisson_frame, text="Poisson")            # <-- NUEVA PESTAÑA
        
        # 5. Uniforme (CONTINUA)
        self.uniforme_continua_frame = UniformeContinuaFrame(self.notebook)
        self.notebook.add(self.uniforme_continua_frame, text="Uniforme Continua") # <-- NUEVA PESTAÑA
        
        # 6. Exponencial
        self.exponencial_frame = ExponencialFrame(self.notebook)
        self.notebook.add(self.exponencial_frame, text="Exponencial")
        
        # 7. K-Erlang
        self.kerlang_frame = KErlangFrame(self.notebook)
        self.notebook.add(self.kerlang_frame, text="K-Erlang")
        
        # 8. Gamma
        self.gamma_frame = GammaFrame(self.notebook)
        self.notebook.add(self.gamma_frame, text="Gamma")
        
        # 9. Normal
        self.normal_frame = NormalFrame(self.notebook)
        self.notebook.add(self.normal_frame, text="Normal")

        # 10. Weibull
        self.weibull_frame = WeibullFrame(self.notebook)
        self.notebook.add(self.weibull_frame, text="Weibull")