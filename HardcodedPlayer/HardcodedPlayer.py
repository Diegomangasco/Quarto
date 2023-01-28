import quarto
import random
from .utils import *

# This agent uses the functions from utils.py file for choosing and placing a piece
class HardcodedPlayer(quarto.Player):
    """Hardcoded player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)
        self._functions = HardcodedFunctions()
    
    def choose_piece(self) -> int:
        return self._functions.find_piece(self.get_game())

    # I return the inverted (x, y) representation since in the game, the two coordinates
    # are passed to the function 'place' and the piece is palced in the inverted coordinates (y, x)
    # I want that my function results will be coherent with the real board that I checked
    def place_piece(self) -> tuple[int, int]:
        place = self._functions.find_position(self.get_game())
        return place[1], place [0]