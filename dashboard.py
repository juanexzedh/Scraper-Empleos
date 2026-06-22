from flask import Flask, render_template, request
from modelos.database import (obtener_total_ofertas, obtener_empresas_top, obtener_salario_promedio, obtener_ciudades_top, buscar_por_palabra_clave, contar_tecnologias, obtener_ofertas)

app = Flask(__name__)

@app.route("/")
def inicio():

    total = obtener_total_ofertas()
    empresas = obtener_empresas_top()
    salario_promedio = obtener_salario_promedio()
    top_tecnologias = contar_tecnologias()
    ofertas = obtener_ofertas()

    return render_template(
        "index.html",
        total = total,
        empresas = empresas,
        salario_promedio = salario_promedio,
        tecnologias = top_tecnologias,
        ofertas = ofertas
    )

@app.route("/buscar")
def buscar():

    palabra = request.args.get("q", "")

    resultados = buscar_por_palabra_clave(palabra)
    return render_template(
        "resultados.html",
        resultados=resultados,
        palabra=palabra
    )

if __name__ == "__main__":
    app.run(debug=True)

