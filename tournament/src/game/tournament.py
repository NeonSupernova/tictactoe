from .game_manager import GameManager
from .utils import calculate_elo

class Tournament:
    def __init__(self, game_manager: GameManager, matches=1000):
        self.gm = game_manager
        self.matches = matches
        self.results = {}

    def play_set(self, bot1_idx: int, bot2_idx: int):
        set_results = []
        for i in range(self.matches):
            res = self.gm.play_match(bot1_idx, bot2_idx)
            set_results.append(res)
        return set_results

    def run(self):
        """
        Run the tournament.

        This will run each match the specified number of times, and store the results in the
        ``results`` dictionary.

        :return: The results dictionary, where the keys are tuples of (bot1_idx, bot2_idx) and the
            values are dictionaries with the keys "bot1_wins" and "bot2_wins" and the number of wins
            for each bot.
        """
        pass




class RoundRobin(Tournament):
    def run(self):
        bots = self.gm.bots
        for i in range(len(bots)):
            for j in range(i + 1, len(bots)):
                winner_idx = self.play_set(i, j)
                if winner_idx == i:
                    bots[i].elo, bots[j].elo = calculate_elo(bots[i].elo, bots[j].elo)
                    self.results.update({(i, j): {"bot1_wins": 1, "bot2_wins": 0}})
                else:
                    bots[j].elo, bots[i].elo = calculate_elo(bots[j].elo, bots[i].elo)
                    self.results.update({(i, j): {"bot1_wins": 0, "bot2_wins": 1}})



class DoubleElimination(Tournament):
    def pair_bots(self):
        # Sort bots by Elo for pairing
        return [(i, i + 1) for i in range(0, len(self.gm.bots), 2)]

    def run(self):
        # Run double elimination rounds
        matchups = self.pair_bots()
        for _ in range(2):  # Winner and loser's bracket
            for bot1_idx, bot2_idx in matchups:
                self.gm.play_match(bot1_idx, bot2_idx)
            matchups = self.pair_bots()
