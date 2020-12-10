#!/usr/bin/python3
"""Play a CLI-based two-person card game.

Using instantiations of Player and Deck classes, the game deals
hands and declares a winner based on calculated player hand values.
Players may elect to play again or exit when a game ends.
"""
from distutils.util import strtobool

from card_deck import Deck
from card_player import Player


class Game:
  """Play a card game where hand values are compared amongst players.

  Attributes:
    winner: A string ID of winning player.
    playing: A boolean indicating if a game is in progress.
  """

  def __init__(self):
    """Game constructor that initializes the card game."""
    self.winner = None
    self.playing = False

  def show_hands(self, *players):
    """Prints player hands to stdout.

    Args:
      players: Players (i.e. player objects) participating in game.
    """
    for player in players:
      print(f"\n{player.name} hand:  {player.hand}")

  def declare_winner(self, *players):
    """Prints game winner (i.e. player name) to stdout.

    Args:
      players: Players (i.e. player objects) participating in game.
    """
    player_scores = {player.name: player.score for player in players}
    self.winner = max(player_scores, key=player_scores.get)

    if self.winner is not None:
      print(f"\n****WINNER****:  {self.winner}")
    else:
      print("\nDRAW")

  def play(self, hand_size=3):
    """Starts a card game between two players.

    Args:
      hand_size: An int representing the number of cards a player will draw.
    """
    self.playing = True

    while self.playing:
      cards = Deck()
      cards.shuffle_deck()

      p1 = Player(input("\nPLAYER 1 NAME:  "))
      p2 = Player(input("\nPLAYER 2 NAME:  "))

      for _ in range(hand_size):
        p1.draw_card(cards.deck)
        p2.draw_card(cards.deck)

      p1.sort_hand(cards.suits, cards.suit_cards)
      p2.sort_hand(cards.suits, cards.suit_cards)

      p1.score_hand(cards.suits, cards.suit_cards)
      p2.score_hand(cards.suits, cards.suit_cards)

      self.show_hands(p1, p2)
      self.declare_winner(p1, p2)

      play_again = input("\nPlay again? [y/N]  ")

      if not strtobool(play_again):
        self.playing = False


if __name__ == "__main__":
  game = Game()
  game.play()
