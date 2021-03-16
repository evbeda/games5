import unittest

from guess_number_game.test_guess_number_game import TestGuessNumberGame

from qwixx.test_die import TestDie
from qwixx.test_game import TestGame
from qwixx.test_row import TestRow
from qwixx.test_score_pad import TestScorePad

from rummy_and_burakko.tests.test_tile import TestTiles
from rummy_and_burakko.tests.test_set_tiles import TestSetTiles

from scrabble.test.test_board import TestBoard
from scrabble.test.test_player import TestPlayer
# from scrabble.test.test_spot
from scrabble.test.test_tile import TestTile


def suite():
    test_suite = unittest.TestSuite()
    # guess number game
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    # qwixx
    test_suite.addTest(unittest.makeSuite(TestDie))
    test_suite.addTest(unittest.makeSuite(TestGame))
    test_suite.addTest(unittest.makeSuite(TestRow))
    test_suite.addTest(unittest.makeSuite(TestScorePad))
    # rummy_and_burakko
    test_suite.addTest(unittest.makeSuite(TestTiles))
    test_suite.addTest(unittest.makeSuite(TestSetTiles))

    # scrabble
    test_suite.addTest(unittest.makeSuite(TestBoard))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestTile))

    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
