def centrar_ventana(ventana, ancho, alto):
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")