import pygame
import numpy as np
import sys
import time

# --- Constantes de Color ---
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

# --- Variables de Simulación ---
# La simulación es de 1D, pero se dibuja en 2D. 
# 'cur_row' almacenará el estado de la fila actual (la última fila calculada).
# 'current_row_index' rastrea qué fila de la matriz global estamos llenando.
cur_row = None
current_row_index = 0

def iniciar(dimx, dimy):
    """
    Inicializa la matriz 2D que almacenará todo el historial de la simulación 1D.
    Establece el patrón inicial: un '1' en el centro de la primera fila.
    """
    global cur_row, current_row_index
    
    # Creamos una matriz para almacenar el historial de filas
    cells = np.zeros((dimy, dimx), dtype=int)
    
    # Establecer la condición inicial: un '1' en el centro de la primera fila
    initial_row = np.zeros(dimx, dtype=int)
    center_pos = dimx // 2
    initial_row[center_pos] = 1
    
    # La primera fila es la condición inicial
    cells[0, :] = initial_row
    
    # Inicializar el estado de la fila actual para el cálculo
    cur_row = initial_row
    current_row_index = 1
    
    return cells

def actualizar_fila(prev_row):
    """
    Calcula la siguiente fila usando la regla XOR:
    celda[i] = prev_row[i-1] XOR prev_row[i+1]
    Se utiliza el módulo (wrap around) para manejar los bordes.
    """
    dimx = prev_row.shape[0]
    next_row = np.zeros(dimx, dtype=int)

    for c in range(dimx):
        # Índice de la celda izquierda (usa módulo para el wrap-around)
        left = prev_row[(c - 1) % dimx]
        # Índice de la celda derecha (usa módulo para el wrap-around)
        right = prev_row[(c + 1) % dimx]

        centro = prev_row[(c) % dimx]
        
        # Regla: Siguiente estado = (Izquierda XOR Derecha)
        # En Python, el operador XOR es ^
        next_row[c] =  left ^ (right or centro)
        
    return next_row

def dibujar_celda(surface, row_index, col_index, value, sz):
    """Dibuja una sola celda en la superficie de Pygame."""
    col = col_alive if value == 1 else col_background
    pygame.draw.rect(surface, col, (col_index * sz, row_index * sz, sz - 1, sz - 1))

def dibujar_historial(surface, cells, sz):
    """Dibuja todo el historial de la matriz."""
    surface.fill(col_background) # Llenamos el fondo antes de dibujar
    
    dimy, dimx = cells.shape
    for r in range(dimy):
        for c in range(dimx):
            if cells[r, c] == 1:
                col = col_alive
            else:
                col = col_background
            
            # Dibujamos las celdas
            pygame.draw.rect(surface, col, (c * sz, r * sz, sz - 1, sz - 1))


def ejecutar_simulacion(dimx, dimy, cellsize):
    """Función principal para inicializar y ejecutar la simulación."""
    global cur_row, current_row_index
    
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Autómata Celular 1D (Regla XOR)")
    surface.fill(col_background)

    # 1. Inicializar la matriz y la primera fila
    cells = iniciar(dimx, dimy)
    dibujar_historial(surface, cells, cellsize)
    pygame.display.update()
    
    running = True
    speed_factor = 0.05 # Retardo entre filas para animación
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # 2. Bucle principal de la simulación
        if current_row_index < dimy:
            
            # a. Calcular la siguiente fila
            next_row = actualizar_fila(cur_row)
            
            # b. Almacenar la nueva fila en el historial
            cells[current_row_index, :] = next_row
            
            # c. Dibujar solo la fila recién calculada
            for c in range(dimx):
                dibujar_celda(surface, current_row_index, c, next_row[c], cellsize)
            
            # d. Actualizar variables de estado
            cur_row = next_row
            current_row_index += 1
            
            pygame.display.update()
            time.sleep(speed_factor) # Control de velocidad
            
        elif current_row_index == dimy:
            # La simulación ha terminado de llenar la pantalla
            time.sleep(0.5)
            # En este punto, puedes esperar indefinidamente a que el usuario cierre
            # o reiniciar la simulación si lo deseas.
            # current_row_index += 1 # Opcional: para que no entre a este bloque de nuevo
            
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    try:
        # Usamos dimensiones más adecuadas para ver el patrón
        dimx = int(sys.argv[1]) if len(sys.argv) > 1 else 129 # Dimensión impar para el centro
        dimy = int(sys.argv[2]) if len(sys.argv) > 2 else 90
        cellsize = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    except Exception:
        dimx, dimy, cellsize = 129, 90, 8

    print(f"[Simulador AC1D] Arrancando con ancho={dimx}, alto={dimy}, tamaño celda={cellsize}", flush=True)
    ejecutar_simulacion(dimx, dimy, cellsize)