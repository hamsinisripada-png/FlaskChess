@app.route("/game")
def game():
    moves_count = len(game.move_history)
    return render_template(
        "game.html",
        board=game.board,
        moves_count=moves_count
    )
