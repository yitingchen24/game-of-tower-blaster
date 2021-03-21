from tower_blaster import *

import unittest

class Test_tower_blaster(unittest.TestCase):

    def test_setup_bricks(self):

        # create main pile and discard pile using setup_bricks
        main_pile, discard_pile = setup_bricks()

        #manually create test main pile and test discard pile to compare with
        test_main_pile = [i for i in range(1, 61)]
        test_discard_pile = []

        #check that main_pile and discard_pile have the correct bricks, in order
        self.assertListEqual(test_main_pile, main_pile)
        self.assertListEqual(test_discard_pile, discard_pile)

    def test_shuffle(self):

        # manually create test main pile and test discard pile
        main_pile = [i for i in range(1, 61)]
        discard_pile = []

        #create test main pile and test discard pile by getting copies
        test_main_pile = main_pile.copy()
        test_discard_pile = discard_pile.copy()

        #shuffle main pile and discard pile using shuffle_bricks
        shuffle_bricks(main_pile)
        shuffle_bricks(discard_pile)

        #check lengths of main pile and discard pile
        self.assertTrue(len(main_pile) == 60)
        self.assertTrue(len(discard_pile) == 0)

        #check that main pile and discard pile still contain the same values, regardless of order
        self.assertCountEqual(test_main_pile, main_pile)
        self.assertCountEqual(test_discard_pile, discard_pile)
        
    def test_check_bricks(self):

        # manually create test main pile and test discard pile
        main_pile = [i for i in range(1, 61)]
        discard_pile = []

        #call check_bricks
        check_bricks(main_pile, discard_pile)

        #check that main pile and discard pile are the same
        self.assertTrue(len(main_pile) == 60)
        self.assertTrue(len(discard_pile) == 0)

        #test main_pile with 1 brick
        main_pile = [60]
        discard_pile = [i for i in range(1, 60)]
        self.assertEqual(len(main_pile), 1)
        self.assertEqual(len(discard_pile), 59)
        check_bricks(main_pile, discard_pile)
        self.assertEqual(len(main_pile), 1)
        self.assertEqual(len(discard_pile), 59)

        #test empty main_pile
        main_pile = []
        discard_pile = [i for i in range(1, 61)]
        self.assertEqual(len(main_pile), 0)
        self.assertEqual(len(discard_pile), 60)
        check_bricks(main_pile, discard_pile)
        self.assertEqual(len(main_pile), 59)
        self.assertEqual(len(discard_pile), 1)

    def test_check_tower_blaster(self):

        #test stable tower
        tower = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(check_tower_blaster(tower))

        #test unstable tower
        tower = [1, 11, 20, 33, 45, 41, 47, 50, 57, 59]
        self.assertFalse(check_tower_blaster(tower))

        #test unstable tower
        tower = [1, 11, 20, 33, 45, 41, 47, 50, 57, 59]
        self.assertFalse(check_tower_blaster(tower))

        #test unstable tower
        tower = [1, 11, 20, 33, 45, 41, 47, 50, 57, 59]
        self.assertFalse(check_tower_blaster(tower))

    def test_get_top_brick(self):
        
        # manually create main pile of bricks
        main_pile = [i for i in range(60, 0, -1)]
        self.assertEqual(len(main_pile), 60)

        #check that top brick of main pile is 60
        self.assertEqual(60, get_top_brick(main_pile))

        #check that main pile was updated, after getting top brick
        new_main_pile = [i for i in range(59, 0, -1)]
        self.assertListEqual(new_main_pile, main_pile)

        #check that top brick of discard pile is 3
        discard_pile = [3, 4, 1]
        self.assertEqual(len(discard_pile), 3)
        self.assertEqual(3, get_top_brick(discard_pile))

        #discard pile should be updated, after getting top brick
        new_discard_pile = [4, 1]
        self.assertListEqual(new_discard_pile, discard_pile)

    def test_deal_initial_bricks(self):

        # manually create test main pile and test discard pile
        main_pile = [i for i in range(1, 61)]
        discard_pile = []

        #shuffle bricks using shuffle_bricks
        shuffle_bricks(main_pile)

        #check size of main_pile
        self.assertTrue(len(main_pile) == 60)

        #deal bricks using deal_initial_bricks
        computer_bricks, user_bricks = deal_initial_bricks(main_pile)

        #check that computer has 10 bricks
        self.assertTrue(len(computer_bricks) == 10)

        #check that user has 10 bricks
        self.assertTrue(len(user_bricks) == 10)

        #check that main pile has 40 bricks left
        self.assertTrue(len(main_pile) == 40)

        #check that bricks in computer_bricks are no longer in main_pile
        for i in computer_bricks:
            self.assertNotIn(i, main_pile)

        #bricks in user_bricks should no longer be in main_pile
        for i in user_bricks:
            self.assertNotIn(i, main_pile)

    def test_add_brick_to_discard(self):

        #manually create test discard pile
        discard_pile = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
        self.assertEqual(len(discard_pile), 10)

        #add specific brick to top of discard
        add_brick_to_discard(20, discard_pile)

        #test new length of discard
        self.assertEqual(len(discard_pile), 11)

        #should have added brick to top of discard (0 index in list)
        top_discard = discard_pile[0]
        self.assertEqual(20, top_discard)

    def test_find_and_replace(self):

        #manually create test tower pile
        tower = [18, 9, 20, 1, 7, 42, 39, 38, 51, 45]
        new_brick = 30
        brick_to_be_replaced = 39

        # manually create test discard pile
        discard = []

        #find and replace brick_to_be_replaced with new_brick
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)

        #create new tower and new discard pile to compare with
        new_tower = [18, 9, 20, 1, 7, 42, 30, 38, 51, 45]
        new_discard = [39]

        #check that brick was replaced and placed on discard
        self.assertListEqual(new_tower, tower)
        self.assertListEqual(new_discard, discard)

        # update 2
        new_brick = 2
        brick_to_be_replaced = 9
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)

        new_tower = [18, 2, 20, 1, 7, 42, 30, 38, 51, 45]
        new_discard = [9, 39]

        self.assertListEqual(new_tower, tower)
        self.assertListEqual(new_discard, discard)

        # update 3
        new_brick = 60
        brick_to_be_replaced = 27
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)

        new_tower = [18, 2, 20, 1, 7, 42, 30, 38, 51, 45]
        new_discard = [9, 39]

        self.assertListEqual(new_tower, tower)
        self.assertListEqual(new_discard, discard)

        # update 4
        new_brick = 43
        brick_to_be_replaced = 7
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)

        new_tower = [18, 2, 20, 1, 43, 42, 30, 38, 51, 45]
        new_discard = [7, 9, 39]

        self.assertListEqual(new_tower, tower)
        self.assertListEqual(new_discard, discard)

if __name__ == '__main__':
    unittest.main()

