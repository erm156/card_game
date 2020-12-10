import pytest

from card_game import Game


def test_playing(monkeypatch):
  # patch input function to handle player names and avoid infinite loop
  monkeypatch.setattr("builtins.input", lambda _: "n")

  game = Game()
  assert game.winner is None
  assert game.playing is False

  game.play()
  assert game.winner is not None
