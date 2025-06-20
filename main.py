import tkinter as tk
from views.login_view import cargar_login
from views.formulario import FormularioProducto
from views.productos_view import cargar_productos

def main():
    ventana = tk.Tk()
    ventana.geometry("1200x700")
    ventana.title("Mi Tienda")
    ventana.configure(bg="#f0f0f0")

    frames = {}
    catalogo_frame = None
    contenedor_derecha = None

    def refrescar_productos():
        nonlocal catalogo_frame
        if catalogo_frame:
            catalogo_frame.destroy()
        catalogo_frame = cargar_productos(contenedor_derecha)
        catalogo_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def on_login_success(usuario):
        nonlocal catalogo_frame, contenedor_derecha
        
        # Ocultar login
        frames['login'].pack_forget()
        
        # Crear contenedor principal
        contenedor_principal = tk.Frame(ventana)
        contenedor_principal.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Panel izquierdo (formulario)
        contenedor_izquierda = tk.Frame(contenedor_principal, width=300)
        contenedor_izquierda.pack(side="left", fill="y", padx=(0, 10))
        
        # Panel derecho (catálogo)
        contenedor_derecha = tk.Frame(contenedor_principal)
        contenedor_derecha.pack(side="right", fill="both", expand=True)
        
        # Crear formulario con callback para refrescar productos
        frames['formulario'] = FormularioProducto(
            contenedor_izquierda, 
            refrescar_callback=refrescar_productos
        )
        frames['formulario'].pack(fill="y", expand=True)
        
        # Cargar productos iniciales
        refrescar_productos()

    # Cargar vista de login
    frames['login'] = cargar_login(ventana, on_login_success)
    frames['login'].pack(fill="both", expand=True)

    ventana.mainloop()

if __name__ == "__main__":
    main()