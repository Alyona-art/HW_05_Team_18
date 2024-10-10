from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
messages = []
user_service_url = 'http://localhost:5001/users'

@app.route('/messages', methods=['POST'])
def post_message():
    username = request.json.get('username')
    content = request.json.get('content')

    if len(content) > 400:
        return jsonify({"error": "Message must be less than 400 characters"}), 400

    # Check if the user is registered
    response = requests.get(user_service_url)
    registered_users = response.json()
    
    if username not in registered_users:
        return jsonify({"error": "User not registered"}), 403

    messages.append({"username": username, "content": content})
    return jsonify({"message": "Message posted successfully"}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages[-10:]), 200  # Return last 10 messages

if __name__ == '__main__':
    app.run(port=5002)