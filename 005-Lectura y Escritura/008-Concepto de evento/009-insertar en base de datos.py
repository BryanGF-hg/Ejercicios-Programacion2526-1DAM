import mysql.connector
import tkinter as tk
conexion = mysql.connector.connect(host="localhost", user="empresadam", password="Empresadam123$", database="empresadam")
cursor = conexion.cursor()
ventana = tk.Tk()
def insertar():
 cursor.execute('''
  INSERT INTO clientes
  VALUES(
    NULL,
    "'''+dninie.get()+'''",
    "'''+nombres.get()+'''",
    "'''+apellidos.get()+'''",
    "'''+email.get()+'''"
  );
''')
 conexion.commit()
marco = tk.Frame(ventana)
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie= tk.Entry(marco)
dninie.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce los nombres del cliente").pack(padx=10,pady=10)
nombres= tk.Entry(marco)
nombres.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos= tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)
tk.Button(marco,text="Insertar clientes",command = insertar).pack(padx=10,pady=10)
marco.pack(padx=20,pady=20)
ventana.mainloop()
conexion.close()
