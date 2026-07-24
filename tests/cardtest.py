import unittest
from classes.card import Card


class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card("Red", "5")

        self.assertEqual(card.color, "Red")
        self.assertEqual(card.value, "5")

    def test_card_string(self):
        card = Card("Blue", "Skip")

        self.assertEqual(str(card), "Blue Skip")
