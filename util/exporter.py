import openpyxl
from openpyxl.styles import Font

def export_to_excel(datos, filename="numeros_aleatorios.xlsx"):
    """
    Exporta los datos a un archivo Excel.
    :param datos: lista de tuplas (iteración, operacion, semilla_central, numero)
    :param filename: nombre del archivo de salida
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Resultados"

    # Encabezados
    headers = ["Iteración", "Valor Completo", "Semilla Central", "Número [0,1)"]
    ws.append(headers)

    # Aplicar estilo a encabezados
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Agregar datos
    for fila in datos:
        ws.append(fila)

    wb.save(filename)
    return filename
