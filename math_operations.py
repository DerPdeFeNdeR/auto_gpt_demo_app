from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:
        result = float(num1) + float(num2)
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input.'})

@app.route('/subtract', methods=['POST'])
def subtract():
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:
        result = float(num1) - float(num2)
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input.'})

@app.route('/multiply', methods=['POST'])
def multiply():
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:
        result = float(num1) * float(num2)
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input.'})

@app.route('/divide', methods=['POST'])
def divide():
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:
        result = float(num1) / float(num2)
        return jsonify({'result': result})
    except ZeroDivisionError:
        return jsonify({'error': 'Cannot divide by zero.'})
    except:
        return jsonify({'error': 'Invalid input.'})

if __name__ == '__main__':
    app.run(debug=True)