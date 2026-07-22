from card import Card
import random

class Deck:
    # Stores all cards
    def __init__(self):
        self.cards = []
        self.create_deck()

        # Shuffle Cards
        random.shuffle(self.cards)
    
    def create_deck(self):
        card_color = ["Red", "Blue", "Green", "Yellow"]
        actions = ["Skip", "Reverse", "Draw Two"]
        wild_cards = ["Regular Wild", "Wild Draw Four"]
    
        # Create Zero Cards
        for color in card_color:
            self.cards.append(Card(color, "0"))

            # Create cards 1-9, two for each color
            for value in range(1, 10):
                self.cards.append(Card(color, str(value)))
                self.cards.append(Card(color, str(value)))
        
            # Create two of each action card per color
            for action in actions:
                self.cards.append(Card(color, action))
                self.cards.append(Card(color, action))
            
        # Creates Wild Cards
        for wild in wild_cards:
            for wild_copy in range(4):
                self.cards.append(Card(None, wild))
                





