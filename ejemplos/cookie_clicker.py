import tkinter as tk

etiqueta = None
contador = 0
def respuesta():
    global contador
    contador = contador + 1
    etiqueta.config(text = contador)

ventana = tk.Tk()
# ventana.title("Mostrar imagen en Tkinter")

frm = tk.Frame(ventana)
frm.grid()

# Cargar la imagen (debe ser GIF o PNG)
imagen = tk.PhotoImage(file="ejemplos/cookie.png")

tk.Button(frm, image=imagen, command=respuesta).grid(column=0, row=0)
etiqueta = tk.Label(frm, text='Hazme click')
etiqueta.grid(column=0, row=1)

ventana.mainloop()