from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def log_change(action):
    with open("backup.log", "a") as f:
        f.write(f"{datetime.datetime.now()}: {action}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        val1 = request.form.get('val1')
        val2 = request.form.get('val2')
        op = request.form.get('operation')

        try:
            if op == 'add':
                # Suma aritmética simple (Paso 2)
                result = float(val1) + float(val2)
            elif op == 'bin':
                # Conversión binaria (Paso 2)
                result = bin(int(val1))
            elif op == 'and':
                # Calculadora lógica (Paso 9)
                result = int(val1) & int(val2)
            
            log_change(f"Calculated {op} with {val1}, {val2}")
        except Exception as e:
            result = f"Error: {e}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)