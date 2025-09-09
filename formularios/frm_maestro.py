import os
import sys
import tkinter as tk
from tkinter import ttk, font, messagebox
import matplotlib.pyplot as plt
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_CONTROLES
from util.util_calculos import metodo_potencia, metodo_producto, metodo_constante, prueba_media
from util.exporter import export_to_excel
import util.util_ventana as uv


class FormularioMaestro(tk.Tk):


    def __init__(self):
        super().__init__()
        self.algoritmo = tk.IntVar(self, value=1)
        self.title("Calculadora de Numeros Aleatorios")
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.tabla_resultados()
        self.resultados = []
        

    def config_window(self):
        w, h = 600, 800
        uv.centrar_ventana(self, w, h)

    def paneles(self):
        # Barra superior pequeña
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=20)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        # Barra de controles
        altura_panel = 130  # altura fija para controles e informe
        self.barra_controles = tk.Frame(self, bg=COLOR_CONTROLES, height=altura_panel)
        self.barra_controles.pack(side=tk.TOP, fill=tk.X)

        # Cuerpo principal: ocupa espacio restante
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Panel de informe con la misma altura que barra de controles
        self.panel_informe = tk.Frame(self, bg=COLOR_CONTROLES, height=altura_panel)
        self.panel_informe.pack(side=tk.BOTTOM, fill=tk.X)

        # Text widget para mostrar informe
        self.texto_informe = tk.Text(self.panel_informe, state=tk.DISABLED)
        self.texto_informe.pack(fill=tk.BOTH, expand=True)
    
    def graficar(self):
        if not self.resultados:
            messagebox.showwarning("Aviso", "No hay datos para graficar. Genere primero los números.")
            return

        # Extraer iteración y número [0,1)
        iteraciones = [fila[0] for fila in self.resultados]
        numeros = [float(fila[3]) for fila in self.resultados]

        # Crear dispersograma
        plt.figure("Dispersograma de Números Pseudoaleatorios")
        plt.scatter(iteraciones, numeros, color='blue')
        plt.title("Dispersograma de Números Pseudoaleatorios")
        plt.xlabel("Iteración")
        plt.ylabel("Número [0,1)")
        plt.grid(True)
        plt.show()


    def generar(self):
        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        try:
            semilla1 = int(self.semilla1.get())
            semilla2 = int(self.semilla2.get())
            constante = int(self.constante.get())
            n = int(self.n.get())
            alg = int(self.algoritmo.get())

            # Validaciones de longitud
            if len(str(semilla1)) <= 3:
                raise ValueError("La semilla 1 debe tener más de 3 dígitos")
            if alg == 2 and len(str(semilla2)) <= 3:
                raise ValueError("La semilla 2 debe tener más de 3 dígitos")
            if alg == 3 and len(str(constante)) <= 3:
                raise ValueError("La constante debe tener más de 3 dígitos")

        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))
            return

        

        if alg == 1:
            resultados = metodo_potencia(semilla1, n)
        elif alg == 2:
            resultados = metodo_producto(semilla1, semilla2, n)
        elif alg == 3:
            resultados = metodo_constante(semilla1, constante, n)
        else:
            resultados = []

        self.resultados = resultados


        if resultados:
            self.boton_exportar.config(state=tk.NORMAL)
            self.boton_graficar.config(state=tk.NORMAL)

        for fila in resultados:
            self.tabla.insert("", "end", values=fila)

        informe = prueba_media(resultados)
        self.texto_informe.config(state=tk.NORMAL)
        self.texto_informe.delete("1.0", tk.END)
        self.texto_informe.insert(tk.END, informe)
        self.texto_informe.config(state=tk.DISABLED)

    def controles_barra_superior(self):
        fuente = font.Font(family="Arial", size=12, weight="bold")
        fuente2 = font.Font(family="Arial", size=10)
        etiqueta_titulo = tk.Label(self.barra_superior, text="Calculadora de " \
        "Numeros Aleatorios", bg=COLOR_BARRA_SUPERIOR, 
        fg="white", font=fuente)
        etiqueta_titulo.pack(pady=10)

        semilla1_titulo = tk.Label(self.barra_controles, text="Semilla 1:",
        bg=COLOR_CONTROLES, fg="white", font=fuente2)
        semilla1_titulo.grid(row=0, column=0, padx=10, pady=5)

        semilla2_titulo = tk.Label(self.barra_controles, text="Semilla 2:",
        bg=COLOR_CONTROLES, fg="white", font=fuente2)
        semilla2_titulo.grid(row=0, column=1, padx=10, pady=5)

        constante_titulo = tk.Label(self.barra_controles, text="Constante:",
        bg=COLOR_CONTROLES, fg="white", font=fuente2)
        constante_titulo.grid(row=0, column=2, padx=10, pady=5)

        algoritmo_titulo = tk.Label(self.barra_controles, text="Algoritmo:",
        bg=COLOR_CONTROLES, fg="white", font=fuente2)
        algoritmo_titulo.grid(row=0, column=3, padx=10, pady=5)

        n_titulo = tk.Label(self.barra_controles, text="N:",
        bg=COLOR_CONTROLES, fg="white", font=fuente2)
        n_titulo.grid(row=0, column=4, padx=10, pady=5)

        self.semilla1 = tk.Entry(self.barra_controles, width=10)
        self.semilla1.grid(row=1, column=0, padx=10, pady=5)
        self.semilla1.insert(0, "1234")

        self.semilla2 = tk.Entry(self.barra_controles, width=10)
        self.semilla2.grid(row=1, column=1, padx=10, pady=5)
        self.semilla2.insert(0, "5678")

        self.constante = tk.Entry(self.barra_controles, width=10)
        self.constante.grid(row=1, column=2, padx=10, pady=5)
        self.constante.insert(0, "91011")

        self.algoritmo = tk.StringVar()

        Rbtn1 = tk.Radiobutton(self.barra_controles, width=8, text="Potencia 2", variable=self.algoritmo, value=1)
        Rbtn1.grid(row=1, column=3, padx=5, pady=1)
        
        Rbtn2 = tk.Radiobutton(self.barra_controles, width=8, text="Producto", variable=self.algoritmo, value=2)
        Rbtn2.grid(row=2, column=3, padx=5, pady=1)

        Rbtn3 = tk.Radiobutton(self.barra_controles, width=8, text="Constante", variable=self.algoritmo, value=3)
        Rbtn3.grid(row=3, column=3, padx=5, pady=1)

        self.n = tk.Entry(self.barra_controles, width=10)
        self.n.grid(row=1, column=4, padx=10, pady=5)
        self.n.insert(0, "100")

        boton_generar = tk.Button(self.barra_controles, font=fuente, command=self.generar, text="Generar")
        boton_generar.grid(row=1, column=5, padx=10, pady=5)

        self.boton_exportar = tk.Button(self.barra_controles, font=fuente, command=self.exportar, text="Exportar", state=tk.DISABLED)
        self.boton_exportar.grid(row=2, column=5, padx=10, pady=5)

        self.boton_graficar = tk.Button(self.barra_controles, font=fuente, command=self.graficar, text="Graficar", state=tk.DISABLED)
        self.boton_graficar.grid(row=3, column=5, padx=10, pady=5)

    def exportar(self):
        if not self.resultados:
            messagebox.showwarning("Aviso", "No hay datos para exportar. Genere primero los números.")
            return

        try:
            filename = export_to_excel(self.resultados)
            try:
                if sys.platform.startswith('win'):
                    os.startfile(filename)
                elif sys.platform.startswith('darwin'):
                    os.system(f'open "{filename}"')
                else:
                    os.system(f'xdg-open "{filename}"')
            except Exception as e:
                print(f"No se pudo abrir el archivo automáticamente: {e}")
            messagebox.showinfo("Exportación exitosa", f"Los resultados se exportaron a:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error al exportar", str(e))

    def tabla_resultados(self):
        columnas = ("iteracion", "operacion", "semilla_central", "numero")
        self.tabla = ttk.Treeview(self.cuerpo_principal, columns=columnas, show="headings", height=20)
        
        self.tabla.heading("iteracion", text="Iteración")
        self.tabla.heading("operacion", text="Valor Completo")
        self.tabla.heading("semilla_central", text="Semilla Central")
        self.tabla.heading("numero", text="Número [0,1)")

        self.tabla.column("iteracion", anchor=tk.CENTER, width=80)
        self.tabla.column("operacion", anchor=tk.CENTER, width=150)
        self.tabla.column("semilla_central", anchor=tk.CENTER, width=120)
        self.tabla.column("numero", anchor=tk.CENTER, width=120)

        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)




