from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    return f'Hello {name}!'

    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)