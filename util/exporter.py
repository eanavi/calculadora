def export_to_excel(data, filename="resultados.xlsx"):
    import pandas as pd

    df = pd.DataFrame(data, columns=["Iteración", "Operación", "Semilla Central", "Número"])
    df.to_excel(filename, index=False)

    return filename