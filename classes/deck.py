from card import Card
import random

class Deck:
    # Stores all cards
    def __init__(self):
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        card_color = ["Red", "Blue", "Green", "Yellow"]
    
        # Create Zero Cards
        for color in card_color:
            self.cards.append(Card(color, "0"))

        # Create cards 1-9
        for value in range(1, 10):
            


