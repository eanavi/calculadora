import tkinter as tk
from pathlib import Path
import sys
import subprocess
from tkinter import ttk, messagebox, font
from config import COLOR_CUERPO_PRINCIPAL, COLOR_CONTROLES, COLOR_BARRA_SUPERIOR

def start_automata(dimx:int=100, dimy:int = 70, cellsize: int = 9):
    try:
        juego_path = Path(__file__).resolve().parents[1] / 'formularios/juego_de_la_vida.py'
        if not juego_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {juego_path}")

        cmd = [sys.executable, str(juego_path), str(dimx), str(dimy), str(cellsize)]
        # capturar salida para depuración
        proc = subprocess.Popen(cmd, cwd=str(juego_path.parent),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # esperar brevemente para detectar fallo inmediato
        try:
            outs, errs = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            # proceso sigue vivo -> OK (no bloquear)
            return

        # si terminó rápido, mostrar salida/errores para depuración
        if proc.returncode != 0:
            msg = f"Proceso finalizó con código {proc.returncode}\n\nSTDOUT:\n{outs}\n\nSTDERR:\n{errs}"
            messagebox.showerror("Error al iniciar autómata", msg)
        else:
            # mostrar salida informativa (opcional)
            if outs.strip() or errs.strip():
                print("[autómata output]", outs)
                if errs.strip():
                    print("[autómata error]", errs)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar el autómata:\n{e}")
        raise

def iniciar_triangulo(dimx:int=100, dimy:int = 70, cellsize: int = 9):
    try:
        juego_path = Path(__file__).resolve().parents[1] / 'formularios/triangulo.py'
        if not juego_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {juego_path}")

        cmd = [sys.executable, str(juego_path), str(dimx), str(dimy), str(cellsize)]
        # capturar salida para depuración
        proc = subprocess.Popen(cmd, cwd=str(juego_path.parent),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # esperar brevemente para detectar fallo inmediato
        try:
            outs, errs = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            # proceso sigue vivo -> OK (no bloquear)
            return

        # si terminó rápido, mostrar salida/errores para depuración
        if proc.returncode != 0:
            msg = f"Proceso finalizó con código {proc.returncode}\n\nSTDOUT:\n{outs}\n\nSTDERR:\n{errs}"
            messagebox.showerror("Error al iniciar autómata", msg)
        else:
            # mostrar salida informativa (opcional)
            if outs.strip() or errs.strip():
                print("[autómata output]", outs)
                if errs.strip():
                    print("[autómata error]", errs)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar el autómata:\n{e}")
        raise

def iniciar_triada(dimx:int=100, dimy:int = 70, cellsize: int = 9):
    try:
        juego_path = Path(__file__).resolve().parents[1] / 'formularios/triada.py'
        if not juego_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {juego_path}")

        cmd = [sys.executable, str(juego_path), str(dimx), str(dimy), str(cellsize)]
        # capturar salida para depuración
        proc = subprocess.Popen(cmd, cwd=str(juego_path.parent),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # esperar brevemente para detectar fallo inmediato
        try:
            outs, errs = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            # proceso sigue vivo -> OK (no bloquear)
            return

        # si terminó rápido, mostrar salida/errores para depuración
        if proc.returncode != 0:
            msg = f"Proceso finalizó con código {proc.returncode}\n\nSTDOUT:\n{outs}\n\nSTDERR:\n{errs}"
            messagebox.showerror("Error al iniciar autómata", msg)
        else:
            # mostrar salida informativa (opcional)
            if outs.strip() or errs.strip():
                print("[autómata output]", outs)
                if errs.strip():
                    print("[autómata error]", errs)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar el autómata:\n{e}")
        raise

class FormularioContinua(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLOR_CUERPO_PRINCIPAL)
        try:
            self.paneles()
            self.crear_widgets()
        except Exception as e:
            import traceback
            print("Error al iniciar el formulario", e)
            traceback.print_exc()
            messagebox.showerror("Error", f"fallo")

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

        etiqueta_titulo = tk.Label(self.barra_superior, text="Automata Celular", bg=COLOR_BARRA_SUPERIOR, fg="white", font=fuente)
        etiqueta_titulo.pack(pady=10)

        # Aquí se pueden agregar más controles para la distribución continua
        self.boton_iniciar = tk.Button(self.barra_controles, text="Iniciar Automata El juego de la Vida", command=self._on_start)
        self.boton_iniciar.pack(side=tk.LEFT, padx=4)

        self.boton_iniciar_tri = tk.Button(self.barra_controles, text="Iniciar Triangulo", command=self._iniciar_tri)
        self.boton_iniciar_tri.pack(side=tk.RIGHT, padx=4)

        self.boton_iniciar_triada = tk.Button(self.barra_controles, text="Iniciar Triada", command=self._iniciar_triada)
        self.boton_iniciar_triada.pack(side = tk.BOTTOM, padx=4)

        self.informacion = tk.Label(self.cuerpo_principal, text="Al pulsar se lanzara el automata", wraplength=400, justify='left', bg=COLOR_CUERPO_PRINCIPAL)
        self.informacion.pack(anchor="nw", padx=8, pady=6)

    def _on_start(self):
        try:
            start_automata(100, 70, 9)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el automata: {e}")

    def _iniciar_tri(self):
        try:
            iniciar_triangulo(100, 70, 9)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el automata del triangulo {e}")

    def _iniciar_triada(self):
        try:
            iniciar_triada(100, 70, 9)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el automata del triangulo {e}")