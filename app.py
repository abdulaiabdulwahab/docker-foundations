from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

# Environment variable lets Docker inject configuration
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from Docker!")

# Data written here can later be persisted with a Docker volume
DATA_FILE = "/data/visits.txt"


@app.get("/")
def home():
    return jsonify(
        message=APP_MESSAGE,
        hostname=socket.gethostname()
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/visits")
def visits():

    # Make sure the directory exists
    os.makedirs("/data", exist_ok=True)

    try:
        with open(DATA_FILE, "r") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0

    count += 1

    with open(DATA_FILE, "w") as file:
        file.write(str(count))

    return jsonify(visits=count)


if __name__ == "__main__":

    # 0.0.0.0 is important inside a container.
    # Binding only to localhost would prevent traffic
    # entering through Docker's published port.
    app.run(
        host="0.0.0.0",
        port=5000
    )