import tkinter as tk

def cargar_header(ventana):
    Header_panel = tk.Frame(
        ventana, bg="red", 
        padx=0,
        pady=0,
        width="1000",
        height="150")
    Header_panel.pack()
    print("panel header cargados")
   