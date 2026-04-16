from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def log_change(action):
    with open("backup.log", "a") as f:
        f.write(f"{datetime.datetime.now()}: {action}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    # Punto 12: Variable extra para mostrar la hora en la página
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if request.method == 'POST':
        val1 = request.form.get('val1')
        val2 = request.form.get('val2')
        op = request.form.get('operation')

        try:
            if op == 'add':
                # Suma aritmética (Paso 2)
                result = float(val1) + float(val2)
            elif op == 'bin':
                # Conversión binaria (Paso 2)
                result = bin(int(val1))
            elif op == 'and':
                # Lógica AND (Paso 9)
                result = int(val1) & int(val2)
            
            log_change(f"Calculated {op} with {val1}, {val2}")
        except:
            result = "Error"

    return render_template('index.html', result=result, fecha=ahora)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)