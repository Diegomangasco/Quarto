import quarto

class GAPlayer(quarto.Player):
    '''Defines a Genetic Algorithm player'''

    def __init__(self, quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return super().choose_piece()

    def place_piece(self) -> tuple[int, int]:
        return super().place_piece()