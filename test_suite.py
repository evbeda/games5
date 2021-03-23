import unittest

from guess_number_game.test_guess_number_game import TestGuessNumberGame

from qwixx.test_dice import TestDice
from qwixx.test_qwixx import TestQwixx as QwixxTestQwixx
from qwixx.test_row import TestRow
from qwixx.test_score_pad import TestScorePad
from qwixx.test_set_dices import TestSetDices

from rummy_and_burakko.tests.test_board import TestBoard as RTestBoard
from rummy_and_burakko.tests.test_game import TestGame as RTestGame
from rummy_and_burakko.tests.test_player import TestPlayer as RTestPlayer
from rummy_and_burakko.tests.test_tile_bag import TestTileBag as RTestTileBag
from rummy_and_burakko.tests.test_set_tiles import TestSetTiles
from rummy_and_burakko.tests.test_tile import TestTiles

from scrabble.test.test_board import TestBoard as STestBoard
from scrabble.test.test_game import TestGame as STestGame
from scrabble.test.test_player import TestPlayer as STestPlayer
from scrabble.test.test_scrabble import TestScrabble
from scrabble.test.test_spot import TestSpot
from scrabble.test.test_tile_bag import TesttileBag as STestTileBag
from scrabble.test.test_tile import TestTile
from test_game import TestGame


def suite():
    test_suite = unittest.TestSuite()
    # General test games
    test_suite.addTest(unittest.makeSuite(TestGame))
    # guess number game
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    # qwixx
    test_suite.addTest(unittest.makeSuite(TestDice))
    test_suite.addTest(unittest.makeSuite(QwixxTestQwixx))
    test_suite.addTest(unittest.makeSuite(TestRow))
    test_suite.addTest(unittest.makeSuite(TestScorePad))
    test_suite.addTest(unittest.makeSuite(TestSetDices))
    # rummy_and_burakko
    test_suite.addTest(unittest.makeSuite(RTestBoard))
    test_suite.addTest(unittest.makeSuite(RTestGame))
    test_suite.addTest(unittest.makeSuite(RTestPlayer))
    test_suite.addTest(unittest.makeSuite(TestSetTiles))
    test_suite.addTest(unittest.makeSuite(RTestTileBag))
    test_suite.addTest(unittest.makeSuite(TestTiles))
    # scrabble
    test_suite.addTest(unittest.makeSuite(STestBoard))
    test_suite.addTest(unittest.makeSuite(STestGame))
    test_suite.addTest(unittest.makeSuite(STestPlayer))
    test_suite.addTest(unittest.makeSuite(TestScrabble))
    test_suite.addTest(unittest.makeSuite(TestSpot))
    test_suite.addTest(unittest.makeSuite(STestTileBag))
    test_suite.addTest(unittest.makeSuite(TestTile))

    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
