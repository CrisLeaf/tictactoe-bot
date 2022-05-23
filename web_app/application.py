from flask import Blueprint, request, jsonify
from .minimax import next_move

bp = Blueprint("app", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
def home():
    return """Home"""

@bp.route("/next", methods=["GET"])
def get_next_move():
    board = request.args.get("board")
    next_piece = int(request.args.get("piece"))

    def translate_board(value):
        return -1 if int(value) >= 2 else int(value)

    board_list = [
        [translate_board(board[0]), translate_board(board[1]), translate_board(board[2])],
        [translate_board(board[3]), translate_board(board[4]), translate_board(board[5])],
        [translate_board(board[6]), translate_board(board[7]), translate_board(board[8])]
    ]

    move = next_move(board_list, -1 if next_piece == 2 else next_piece)

    if move == "00":
        response = 0
    elif move == "01":
        response = 1
    elif move == "02":
        response = 2
    elif move == "10":
        response = 3
    elif move == "11":
        response = 4
    elif move == "12":
        response = 5
    elif move == "20":
        response = 6
    elif move == "21":
        response = 7
    elif move == "22":
        response = 8

    return jsonify({"next-move": response})
