# app.py
from flask import Flask, request, jsonify, send_from_directory
import game

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    result = game.play(data["choice"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)