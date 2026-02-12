from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"""
-------------------------
Time: {datetime.now()}
Name: {name}
Email: {email}
Message: {message}
""")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)

