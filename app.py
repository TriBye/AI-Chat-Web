from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Root route
@app.route('/', methods=['GET'])
def index():
    return "Hello from Flask! This is the root route."

# Example API route
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask on Render!"})

# Entry point
if __name__ == '__main__':
    # Render typically detects the correct port automatically, 
    # but you can explicitly set it to 5000.
    app.run(host='0.0.0.0', port=5000)
