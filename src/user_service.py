from flask import Flask, request, jsonify

app = Flask(__name__)
users = set()
users.add('test_user')

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    if username and username not in users:
        users.add(username)
        return jsonify({"message": "User registered successfully"}), 201
    return jsonify({"error": "Username already exists or invalid"}), 400

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    if username in users:
        return jsonify({'message': 'User logged in successfully!'}), 200
    return jsonify({'message': 'User not found!'}), 404

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(list(users)), 200

if __name__ == '__main__':
    app.run(port=5001)