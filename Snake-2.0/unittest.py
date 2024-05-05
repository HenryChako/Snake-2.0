# test_game.py
import unittest
from game import Snake, Game, TILE_SIZE  # Now we're importing TILE_SIZE from 'game'

class TestSnakeMethods(unittest.TestCase):

    def setUp(self):
        self.snake = Snake(5, 5)

    def test_init(self):
        self.assertEqual(self.snake.head.x, 5)
        self.assertEqual(self.snake.head.y, 5)
        self.assertEqual(self.snake.velocityX, 0)
        self.assertEqual(self.snake.velocityY, 0)

class TestGameMethods(unittest.TestCase):

    def setUp(self):
        self.game = Game(None, None)  # replace None with actual window and canvas if needed

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(self.game.snake.head.x, 5 * TILE_SIZE)
        self.assertEqual(self.game.snake.head.y, 5 * TILE_SIZE)
        self.assertEqual(self.game.snake.velocityX, 0)
        self.assertEqual(self.game.snake.velocityY, 0)
        self.assertEqual(self.game.snake.body, [])
        self.assertEqual(self.game.game_over, False)
        self.assertEqual(self.game.score, 0)

if __name__ == '__main__':
    unittest.main()