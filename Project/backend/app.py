from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/api/test')
def hello():
    return {'message': 'Hello World!'}

# Addition operation
@app.route('/api/add', methods=['POST'])
def add():
    data_request = request.get_json()
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    result = number_1 + number_2
    return jsonify({'result': result})

# Multiplication operation
@app.route('/api/multiply', methods=['POST'])
def multiply():
    data_request = request.get_json()
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    result = number_1 * number_2
    return jsonify({'result': result})

# Subtraction operation
@app.route('/api/subtract', methods=['POST'])
def subtract():
    data_request = request.get_json()
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    result = number_1 - number_2
    return jsonify({'result': result})

# Division operation
@app.route('/api/divide', methods=['POST'])
def divide():
    data_request = request.get_json()
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    if number_2 == 0:
        return jsonify({'error': 'Division by zero'}), 400
    result = number_1 / number_2
    return jsonify({'result': result})

# Square root operation
@app.route('/api/sqrt', methods=['POST'])
def square_root():
    data_request = request.get_json()
    if not data_request or 'number' not in data_request:
        return jsonify({'error': 'Invalid input'}), 400

    number = float(data_request['number'])
    if number < 0:
        return jsonify({'error': 'Cannot calculate square root of a negative number'}), 400
    result = math.sqrt(number)
    return jsonify({'result': result})

# Exponentiation operation
@app.route('/api/power', methods=['POST'])
def power():
    data_request = request.get_json()
    if (not data_request or 'base' not in data_request or
            'exponent' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    base = float(data_request['base'])
    exponent = float(data_request['exponent'])
    result = math.pow(base, exponent)
    return jsonify({'result': result})

# Trigonometric functions
@app.route('/api/trig', methods=['POST'])
def trigonometric():
    data_request = request.get_json()
    if not data_request or 'function' not in data_request or 'angle' not in data_request:
        return jsonify({'error': 'Invalid input'}), 400

    function = data_request['function'].lower()
    angle = float(data_request['angle'])

    if function == 'sin':
        result = math.sin(math.radians(angle))
    elif function == 'cos':
        result = math.cos(math.radians(angle))
    elif function == 'tan':
        result = math.tan(math.radians(angle))
    else:
        return jsonify({'error': 'Invalid trigonometric function'}), 400

    return jsonify({'result': result})

# Logarithm operation
@app.route('/api/log', methods=['POST'])
def logarithm():
    data_request = request.get_json()
    if not data_request or 'number' not in data_request:
        return jsonify({'error': 'Invalid input'}), 400

    number = float(data_request['number'])
    if number <= 0:
        return jsonify({'error': 'Cannot calculate logarithm of a non-positive number'}), 400

    base = float(data_request.get('base', math.e))  # Default to natural log if base not provided
    result = math.log(number, base)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
