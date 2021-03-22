import unittest
from guess_number_game.guess_number_game import GuessNumberGame


class TestGuessNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = GuessNumberGame()
        self.game._guess_number = 50

    def test_initial_status(self):
        self.assertTrue(self.game.is_playing)

    def _test_play(self, number, expected_result, expected_is_playing):
        self.assertEqual(self.game.play(number), expected_result)
        self.assertEqual(self.game.is_playing, expected_is_playing)

    def test_play_lower(self):
        self._test_play(10, 'too low', True)

    def test_play_higher(self):
        self._test_play(80, 'too high', True)

    def test_play_equal(self):
        self._test_play(50, 'you win', False)

    def test_initial_next_turn(self):
        self.assertEqual(
            self.game.next_turn(),
            'Give me a number from 0 to 100',
        )

    def _test_next_turn(self, number, expected_message):
        self.game.play(number)
        self.assertEqual(
            self.game.next_turn(),
            expected_message,
        )

    def test_next_turn_after_play(self):
        self._test_next_turn(10, 'Give me a number from 0 to 100')

    def test_next_turn_after_win(self):
        self._test_next_turn(50, 'Game Over')

    def test_get_board(self):
        self.assertEqual(
            self.game.board,
            '[]'
        )
        self.game.play(10)
        self.assertEqual(
            self.game.board,
            '[10]'
        )


if __name__ == "__main__":
    unittest.main()
