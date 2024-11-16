from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate(num1, num2, operation):
    """Perform the calculation based on the operation."""
    try:
        num1, num2 = float(num1), float(num2)
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
    except ValueError:
        return "Error: Invalid numbers"

@app.route('/')
def home():
    """Render the calculator page."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def handle_calculation():
    """Handle the calculation request."""
    data = request.get_json()
    result = calculate(data['num1'], data['num2'], data['operation'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)