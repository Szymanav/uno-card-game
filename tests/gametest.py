import unittest
from classes.game import Game
from classes.player import Player
from classes.card import Card


class TestGame(unittest.TestCase):

    def test_game_creation(self):
        game = Game()

        self.assertEqual(len(game.players), 0)
        self.assertEqual(game.deck.track_remaining(), 108)

    def test_deal_cards(self):
        game = Game()

        game.players.append(Player("Player1"))
        game.players.append(Player("Player2"))

        game.deal_cards()

        self.assertEqual(len(game.players[0].hand), 7)
        self.assertEqual(len(game.players[1].hand), 7)
        self.assertEqual(game.deck.track_remaining(), 94)

    def test_create_discard_pile(self):
        game = Game()

        game.create_discard_pile()

        self.assertEqual(len(game.discard_pile), 1)

    def test_determine_first_player(self):
        game = Game()

        game.players.append(Player("Player1"))
        game.players.append(Player("Player2"))

        game.determine_first_player()

        self.assertIn(game.current_player, game.players)

    def test_draw_card_for_player(self):
        game = Game()

        player = Player("Player1")
        game.players.append(player)

        game.draw_card_for_player(player)

        self.assertEqual(len(player.hand), 1)

    def test_player_play_card(self):
        game = Game()

        player = Player("Player1")
        card = Card("Red", "5")

        player.add_card(card)
        game.players.append(player)

        game.player_play_card(player, card)

        self.assertEqual(len(player.hand), 0)
        self.assertEqual(game.discard_pile[-1], card)

    def test_next_player_turn(self):
        game = Game()

        game.players.append(Player("Player1"))
        game.players.append(Player("Player2"))

        game.current_player = 0

        game.next_player_turn()

        self.assertEqual(game.current_player, 1)

    def test_skip_player_turn(self):
        game = Game()

        game.players.append(Player("Player1"))
        game.players.append(Player("Player2"))
        game.players.append(Player("Player3"))

        game.current_player = 0

        game.skip_player_turn(game.players[1])

        self.assertEqual(game.current_player, 2)

    def test_reverse_player_order(self):
        game = Game()

        game.direction = 1

        game.reverse_player_order()

        self.assertEqual(game.direction, -1)

    def test_draw_two_cards(self):
        game = Game()

        player = Player("Player1")

        game.draw_two_cards(player)

        self.assertEqual(len(player.hand), 2)

    def test_apply_wild(self):
        game = Game()

        player = Player("Player1")

        game.apply_wild(player)

        self.assertIn(game.current_color,
                      ["Red", "Blue", "Green", "Yellow"])

    def test_apply_wild_draw_four(self):
        game = Game()

        player = Player("Player1")

        game.apply_wild_draw_four(player)

        self.assertEqual(len(player.hand), 4)

    def test_check_for_winner(self):
        game = Game()

        winner = Player("Player1")
        game.players.append(winner)

        self.assertEqual(game.check_for_winner(), winner)