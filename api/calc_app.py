from flask import request
from api import create_app
from api.calculator import Calculator


def create_calculator(_app=None):

    app = _app if _app else create_app()

    @app.route('/healthcheck', methods=['get'])
    def health():
        return "It's ok!"

    @app.route('/api/add', methods=['POST'])
    def add():
        return operation('add', 2)

    @app.route('/api/subtract', methods=['POST'])
    def subtract():
        return operation('subtract', 2)

    @app.route('/api/multiply', methods=['POST'])
    def multiply():
        return operation('multiply', 2)

    @app.route('/api/divide', methods=['POST'])
    def divide():
        return operation('divide', 2)

    def operation(method, num_factors):
        factors = []
        if num_factors == 2:
            factors.append(float(request.json.get('x')))
            factors.append(float(request.json.get('y')))

        return str(getattr(Calculator, method)(*factors))
    return app


if __name__ == "__main__":
    calculator = create_calculator()
    calculator.run(host='0.0.0.0', port=8080)
