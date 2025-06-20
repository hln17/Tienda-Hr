import tkinter as tk
from tkinter import messagebox
from services.mi_sql import conectar

def cargar_login(ventana, on_success_callback):
    login_panel = tk.Frame(ventana, bg="#f0f0f0", width=1000, height=600)
    login_panel.pack(fill="both", expand=True)

    # Contenedor central
    contenedor_central = tk.Frame(login_panel, bg="#ffffff", bd=2, relief="groove", padx=40, pady=30)
    contenedor_central.place(relx=0.5, rely=0.5, anchor="center")

    titulo = tk.Label(contenedor_central, text="Inicio de Sesión", font=("Arial", 16), bg="#ffffff")
    titulo.pack(pady=20)

    tk.Label(contenedor_central, text="Correo", bg="#ffffff", anchor="w").pack(fill="x")
    entrada_correo = tk.Entry(contenedor_central, width=30)
    entrada_correo.pack(fill="x", pady=(0, 10))

    tk.Label(contenedor_central, text="Contraseña", bg="#ffffff", anchor="w").pack(fill="x")
    entrada_contrasena = tk.Entry(contenedor_central, show="*", width=30)
    entrada_contrasena.pack(fill="x", pady=(0, 10))

    def boton_continuar():
        correo = entrada_correo.get().strip()
        contrasenna = entrada_contrasena.get().strip()

        if not correo or not contrasenna:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        try:
            resultado = conectar(f"SELECT * FROM usuarios WHERE correo = '{correo}' AND contrasenna = '{contrasenna}'")
            if resultado:
                on_success_callback(resultado[0])
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión: {e}")

    boton = tk.Button(contenedor_central, text="Continuar", command=boton_continuar, 
                     bg="#4A235A", fg="white", padx=15, pady=5)
    boton.pack(pady=20)

    return login_panel