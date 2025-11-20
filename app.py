from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("\n===== NEW WEBHOOK PAYLOAD =====")
        print(json.dumps(data, indent=2))
        print("================================\n")

        return {"received": True}, 200

    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}, 500

app.run(host="0.0.0.0", port=8080)
