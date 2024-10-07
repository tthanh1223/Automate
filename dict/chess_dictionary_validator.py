"""
convention: b : for black side, w : for white side
"""
#Phải xem lại ngày mai - giờ k tập trung được clm

def isValidChessBoard(board):
    # Define the possible spaces on the board
    valid_spaces = [f"{i}{chr(j)}" for i in range(1, 9) for j in range(ord('a'), ord('h') + 1)]

    # Dictionary to count the number of pieces
    piece_count = {
        'w_king': 0, 'b_king': 0,
        'w_pawn': 0, 'b_pawn': 0,
        'w_total': 0, 'b_total': 0
    }

    # Define valid piece types
    valid_piece_types = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    # Iterate over each piece on the board
    for position, piece in board.items():
        # Check if the position is valid
        if position not in valid_spaces:
            return False

        # Check if the piece name is valid
        if len(piece) < 2 or piece[:2] not in ('w_', 'b_') or piece[2:] not in valid_piece_types:
            return False

        # Update the piece counts
        piece_count[piece] = piece_count.get(piece, 0) + 1  # Count the specific piece
        if piece[2:] == 'pawn':
            piece_count[piece[:2] + 'pawn'] += 1  # Count pawns
        piece_count[piece[:2] + 'total'] += 1  # Count total pieces per color

    # Validate the piece counts
    if piece_count['w_king'] != 1 or piece_count['b_king'] != 1:
        return False
    if piece_count['w_total'] > 16 or piece_count['b_total'] > 16:
        return False
    if piece_count['w_pawn'] > 8 or piece_count['b_pawn'] > 8:
        return False

    return True


# Example usage
chess_board = {
    '1h': 'b_king', '6c': 'w_queen', '2g': 'b_bishop',
    '5h': 'b_queen', '3e': 'w_king'
}

print(isValidChessBoard(chess_board))  # Output: True or False

# Define the board
#