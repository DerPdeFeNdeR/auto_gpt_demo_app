from flask import Flask, request, jsonify
from operations import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = add(num1, num2)
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract_route():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = subtract(num1, num2)
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply_route():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = multiply(num1, num2)
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide_route():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = divide(num1, num2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()