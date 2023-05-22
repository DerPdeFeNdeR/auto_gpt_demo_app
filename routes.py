# Importing the necessary modules
from flask import Flask, request, jsonify, render_template

# Creating the Flask app
app = Flask(__name__,template_folder='.')

# Defining the routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input'})

@app.route('/subtract', methods=['POST'])
def subtract():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 - num2
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input'})

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 * num2
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input'})

@app.route('/divide', methods=['POST'])
def divide():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'})
        result = num1 / num2
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid input'})

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
