class Board:
    row: [[bool | None]]
    col: [[bool | None]]
    diagonal_top_left: [[bool | None]]
    diagonal_top_right: [[bool | None]]

    def __init__(self, board: [[bool | None]]):
        self.row = board

    def wide_to_long(self):
        if self.row:
            self.col = [[] for i in range(7)]
            i = 0
            while i < len(self.row):
                j = 0
                while j < len(self.row[i]):
                    self.col[j].append(self.row[i][j])
                    j += 1
                i += 1
        print(self.col)

    def wide_to_diagonal_top_right(self):
        if self.row:
            self.diagonal_top_right = [[] for i in range(12)]
            self.diagonal_top_left = [[] for i in range(12)]
            i = 0
            while i < len(self.row):
                j = 0
                while j < len(self.row[i]):
                    self.diagonal_top_right[5 - i + j].append(self.row[i][j])
                    self.diagonal_top_left[5 - i + j].append(self.row[5 - i][j])
                    j += 1
                i += 1
        print(self.diagonal_top_right)
        print(self.diagonal_top_left)

board = [[False, False, True, False, None, True, True],
         [True, False, True, False, None, True, True],
         [True, False, True, False, None, True, True],
         [True, False, True, False, None, True, True],
         [False, False, True, False, None, True, True],
         [False, None, True, False, None, True, True]]

a = Board(board)
a.wide_to_diagonal_top_right()
