from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    nombre = request.args.get("nombre")
    mensaje = f"¡Hola {nombre}!"
    return render_template("index.html", saludo=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
