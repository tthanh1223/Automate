"""
convention: b : for black side, w : for white side
"""
#Phải xem lại ngày mai - giờ k tập trung được clm

def isValidChessBoard(board):
    # Define the possible spaces on the board
    valid_spaces = [f"{i}{chr(j)}" for i in range(1, 9) for j in range(ord('a'), ord('h') + 1)]

    # Dictionary to count the number of pieces
    piece_count = {
        'wking': 0, 'bking': 0,
        'wpawn': 0, 'bpawn': 0,
        'wtotal': 0, 'btotal': 0
    }

    # Define valid piece types
    valid_piece_types = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    # Iterate over each piece on the board
    for position, piece in board.items():
        # Check if the position is valid
        if position not in valid_spaces:
            return False

        # Check if the piece name is valid
        if len(piece) < 2 or piece[0] not in ('w', 'b') or piece[1:] not in valid_piece_types:
            return False

        # Update the piece counts
        piece_count[piece] = piece_count.get(piece, 0) + 1  # Count specific piece
        if piece[1:] == 'pawn':
            piece_count[piece[0] + 'pawn'] += 1  # Count pawns
        piece_count[piece[0] + 'total'] += 1  # Count total pieces per color

    # Validate the piece counts
    if piece_count['wking'] != 1 or piece_count['bking'] != 1:
        return False
    if piece_count['wtotal'] > 16 or piece_count['btotal'] > 16:
        return False
    if piece_count['wpawn'] > 8 or piece_count['bpawn'] > 8:
        return False

    return True


# Example usage
chess_board = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'
}

print(isValidChessBoard(chess_board))  # Output: True or False
