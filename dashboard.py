from flask import Flask, render_template
from database import (
    obtener_total_ofertas,
    obtener_empresas_top,
    obtener_salario_promedio
)

app = Flask(__name__)

@app.route("/")
def inicio():

    total = obtener_total_ofertas()
    empresas = obtener_empresas_top()
    salario_promedio = obtener_salario_promedio()

    return render_template(
        "index.html",
        total=total,
        empresas=empresas,
        salario_promedio=salario_promedio
    )

if __name__ == "__main__":
    app.run(debug=True)