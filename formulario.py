import tkinter as tk
from tkinter import messagebox
from services.mi_sql import conectar

class FormularioProducto(tk.Frame):
    def __init__(self, master, refrescar_callback=None):
        super().__init__(master)
        self.refrescar_callback = refrescar_callback
        # Solo mostrar estos campos en el formulario
        self.campos = ["Nombre", "Precio", "Cantidad"]
        self.entradas = {}
        
        # Contenedor principal
        contenedor = tk.LabelFrame(self, text="Registro de Producto", padx=10, pady=10)
        contenedor.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Formulario simplificado
        for campo in self.campos:
            fila = tk.Frame(contenedor)
            fila.pack(fill="x", pady=5)
            
            tk.Label(fila, text=campo, width=15, anchor="w").pack(side="left")
            entry = tk.Entry(fila)
            entry.pack(fill="x", padx=5)
            self.entradas[campo] = entry

        tk.Button(contenedor, text="Guardar", command=self.guardar_producto, 
                 bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

    def guardar_producto(self):
        datos = {campo: self.entradas[campo].get().strip() for campo in self.campos}
        
        # Validar campos
        if not all(datos.values()):
            messagebox.showerror("Error", "Completa todos los campos")
            return
            
        # Validar campos numéricos
        try:
            precio = float(datos["Precio"])
            cantidad = int(datos["Cantidad"])
        except ValueError:
            messagebox.showerror("Error", "Precio y Cantidad deben ser números válidos")
            return
            
        try:
            # Consulta parametrizada
            query = """
                INSERT INTO productos (nombre, precio, cantidad) 
                VALUES (%s, %s, %s)
            """
            
            # Valores en el orden correcto
            valores = (
                datos["Nombre"],
                precio,
                cantidad
            )
            
            # Ejecutar consulta con parámetros
            conectar(query, valores)
            
            # Limpiar campos después de guardar
            for entrada in self.entradas.values():
                entrada.delete(0, tk.END)
                
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Producto guardado exitosamente")
            
            # Refrescar catálogo si existe callback
            if self.refrescar_callback:
                self.refrescar_callback()
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")