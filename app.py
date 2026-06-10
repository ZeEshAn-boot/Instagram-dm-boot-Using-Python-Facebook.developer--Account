from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
from responses import get_response

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# CREATE APP
app = Flask(__name__)

# HOME ROUTE
@app.route("/")
def home():
    return "ZAIQA Bot Running Successfully!"

# WEBHOOK VERIFICATION (GET)
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print("\n=== VERIFY REQUEST RECEIVED ===")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Verification Successful!")
        return challenge, 200

    print("Verification Failed: Token Mismatch")
    return "Forbidden", 403

# SEND INSTAGRAM MESSAGE RESPONSE
def send_message(recipient_id, text):
    # Instagram graph API endpoint
    url = "https://graph.facebook.com/v25.0/me/messages"

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": text
        }
    }

    params = {
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.post(
            url,
            json=payload,
            params=params,
            timeout=10  # Added explicit timeout safety for API calls
        )
        print("\n=== API SEND LOGS ===")
        print("SEND STATUS:", response.status_code)
        print("SEND RESPONSE:", response.text)
    except requests.exceptions.RequestException as e:
        print("\n=== API SEND ERROR ===")
        print("Failed to send message via Graph API:", e)

# RECEIVE INSTAGRAM MESSAGES (POST)
@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.get_json()

    print("\n=== DATA RECEIVED FROM META ===")
    print(data)

    # Safe guard checking if data is empty or malformed
    if not data:
        return "Invalid Payload", 400

    try:
        if data.get("object") == "instagram":
            for entry in data.get("entry", []):
                for event in entry.get("messaging", []):
                    
                    # Ensure the event contains a message and is not a bot echo fallback loop
                    message_data = event.get("message", {})
                    if message_data and not message_data.get("is_echo"):
                        sender_id = event["sender"]["id"]
                        text = message_data.get("text", "")

                        # Avoid processing empty or media-only messages without explicit text
                        if text:
                            print(f"\nIncoming Message: '{text}' from Sender ID: {sender_id}")

                            # Pull response from responses.py (Your Groq/Hardcoded logic)
                            reply = get_response(text)

                            # Send the reply back to Instagram
                            send_message(sender_id, reply)
                        else:
                            print("\nSkipping incoming event: Message does not contain text strings.")
                            
    except Exception as e:
        print("\nProcessing Error:", e)

    # Always return a 200 OK to Meta immediately so they don't block your webhook endpoint
    return "ok", 200

# RUN APP
if __name__ == "__main__":
    # debug=True automatically reloads changes while testing
    app.run(host="0.0.0.0", port=5000, debug=True)