from flask import Flask, request, jsonify


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


# Optional: Completing the following TODOs is optional for more practice

# TODO: Implement the 'multiplication operation'
# @app.route('/api/multiply', methods=['POST'])
# def multiply():
#     data_request = request.get_json()
#     # Check if the input is valid
#     # Perform multiplication
#     # Return the result

# TODO: Implement the 'subtraction operation'
# @app.route('/api/subtract', methods=['POST'])
# def subtract():
#     # Write code here

# TODO: Implement the 'division operation'
# @app.route('/api/divide', methods=['POST'])
# def divide():
#     # Write code here

# TODO: Add more routes and operations! Create your own calculator!
# For example:
# - Square root
# - Exponentiation
# - Trigonometric functions (sin, cos, tan)
# - Logarithms

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
