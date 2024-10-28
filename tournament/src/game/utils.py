import os
from enum import Enum


def calculate_elo(winner_elo, loser_elo, k_factor=32):
    """
    Calculate the new Elo ratings for a match.

    :param winner_elo: The Elo rating of the winner.
    :param loser_elo: The Elo rating of the loser.
    :param k_factor: The K-factor for the Elo calculation. Defaults to 32.
    :type winner_elo: int
    :type loser_elo: int
    :type k_factor: int
    :return: The new Elo ratings for the winner and loser.
    """
    expected_winner = 1 / (1 + 10 ** ((loser_elo - winner_elo) / 400))
    new_winner_elo = winner_elo + k_factor * (1 - expected_winner)
    new_loser_elo = loser_elo - k_factor * (1 - expected_winner)
    return new_winner_elo, new_loser_elo


def ls_exec(directory):
    """
    List bot folders in a given directory.

    :param directory: The directory to list bots from.
    :type directory: str
    :return: A list of bot folders in the given directory.
    :rtype: list
    """
    bot_folders = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            bot_folders.append(entry)
    return bot_folders


class Tokens(Enum):
    X = "X"
    O = "O"
    EMPTY = "E"
