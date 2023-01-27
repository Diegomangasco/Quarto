import quarto
import random
from .utils import *

class HardcodedPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)
        self._functions = HardcodedFunctions()
    
    def choose_piece(self) -> int:
        return self._functions.find_piece(self.get_game())

    def place_piece(self) -> tuple[int, int]:
        place = self._functions.find_position(self.get_game())
        return place[1], place [0]