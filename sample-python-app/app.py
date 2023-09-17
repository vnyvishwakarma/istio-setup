from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-endpoint', methods=['GET'])
def get_endpoint():
    # You can retrieve query parameters using request.args
    name = request.args.get('name', 'World')
    return jsonify(message=f'Hello, {name}!')

@app.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    # You can retrieve JSON data sent in the request body using request.json
    data = request.json
    if not data:
        return jsonify(message='No data provided'), 400
    
    # Just echoing back the data received in the JSON body
    return jsonify(received_data=data)

if __name__ == '__main__':
    app.run(debug=True)
