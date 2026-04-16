from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def registrar_log(operacion, resultado):
    with open("backup.log", "a") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] {operacion} | Resultado: {resultado}\n")

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    res = None
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        if tipo == 'logica':
            v1 = request.form.get('v1') == '1'
            v2 = request.form.get('v2') == '1'
            op = request.form.get('op_log')
            if op == 'AND': res = int(v1 and v2)
            elif op == 'OR': res = int(v1 or v2)
            registrar_log(f"Operacion Logica {op}", res)
    return render_template('index.html', resultado=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)