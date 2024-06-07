
from abc import ABC
from ast import List
from enum import Enum

class PieceType(Enum):
    Rook, Knight, Pawn, Queen, King, Bishop = 1, 2, 3, 4, 5, 6


INITIAL_PIECE_SET_SINGLE = [
    (PieceType.Rook, 0, 0),
    (PieceType.Knight, 1, 0),
    (PieceType.Bishop, 2, 0),
    (PieceType.Queen, 3, 0),
    (PieceType.King, 4, 0),
    (PieceType.Bishop, 5, 0),
    (PieceType.Knight, 6, 0),
    (PieceType.Rook, 7, 0),
    (PieceType.Pawn, 0, 1),
    (PieceType.Pawn, 1, 1),
    (PieceType.Pawn, 2, 1),
    (PieceType.Pawn, 3, 1),
    (PieceType.Pawn, 4, 1),
    (PieceType.Pawn, 5, 1),
    (PieceType.Pawn, 6, 1),
    (PieceType.Pawn, 7, 1)
]

class Color(Enum):
    Black, White = 1, 2

class ChessPosition:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        pass

class Piece(ABC):
    def __init__(self, type: PieceType, color: Color, position: ChessPosition) -> None:
        self._type = type    
        self._color = color
        self._position = position # Box the piece belongs to

    def move(self, target_pos: ChessPosition):
        self._position = target_pos

    def get_threatened_positions(self, board) -> List[ChessPosition]:
        raise NotImplementedError

    def get_moveable_positions(self, board) -> List[ChessPosition]:
        raise NotImplementedError

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(PieceType.Rook, color, position)

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(PieceType.Queen, color, position)

class King(Piece):
    def __init__(self, color, position):
        super().__init__(PieceType.King, color, position)

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(PieceType.Bishop, color, position)

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(PieceType.Pawn, color, position)
    
class PieceFactory:
    @staticmethod
    def create(piece_type: PieceType, position: ChessPosition, color):
        piece = None
        if piece_type == PieceType.King:
            piece = King
        elif piece_type == PieceType.Queen:
            piece = Queen
        elif piece_type == PieceType.Pawn:
            piece = Pawn
        elif piece_type == PieceType.Rook:
            piece = Rook
        elif piece_type == PieceType.Bishop:
            piece = Bishop
        return piece(piece_type, color, position)

