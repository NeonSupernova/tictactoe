from collections import namedtuple
from pydoc import plain

from .bot import Bot
from .board import Board
from .utils import Tokens
from random import choice

BotWrapper = namedtuple("BotWrapper", ["bot", "symbol"])

class GameManager:
    def __init__(self):
        """ Initialize the GameManager with registered bots. """
        self.bots = []
        self.results = None

    def register(self, bot_folder: str):
        """ Register a bot for the competition. """
        bot = Bot(bot_folder)
        self.bots.append(bot)

    def play_match(self, bot1: int, bot2: int):
        """ Play a match between two bots. """
        board = Board()
        bot1 = BotWrapper(self.bots[bot1], choice([Tokens.X, Tokens.O]))
        bot2 = BotWrapper(
            self.bots[bot2], Tokens.O if bot1.symbol == Tokens.X else Tokens.X
        )

        players = [bot1, bot2]

        for bot_wrap in players:
            bot_wrap.bot.start()

        turn = 0
        while not board.is_full:
            current_bot = players[turn % 2]

            board.display()
            print(f"Player {current_bot.symbol.value}'s turn")

            try:
                move = current_bot.bot.make_move(current_bot.symbol, board)
                print(move) # FIXME
                if board.is_valid_move(move):
                    board.place_move(move)
                else:
                    print(f"Invalid move by {current_bot.bot.bot_folder}. {current_bot.symbol.value} loses!")
                    return
            except Exception as e:
                print(f"Error during {current_bot.symbol.value}'s turn: {e}")
                return

            if board.is_winner(current_bot.bot.__doc__):
                board.display()
                print(f"{current_bot.symbol.value} wins!")
                return

            turn += 1

        board.display()
        print("It's a draw!")
        for bot_wrap in players:
            bot_wrap.bot.stop()

