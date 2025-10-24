from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n < 0:
        raise ValueError("El numero no puede ser negativo")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@app.route('/factorial/<int:n>', methods=['GET'])
def get_factorial(n):
    try:
        f = factorial(n)
        etiqueta = "par" if f % 2 == 0 else "impar"
        return jsonify({
            "number": n,
            "factorial": f,
            "etiqueta": etiqueta
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
