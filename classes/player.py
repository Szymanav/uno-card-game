class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def show_hand(self):
        for card in self.hand:
            print(card)

    def has_won(self):
        return len(self.hand) == 0


    
