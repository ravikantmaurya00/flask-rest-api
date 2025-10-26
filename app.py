from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
users = [
    {"id": 1, "name": "Ravi", "email": "ravi@example.com"},
    {"id": 2, "name": "Shreya", "email": "shreya@example.com"}
]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to User Management API"}), 200


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email")):
        return jsonify({"error": "Invalid data"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201


# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200


# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
