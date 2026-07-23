from deck import Deck

class Game: 
    def __init__(self): 
        self.deck = Deck()
        self.players = []

    def deal_cards(self, num_cards=7):
        # loop through each player and deal them the specified number of cards
        pass

    def create_discard_pile(self):
        # create a discard pile and place the first card from the deck into it to begin pile
        pass

    def determine_first_player(self):
        # Choose a player to go first
        pass

    def player_start_turn(self, player):
        # Begin the player's turn
        pass

    def draw_card_for_player(self, player):
        # Draw a card for the specified player, if player does not have a playable card
        pass

    def player_play_card(self, player, card):
        # Play the selected card by moving it from the player's hand to the discard pile & apply any card effects
        pass

    def next_player_turn(self):
        # Move to the next player's turn based on the current direction of play
        pass

    def skip_player_turn(self, player):
        # Skip the specified player's turn
        pass

    def reverse_player_order(self):
        # Reverse the order of play
        pass

    def draw_two_cards(self, player):
        # Draw two cards for the specified player
        pass

    def apply_wild(self, player):
        # Allow the specified player to choose a color for the next turn
        pass

    def apply_wild_draw_four(self, player):
        # Draw four cards for the specified player and skip their turn
        pass

    def check_for_winner(self):
        # Check if any player has won the game by having no cards left in their hand
        pass

    



       






       