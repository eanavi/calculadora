def metodo_potencia(semilla, n):
    resultados = []
    for i in range(n):
        semilla = (semilla ** 2) % 10000  # Ejemplo de método de potencia
        resultados.append((i + 1, "Potencia", semilla, semilla / 10000))
    return resultados

def metodo_producto(semilla1, semilla2, n):
    resultados = []
    for i in range(n):
        semilla1 = (semilla1 * semilla2) % 10000  # Ejemplo de método de producto
        resultados.append((i + 1, "Producto", semilla1, semilla1 / 10000))
    return resultados

def metodo_constante(semilla, constante, n):
    resultados = []
    for i in range(n):
        semilla = (semilla + constante) % 10000  # Ejemplo de método de constante
        resultados.append((i + 1, "Constante", semilla, semilla / 10000))
    return resultados

def prueba_media(resultados):
    media = sum(fila[3] for fila in resultados) / len(resultados) if resultados else 0
    return f"Media de los números generados: {media:.4f}"