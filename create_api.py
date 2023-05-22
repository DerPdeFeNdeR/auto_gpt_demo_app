# Import necessary modules
from flask import Flask, request

# Create Flask app
app = Flask(__name__)

# Define endpoints for different mathematical operations
@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return str(a + b)

@app.route('/subtract')
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return str(a - b)

@app.route('/multiply')
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return str(a * b)

@app.route('/divide')
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if b == 0:
        return 'Error: Division by zero'
    return str(a / b)

# Run app with Gunicorn
if __name__ == '__main__':
    app.run()