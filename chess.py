class ChessEngine:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p"] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            ["P"] * 8,
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]

        if piece == "":
            return False

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ""
        return True

    def get_board(self):
        return self.board
