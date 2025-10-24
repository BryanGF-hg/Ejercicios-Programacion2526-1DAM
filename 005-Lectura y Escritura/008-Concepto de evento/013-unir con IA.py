#pip3 install ttkbootstrap --break-system-packages
#pip3 install --upgrade Pillow --break-system-packages
import tkinter as tk
from tkinter import ttk
import mysql.connector
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# --- DATABASE CONNECTION ---
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# --- MAIN WINDOW ---
ventana = tb.Window(themename="superhero")  # try "flatly", "darkly", "morph", etc.
ventana.title("Gestión de Clientes - EmpresaDAM")
ventana.geometry("800x600")

# --- TREEVIEW SECTION ---
frame_tabla = ttk.LabelFrame(ventana, text="Listado de Clientes", padding=10)
frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)

arbol = ttk.Treeview(
    frame_tabla,
    columns=("dninie", "nombre", "apellidos", "email"),
    show="headings",
    height=10
)

# Define column headers
arbol.heading("dninie", text="DNI/NIE del cliente")
arbol.heading("nombre", text="Nombre")
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Email")

# Adjust column widths
arbol.column("dninie", width=120, anchor="center")
arbol.column("nombre", width=150, anchor="center")
arbol.column("apellidos", width=180, anchor="center")
arbol.column("email", width=200, anchor="center")

# Add scrollbar
scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=arbol.yview)
arbol.configure(yscroll=scroll.set)
scroll.pack(side="right", fill="y")
arbol.pack(fill="both", expand=True)

# --- FORM SECTION ---
frame_form = ttk.LabelFrame(ventana, text="Insertar Nuevo Cliente", padding=10)
frame_form.pack(fill="x", padx=20, pady=10)

# Create form entries with ttkbootstrap styling
labels = ["DNI/NIE", "Nombre", "Apellidos", "Email"]
entries = {}

for label_text in labels:
    lbl = ttk.Label(frame_form, text=f"{label_text}:")
    lbl.pack(anchor="w", padx=10, pady=3)
    entry = ttk.Entry(frame_form, width=50)
    entry.pack(padx=10, pady=3)
    entries[label_text.lower()] = entry

# --- FUNCTIONS ---
def cargar_clientes():
    """Carga los clientes desde la base de datos al Treeview."""
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    # Limpiar la tabla antes de recargar
    for item in arbol.get_children():
        arbol.delete(item)
    for fila in filas:
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))

def insertar_cliente():
    """Inserta un nuevo cliente y refresca la tabla."""
    dninie = entries["dni/nie"].get().strip()
    nombre = entries["nombre"].get().strip()
    apellidos = entries["apellidos"].get().strip()
    email = entries["email"].get().strip()

    if not (dninie and nombre and apellidos and email):
        tb.Messagebox.show_warning("Por favor, completa todos los campos.", title="Atención")
        return

    try:
        cursor.execute(
            "INSERT INTO clientes VALUES (NULL, %s, %s, %s, %s);",
            (dninie, nombre, apellidos, email)
        )
        conexion.commit()
        tb.Messagebox.show_info("Cliente insertado correctamente ✅", title="Éxito")
        cargar_clientes()
        for entry in entries.values():
            entry.delete(0, tk.END)
    except Exception as e:
        tb.Messagebox.show_error(f"Error al insertar: {e}", title="Error")

# --- BUTTON ---
btn_insertar = tb.Button(frame_form, text="Insertar Cliente", bootstyle=SUCCESS, command=insertar_cliente)
btn_insertar.pack(padx=10, pady=15)

# Load data initially
cargar_clientes()

# --- RUN APP ---
ventana.mainloop()

# Close database connection when app exits
conexion.close()

