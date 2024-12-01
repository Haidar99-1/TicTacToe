import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_empty_board(self):
        board = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]
        game = TicTacToe(board)
        print("No winner board is empty")
        self.assertIsNone(game.checkWinner()) 

            
    def test_winner_horizontal(self):
        board = [
            ['X', 'X', 'X', 'X'],
            ['O', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['O', 'O', 'X', 'O']
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 'X') 

    def test_winner_vertical(self):
        board = [
            ['X', 'O', 'X', 'O'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'O'],
            ['X', 'O', 'X', 'O']
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 'X')

    def test_winner_diagonal(self):
        board = [
            ['X', 'O', 'O', 'X'],
            ['O', 'X', 'O', 'O'],
            ['O', 'O', 'X', 'O'],
            ['X', 'O', 'O', 'X']
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 'X')

    def test_winner_2x2_box(self):
        board = [
            ['X', 'O', 'O', 'X'],
            ['O', 'X', 'X', 'O'],
            ['X', 'X', 'X', 'O'],
            ['O', 'O', 'X', 'O']
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 'X')  

    def test_winner_all_corners(self):
        board = [
            ['X', 'O', 'O', 'X'],
            ['O', ' ', 'O', 'O'],
            ['O', ' ', ' ', 'O'],
            ['X', 'O', 'O', 'X']
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 'X')  

    def test_no_winner(self):
        board = [
            ['X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['O', 'X', 'X', 'O']
        ]
        game = TicTacToe(board)
        self.assertIsNone(game.checkWinner())  
    
    def test_winner_o(self):
        board = [
            ['O', 'O', 'O', 'O'],
            ['X', 'X', 'X', 'O'],
            ['X', 'X', 'X', 'O'],
            ['O', 'O', 'O', 'X']
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 'O') 
        
    def test_any_moves_left(self):
        board_with_moves_left = [
            ['X', 'O', 'X', 'O'],
            ['O', 'X', 'O', ' '],
            ['X', 'X', 'O', 'O'],
            ['O', 'O', 'X', 'X']
        ]
        game = TicTacToe(board_with_moves_left)
        self.assertTrue(game.anyMovesLeft())  
        
    def test_is_game_over(self):
        board_winner_horizontal = [
            ['X', 'X', 'X', 'X'],
            ['O', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['O', 'O', 'X', 'O']
        ]
        game = TicTacToe(board_winner_horizontal)
        self.assertTrue(game.isGameOver()) 
        
if __name__ == "__main__":
    unittest.main()
