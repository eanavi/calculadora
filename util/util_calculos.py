# util/util_calculos.py
import math

def prueba_media(resultados):
    if not resultados:
        return "No hay datos para la prueba."

    numeros = [float(fila[3]) for fila in resultados]
    n = len(numeros)
    media_obtenida = sum(numeros)/n
    media_esperada = 0.5
    sigma = 1 / math.sqrt(12*n)
    Z = (media_obtenida - media_esperada)/sigma

    aceptacion = "ACEPTADA" if abs(Z) < 1.96 else "RECHAZADA"

    informe = (
        f"Prueba de la Media\n"
        f"-------------------\n"
        f"Números generados: {n}\n"
        f"Media obtenida: {media_obtenida:.4f}\n"
        f"Media esperada: {media_esperada}\n"
        f"Desviación estándar: {sigma:.4f}\n"
        f"Z calculado: {Z:.4f}\n"
        f"Resultado: {aceptacion}"
    )
    return informe

def metodo_potencia(semilla, n):
    resultados = []
    x = semilla
    for i in range(n):
        operacion = str(x ** 2).zfill(8)
        mid = len(operacion) // 2
        x = int(operacion[mid-2:mid+2])
        num = x / 10000
        resultados.append((i+1, operacion, x, f"{num:.4f}"))
    return resultados



def metodo_producto( semilla1, semilla2, n):
    resultados = []
    x1, x2 = semilla1, semilla2
    for i in range(n):
        operacion = str(x1 * x2).zfill(8)
        mid = len(operacion) // 2
        x1 = int(operacion[mid-2:mid+2])
        num = x1 / 10000
        resultados.append((i+1, operacion, x1, f"{num:.4f}"))
        x2 = x1  # actualizo semilla2
    return resultados

def metodo_constante(semilla, constante, n):
    resultados = []
    x = semilla
    for i in range(n):
        operacion = str(x * constante).zfill(8)
        mid = len(operacion) // 2
        x = int(operacion[mid-2:mid+2])
        num = x / 10000
        resultados.append((i+1, operacion, x, f"{num:.4f}"))
    return resultados