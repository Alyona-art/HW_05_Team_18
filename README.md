## Twitter-like system based on distributed services

This project demonstrates the service-based architectural pattern for the system where users can post short messages, read them and like them.

To implement a simple Twitter-like system, we created three services:

1. **User Service**: Manages user registration, login and information about all registered users.
2. **Message Service**: Handles message posting and fetching messages.
3. **Like Service**: Manages liking messages.

### Project Structure

- **`user_service.py`:** Contains the User Service
- **`message_service.py`:** Contains the Message Service
- **`like_service.py`:** Contains the Like Service

### Service Structure

1. **User Service**: 
   - Endpoints:
     - `POST /register`: Register a user (username should be unique and not empty).
     - `POST /login`: login a user (user should be registered before).
     - `GET /users`: List all registered users.

2. **Message Service**: 
   - Endpoints:
     - `POST /messages`: Post a message (requires a registered user).
     - `GET /messages`: Get the last 10 messages.

3. **Like Service**:
   - Endpoints:
     - `POST /likes`: Like a message (requires a registered user).
     - `GET /likes/{message_id}`: Get the like count for a message.

### How to Run

**Run all servers:**
   - User Service: `python user_service.py`
   - Message Service: `python message_service.py`
   - Like Service: `python like_service.py`

After that, you can test the application using various tools (Postman, Curl, etc.).