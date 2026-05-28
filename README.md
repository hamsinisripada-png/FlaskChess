# ♟️ FlaskChess AI

An interactive, web-based chess application featuring a custom-built, optimized adversarial AI search engine. The frontend provides a responsive game interface, while the Python backend computes optimal responses in real time using advanced decision-tree pruning techniques.

---

## 🧠 AI Engine Architecture & Optimization:
The AI engine (`chess_engine.py`) evaluates positions using a multi-layered game-tree search pipeline:

* **Positional Evaluation:** Implements static evaluation matrices utilizing **Piece-Square Tables (PSTs)**. The algorithm evaluates material balances and piece positionings (e.g., controlling center squares, discouraging passive king setups).
* **$\alpha$-$\beta$ Pruning:** Optimizes the traditional Minimax search framework by maintaining tracking bounds ($\alpha$ and $\beta$). This allows the engine to securely discard sub-optimal branches, saving valuable compute frames.
* **Iterative Deepening:** Runs progressive search loops through shifting plies. It leverages move-sequence predictions from shallow depths to continuously structure alpha-beta cutoffs as complexity expands.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

* **Backend:** Flask (WSGI web application routing), `python-chess` (move generation and rule verification).
* **Frontend:** `chessboard.js` (UI board layout visualization) and `chess.js` (client-side validation hooks).

---

## 📦 Core Directory Mapping
```text
.
└── FlaskChess/           # Main project directory
    ├── static/           # Frontend stylesheet frameworks & chessboard JS assets
    ├── templates/        # Main presentation layers (index.html, board.html)
    ├── flask_app.py      # Core web entry point & API route endpoint mappings
    ├── chess_engine.py   # Adversarial Minimax / Alpha-Beta algorithm architecture
    ├── board_test.py     # Independent validation utility scripts
    └── .gitignore        # Version control tracking exclude maps
