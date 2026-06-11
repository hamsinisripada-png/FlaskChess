@app.route("/move", methods=["POST"])
def make_move():
    data = request.json
    move = chess.Move.from_uci(data["move"])

    if move in board.legal_moves:
        board.push(move)
        move_history.append(data["move"])

        game_status = "ongoing"

        if board.is_checkmate():
            winner = "Black" if board.turn else "White"
            game_status = f"Checkmate! {winner} wins."

        elif board.is_stalemate():
            game_status = "Draw by stalemate."

        elif board.is_check():
            game_status = "Check!"

        return jsonify({
            "status": "success",
            "fen": board.fen(),
            "moves": move_history,
            "game_status": game_status
        })

    return jsonify({
        "status": "invalid move"
    }), 400
