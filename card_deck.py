"""A class for creating/representing a standard deck of playing cards.

Contains functions for constructing a 52-card deck and performing
in-place shuffling of cards.

  Usage:

  cards = Deck()
  cards.shuffle_deck()
"""
import sys

from itertools import product
from random import shuffle


class Deck:
  """Constructs 52 card deck as array of suit/value tuples.

  Attributes:
      deck: An array of suit/value tuples representing cards.
      suits: A dict of suit types and their respective values.
      suit_cards: A dict of suit cards and their values.
      UNICODE_SUITS: A tuple containing unicode suit symbols
      ALPHA_SUITS: A tuple containing alphanumeric suit names.
      SUIT_VALS: A tuple of suit point values.
      UNICODE_SUPPORT: A boolean indicating if stdout supports unicode.
  """

  UNICODE_SUITS = ("♣", "♥", "♦", "♠")
  ALPHA_SUITS = ("Clubs", "Hearts", "Diamonds", "Spades")
  SUIT_VALS = (4, 3, 2, 1)
  UNICODE_SUPPORT = sys.stdout.encoding.lower().startswith("utf")

  def __init__(self):
    """Deck object constructor that checks for stdout unicode support."""
    if self.UNICODE_SUPPORT:
      self.suits = dict(zip(self.UNICODE_SUITS, self.SUIT_VALS))
    else:
      self.suits = dict(zip(self.ALPHA_SUITS, self.SUIT_VALS))

    self.suit_cards = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11,
    }
    self.deck = self.construct_deck()

  def construct_deck(self):
    """Creates array of card/suit tuples via Cartesian product."""
    return list(card for card in product(self.suit_cards, self.suits))

  def shuffle_deck(self):
    """Performs in-place shuffling of values in deck array."""
    shuffle(self.deck)
