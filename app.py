from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("\n🔥 NEW SUBMISSION RECEIVED 🔥")
    print(json.dumps(data, indent=2))

    return {"received": True}, 200
