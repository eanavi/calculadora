import tkinter as tk
import importlib.util
import subprocess
import sys
from pathlib import Path
from tkinter import messagebox


def start_automata(dimx:int=100, dimy:int = 70, cellsize: int = 9):
    """
    Lanza el script juego_de_la_vida.py en un proceso separado usando el mismo
    intérprete (sys.executable). No redirigimos stdout/stderr para que las
    impresiones aparezcan en la consola principal.
    """
    try:
        juego_path = Path(__file__).resolve().parents[1] / 'juego_de_la_vida.py'
        if not juego_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {juego_path}")
        cmd = [sys.executable, str(juego_path), str(dimx), str(dimy), str(cellsize)]
        # abrir en proceso independiente; hereda la consola (las impresiones se verán)
        subprocess.Popen(cmd, cwd=str(juego_path.parent))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar el autómata:\n{e}")
        raise


class UniformeContinuaFrame(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.configure(bg="#ffffff")
        self._build()
    
    def _build(self):
        lbl = tk.Label(self, text="Automata Celular", font=("Arial", 11, "bold"))
        lbl.pack(pady=8)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=6)

        self.btn_start = tk.Button(btn_frame, text="Iniciar Automata", command=self._on_start)
        self.btn_start.pack(side=tk.LEFT, padx=4)

        self.info = tk.Label(self, text="Al pulsar se lanzara el automata en una nueva ventana", wraplength=300)
        self.info.pack(padx=8, pady=6)

    def _on_start(self):
        try:
            start_automata(100, 70, 9)
        except Exception as e:
            messagebox.showerror("Error", f"NO se pudo iniciar el automata: {e}")

