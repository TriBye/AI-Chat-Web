from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ensures the frontend can call the backend

@app.route('/', methods=['GET'])
def index():
    return "Hello from Flask! (Root route)"

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask on Render!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)