import unittest
from classes.player import Player
from classes.card import Card


class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player("Player1")

        self.assertEqual(player.name, "Player1")
        self.assertEqual(player.hand, [])

    def test_add_card(self):
        player = Player("Player1")
        card = Card("Red", "5")

        player.add_card(card)

        self.assertEqual(len(player.hand), 1)

    def test_remove_card(self):
        player = Player("Player1")
        card = Card("Red", "5")

        player.add_card(card)
        player.remove_card(card)

        self.assertEqual(len(player.hand), 0)

    def test_has_won_after_playing_last_card(self):
        player = Player("Player1")
        card = Card("Red", "5")

        player.add_card(card)
        player.remove_card(card)

        self.assertTrue(player.has_won())

    def test_has_won_false(self):
        player = Player("Player1")
        player.add_card(Card("Blue", "2"))

        self.assertFalse(player.has_won())