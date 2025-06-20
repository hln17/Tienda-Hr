import tkinter as tk
from tkinter import ttk
from services.mi_sql import conectar

def cargar_productos(master):
    return CatalogoProductos(master)

class CatalogoProductos(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnas = 3
        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill="both", expand=True)
        self.cargar_productos()

    def cargar_productos(self):
        # Limpiar contenedor
        for widget in self.contenedor.winfo_children():
            widget.destroy()
            
        try:
            # Obtener todos los datos necesarios para mostrar
            resultados = conectar("""
                SELECT id, nombre, precio, cantidad, clase 
                FROM productos;
            """)
            
            if not resultados:
                ttk.Label(self.contenedor, text="No hay productos disponibles").pack(pady=20)
                return
                
            # Crear las tarjetas de productos
            for index, producto in enumerate(resultados):
                id_, nombre, precio, cantidad, clase = producto
                
                # Crear marco para cada tarjeta
                tarjeta = tk.Frame(
                    self.contenedor, 
                    bd=1, 
                    relief="solid", 
                    padx=15, 
                    pady=10,
                    bg="#f8f9fa"
                )
                tarjeta.grid(
                    row=index // self.columnas, 
                    column=index % self.columnas, 
                    padx=10, 
                    pady=10, 
                    sticky="nsew"
                )

                # Encabezado con ID y Nombre
                tk.Label(
                    tarjeta, 
                    text=f"{id_} - {nombre}", 
                    font=("Arial", 10, "bold"),
                    bg="#f8f9fa"
                ).pack(anchor="w", pady=(0, 5))

                # Detalles del producto
                tk.Label(
                    tarjeta, 
                    text=f"Precio: ${precio}", 
                    font=("Arial", 9),
                    bg="#f8f9fa",
                    anchor="w"
                ).pack(anchor="w", fill="x")
                
                tk.Label(
                    tarjeta, 
                    text=f"Stock: {cantidad} unidades", 
                    font=("Arial", 9),
                    bg="#f8f9fa",
                    anchor="w"
                ).pack(anchor="w", fill="x")
                
                tk.Label(
                    tarjeta, 
                    text=f"Categoría: {clase}", 
                    font=("Arial", 9),
                    bg="#f8f9fa",
                    anchor="w"
                ).pack(anchor="w", fill="x")
                
        except Exception as e:
            ttk.Label(self.contenedor, text=f"Error al cargar productos: {e}", foreground="red").pack()