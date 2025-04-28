from ejemplos.calculadora import calcular
import tkinter as tk

txtOp1 = txtOp2 = txtOp = lblResultado = None
def respuesta():
    a = float(txtOp1.get("1.0", "end-1c"))
    b = float(txtOp2.get("1.0", "end-1c"))
    
    op = txtOp.get("1.0", "end-1c")
    
    resultado = calcular(a, op, b)
    
    lblResultado.config(text = resultado)

ventana = tk.Tk()
ventana.title("Calculadora")

frm = tk.Frame(ventana)
frm.grid()

txtOp1 = tk.Text(frm, height=1, width=10)
txtOp1.grid(column=0, row=0)
txtOp = tk.Text(frm, height=1, width=10)
txtOp.grid(column=1, row=0)
txtOp2 = tk.Text(frm, height=1, width=10)
txtOp2.grid(column=2, row=0)
tk.Button(frm, text='=', command=respuesta, height=1, width=10).grid(column=3, row=0)
lblResultado = tk.Label(frm, text='', height=1, width=10)
lblResultado.grid(column=4, row=0)

ventana.mainloop()