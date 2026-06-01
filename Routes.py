from flask import Blueprint, jsonify, request

chess_bp = Blueprint('chess', __name__)

game_state = {
    "turn": "white",
    "moves": []
}

@chess_bp.route("/move", methods=["POST"])
def make_move():
    data = request.json

    move = {
        "from": data.get("from"),
        "to": data.get("to")
    }

    game_state["moves"].append(move)

    game_state["turn"] = (
        "black" if game_state["turn"] == "white"
        else "white"
    )

    return jsonify({
        "success": True,
        "turn": game_state["turn"]
    })
