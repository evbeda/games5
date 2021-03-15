import unittest
from tests import test_tile
from tests import test_set_tiles
# from tests import test_board
# from tests import test_game


def create_suite(module):
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    return suite


def create_suite_pack():
    suite_list = []
    suite_list.append(create_suite(test_tile))
    suite_list.append(create_suite(test_set_tiles))
    # suite_list.append(create_suite(test_board))
    # suite_list.append(create_suite(test_game))
    return suite_list


if __name__ == '__main__':
    suite_pack = unittest.TestSuite(create_suite_pack())

    runner = unittest.TextTestRunner(descriptions=True, verbosity=3)
    runner.run(suite_pack)
