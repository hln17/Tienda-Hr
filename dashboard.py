import tkinter as tk

def ventana_categorias(descripcion):
    ventana = tk.Tk()
    ventana.title("Panel de Categorías")
    ventana.geometry("1000x600")
    ventana.configure(bg="#ffffff")

    # Panel izquierdo: Registro de producto
    marco_registro = tk.Frame(ventana, bg="#f0f0f0", padx=20, pady=20, bd=2, relief="ridge", width=300)
    marco_registro.pack(side="left", fill="y")

    titulo = tk.Label(marco_registro, text="Registrar Producto", font=("Segoe UI", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=(0, 10))

    campos = ["ID", "Nombre", "Descripción", "Cantidad", "Precio"]
    entradas = {}

    for campo in campos:
        lbl = tk.Label(marco_registro, text=f"{campo}:", bg="#f0f0f0", anchor="w")
        lbl.pack(fill="x")
        entry = tk.Entry(marco_registro)
        entry.pack(fill="x", pady=(0, 10))
        entradas[campo] = entry

    btn_guardar = tk.Button(marco_registro, text="Guardar producto", bg="#4CAF50", fg="white")
    btn_guardar.pack(pady=10)

    # Panel derecho: Muestra de la descripción
    marco_derecho = tk.Frame(ventana, bg="#ffffff", padx=20, pady=20)
    marco_derecho.pack(side="right", fill="both", expand=True)

    etiqueta_info = tk.Label(
        marco_derecho,
        text=descripcion,
        font=("Segoe UI", 14),
        bg="#ffffff",
        fg="#333333",
        wraplength=500,
        justify="left"
    )
    etiqueta_info.pack(anchor="nw")  # Anclar arriba a la izquierda
    
    ventana.mainloop()



