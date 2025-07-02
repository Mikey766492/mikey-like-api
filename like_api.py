from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/like", methods=["GET"])
def send_like():
    user_id = request.args.get("id")
    count = request.args.get("count", default=30)

    if not user_id:
        return jsonify({
            "status": "error",
            "message": "❌ Missing 'id' parameter"
        }), 400

    return jsonify({
        "status": "success",
        "message": f"✅ {count} likes sent to user {user_id}!"
    })

if __name__ == "__main__":
    app.run()