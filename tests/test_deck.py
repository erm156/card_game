from copy import deepcopy

import pytest

from card_deck import Deck


@pytest.fixture
def cards_for_tests():
  cards = Deck()
  return cards

def test_construct_deck(cards_for_tests):
  assert len(cards_for_tests.deck) == 52

def test_shuffle_deck(cards_for_tests):
  unshuffled = deepcopy(cards_for_tests.deck)
  cards_for_tests.shuffle_deck()
  assert unshuffled != cards_for_tests.deck

def test_deck_cards(cards_for_tests):
  for card in cards_for_tests.deck:
    assert isinstance(card, tuple)
    assert len(card) == 2
    assert isinstance(card[0], str)
    assert isinstance(card[1], str)
