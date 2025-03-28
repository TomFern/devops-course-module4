from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# Get Redis host and port from environment variables; default to 'redis' and 6379.
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    return "Hello from Flask app connected to Redis!"

@app.route("/set", methods=["POST"])
def set_value():
    key = request.json.get("key")
    value = request.json.get("value")
    if not key or not value:
        return jsonify({"error": "Both 'key' and 'value' are required."}), 400
    r.set(key, value)
    return jsonify({"message": f"Set {key} = {value}"}), 200

@app.route("/get/<key>")
def get_value(key):
    value = r.get(key)
    if value is None:
        return jsonify({"error": "Key not found."}), 404
    return jsonify({key: value}), 200

if __name__ == '__main__':
    # Bind to all interfaces so the container can expose the service properly.
    app.run(host="0.0.0.0", port=4000, debug=True)

