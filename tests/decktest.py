import unittest
from classes.deck import Deck
from classes.card import Card


class TestDeck(unittest.TestCase):

    def test_deck_creation(self):
        deck = Deck()

        self.assertEqual(len(deck.cards), 108)

    def test_draw_card(self):
        deck = Deck()

        card = deck.draw_card()

        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 107)

    def test_track_deck_amount(self):
        deck = Deck()

        self.assertEqual(deck.track_remaining(), 108)

        deck.draw_card()

        self.assertEqual(deck.track_remaining(), 107)

    def test_draw_empty_deck(self):
        deck = Deck()

        deck.cards = []

        self.assertIsNone(deck.draw_card())