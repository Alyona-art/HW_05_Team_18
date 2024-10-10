from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
likes = {}
user_service_url = 'http://localhost:5001/users'

@app.route('/likes', methods=['POST'])
def like_message():
    username = request.json.get('username')
    message_id = request.json.get('message_id')

    # Check if the user is registered
    response = requests.get(user_service_url)
    registered_users = response.json()
    
    if username not in registered_users:
        return jsonify({"error": "User not registered"}), 403

    # Update likes for the specified message
    if message_id not in likes:
        likes[message_id] = 0
    likes[message_id] += 1
    
    return jsonify({"message": "Message liked successfully"}), 201

@app.route('/likes/<int:message_id>', methods=['GET'])
def get_likes(message_id):
    count = likes.get(message_id, 0)
    return jsonify({"likes": count}), 200

if __name__ == '__main__':
    app.run(port=5003)