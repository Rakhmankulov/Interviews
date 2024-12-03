import os
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello!"

@app.route('/hello there')
def hello():
    phrase = random.choice(["Good day","Glad to see you","Hello"])
    return phrase + ', my friend.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
