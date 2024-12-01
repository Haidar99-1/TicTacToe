class TicTacToe:
    def __init__(self, board):
        """
        Each cell contains 'X', 'O', or ' ' (space for empty).
        """
        self.board = board

    def checkWinner(self):
        winner = self.check_rows_and_columns()
        if winner:
            return winner

        winner = self.check_diagonals()
        if winner:
            return winner

        winner = self.check_2x2_boxes()
        if winner:
            return winner

        winner = self.check_four_corners()
        if winner:
            return winner

        print("No winner found")
        return None

    def check_rows_and_columns(self):
        for i in range(4):
            # Check row
            if self.board[i][0] != ' ' and all(self.board[i][j] == self.board[i][0] for j in range(4)):
                print(f"Row win: {i}")
                return self.board[i][0]
            
            # Check column
            if self.board[0][i] != ' ' and all(self.board[j][i] == self.board[0][i] for j in range(4)):
                print(f"Column win: {i}")
                return self.board[0][i]
        return None

    def check_diagonals(self):
        if self.board[0][0] != ' ' and all(self.board[i][i] == self.board[0][0] for i in range(4)):
            print("Main diagonal win")
            return self.board[0][0]
        if self.board[0][3] != ' ' and all(self.board[i][3 - i] == self.board[0][3] for i in range(4)):
            print("Anti-diagonal win")
            return self.board[0][3]
        return None

    def check_2x2_boxes(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i][j + 1] == self.board[i + 1][j] == self.board[i + 1][j + 1]:
                    print(f"2x2 box win at ({i}, {j})")
                    return self.board[i][j]
        return None

    def check_four_corners(self):
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[0][3] == self.board[3][0] == self.board[3][3]:
            print("Four corners win")
            return self.board[0][0]
        return None


    def anyMovesLeft(self):
        return any(cell == ' ' for row in self.board for cell in row)

    def isGameOver(self):
        return self.checkWinner() is not None or not self.anyMovesLeft()
