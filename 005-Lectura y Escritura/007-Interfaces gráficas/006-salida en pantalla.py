#sudo apt-get install python3-tk
import tkinter as tk

def accion():
 etiqueta.config(text=" Pues sí que has pulsado el boton")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)
etiqueta = tk.Label(text="Has pulsado el boton?")
etiqueta.pack(padx=10,pady=10)
# padx= margen de izquierda a derecha
# pady = margen de arriba a abajo

ventana.mainloop() #No te salgas
