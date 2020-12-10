"""A class for creating/representing a card player.

A player is instantiated with a score of zero and an empty hand.
Players may draw cards to create a complete hand. Player hands are
sorted and scored based on suit and card

  Usage:

  p1 = Player("PLAYER1")
  p1.draw_card(deck)

  p1.sort_hand(deck.suit_vals, deck.suit_cards)
  p1.score_hand(deck.suit_vals, deck.suit_cards)
"""


class Player:
  """Creates Player object with name, hand and score attributes.

  Attributes:
      name: A string identifier for a player.
      hand: An array of suit/value tuples.
      score: An integer representing value of a hand.
  """

  def __init__(self, name):
    """Player object constructor that initializes hand and score.

    Args:
      name: A string representing a player's ID.
    """
    self.name = name
    self.hand = []
    self.score = 0

  def draw_card(self, deck):
    """Pops first element of deck array and appends it to player hand.

    Args:
      name: A string representing a player's ID.
    """
    try:
      self.hand.append(deck.pop(0))
    except IndexError:
      print("NO CARDS LEFT!")

  def sort_hand(self, suit_vals, card_vals):
    """Sorts player hand based on suit and card value mappings.

    Performs sorting by suit (primary) and suit card (secondary).

    Args:
      suit_vals: A dict mapping card suits to their point values.
      card_vals: A dict mapping suit cards to their point values.
    """
    self.hand.sort(key=lambda x: (suit_vals[x[1]], card_vals[x[0]]))

  def score_hand(self, suit_vals, card_vals):
    """Scores player hand based on suit and card value mappings.

    Updates player score attribute with value of scored hand.

    Args:
      suit_vals: A dict mapping suits to their point values.
      card_vals: A dict mapping suit cards to their point values.
    """
    self.score = sum(
        [card_vals[card[0]] * suit_vals[card[1]] for card in self.hand]
    )
