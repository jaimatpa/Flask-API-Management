from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f'Hello from my Flask API Endpoint Server'

@app.route('/hello', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'no last name provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()
    return jsonify({'message': f'Hello {nameCapital} {lastnameCapital}!'})


if __name__ == '__main__':
    app.run(debug=True)


## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooper