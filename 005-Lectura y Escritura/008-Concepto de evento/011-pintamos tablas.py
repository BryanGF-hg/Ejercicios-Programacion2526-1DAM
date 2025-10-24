import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

arbol = ttk.Treeview(ventana, columns=("nombre","apellidos"), show="headings")
arbol.heading("nombre",text="Nombre del cliente")
arbol.heading("apellidos",text="Apellidos del cliente")

arbol.insert("","end", values=("Bryan Glot","Fong"))
arbol.insert("","end", values=("Baron Gut","Fart"))

arbol.pack(padx=20,pady=20)

ventana.mainloop()
