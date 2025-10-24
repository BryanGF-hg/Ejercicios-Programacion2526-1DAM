import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

#ÐNINIE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie= tk.Entry(marco)
dninie.pack(padx=10,pady=10)

#NOMBRE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
nombres= tk.Entry(marco)
nombres.pack(padx=10,pady=10)

#APELLIDOS
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
apellidos= tk.Entry(marco)
apellidos.pack(padx=10,pady=10)

#EMAIL
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)

#BOTON
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)

marco.pack(padx=20,pady=20)

ventana.mainloop()
