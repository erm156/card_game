import pytest

from card_player import Player
from tests.test_deck import cards_for_tests


def test_create_player():
  player = Player("Test Player")
  assert len(player.hand) == 0
  assert player.score == 0

def test_draw_card(cards_for_tests):
  player = Player("Test Player")
  player.draw_card(cards_for_tests.deck)
  assert len(cards_for_tests.deck) == 51
  assert len(player.hand) == 1

def test_sort_hand(cards_for_tests):
  player = Player("Test Player")
  suit_vals = cards_for_tests.suits
  suit_cards = cards_for_tests.suit_cards

  player.hand = [("9", "♥"), ("King", "♠"), ("2", "♦")]
  player.sort_hand(suit_vals, suit_cards)
  assert player.hand == [("King", "♠"), ("2", "♦"), ("9", "♥")]

def test_sort_hand_alphanumeric(cards_for_tests):
  player = Player("Test Player")
  suit_vals = dict(zip(cards_for_tests.ALPHA_SUITS, cards_for_tests.SUIT_VALS))
  suit_cards = cards_for_tests.suit_cards

  player.hand = [("9", "Hearts"), ("King", "Spades"), ("2", "Diamonds")]
  player.sort_hand(suit_vals, suit_cards)
  assert player.hand == [("King", "Spades"), ("2", "Diamonds"), ("9", "Hearts")]

def test_score_hand(cards_for_tests):
  player = Player("Test Player")
  suit_vals = cards_for_tests.suits
  suit_cards = cards_for_tests.suit_cards

  player.hand = [("9", "♥"), ("King", "♠"), ("2", "♦")]
  player.score_hand(suit_vals, suit_cards)
  assert player.score == 41

def test_score_hand_alphanumeric(cards_for_tests):
  player = Player("Test Player")
  suit_vals = dict(zip(cards_for_tests.ALPHA_SUITS, cards_for_tests.SUIT_VALS))
  suit_cards = cards_for_tests.suit_cards

  player.hand = [("9", "Hearts"), ("King", "Spades"), ("2", "Diamonds")]
  player.score_hand(suit_vals, suit_cards)
  assert player.score == 41
