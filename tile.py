

class Tile:
    # multipliers
    DOUBLE_LETTER = '2'
    TRIPLE_LETTER = '3'
    DOUBLE_WORD   = '8'
    TRIPLE_WORD   = '9'

    def __init__(self):
        self.letter          = ''
        self.letter_value    = ''
        self.tile_multiplier = ''
        self.tile_value      = ''
        self.word_multiplier = ''

    def get_letter_pts(l):
        """ Return point value for each letter (no bonuses)"""
        letter_points = {'A': 1, 'B': 4, 'C': 4, 'D': 2, 'E': 1,
                         'F': 4, 'G': 3, 'H': 4, 'I': 1, 'J': 10,
                         'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
                         'P': 4, 'Q': 10,'R': 1, 'S': 1, 'T': 1,
                         'U': 2, 'V': 4, 'W': 4, 'X': 8,  'Y': 4, 'Z': 8}
        return letter_points[l]