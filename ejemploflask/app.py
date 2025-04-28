from flask import Flask, render_template, request

from calculadora import calcular

app = Flask(__name__)

@app.route("/")
def home():
    nombre = request.args.get("nombre")
    mensaje = f"¡Hola {nombre}!"
    return render_template("index.html", saludo=mensaje)

@app.route("/calculadora")
def calculadora():
    op = request.args.get("op")

    if op:
        op1 = float(request.args.get("op1"))
        op2 = float(request.args.get("op2"))

        resultado = calcular(op1, op, op2)

        return render_template("calculadora.html", resultado=resultado)
    
    return render_template("calculadora.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)