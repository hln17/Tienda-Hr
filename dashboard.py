import tkinter as tk

def ventana_categorias(descripcion):
    ventana = tk.Tk()
    ventana.title("Categoría")
    ventana.geometry("600x300")
    ventana.configure(bg="#fefefe")  # fondo suave

    # Marco elegante para la descripción
    marco = tk.Frame(ventana, bg="#ffffff", padx=20, pady=20, bd=2, relief="groove")
    marco.pack(expand=True, pady=50)

    etiqueta = tk.Label(
        marco,
        text=descripcion,
        font=("Segoe UI", 14),
        bg="#ffffff",
        fg="#333333",
        wraplength=500,
        justify="center"
    )
    etiqueta.pack()

    ventana.mainloop()


