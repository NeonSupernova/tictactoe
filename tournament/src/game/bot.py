import os
import subprocess
import tomllib
from .board import Board
from .utils import Tokens

class Bot:
    def __init__(self, bot_folder: str, elo=500):
        """ Initialize the bot with its folder path and configuration. """
        self.bot_folder = bot_folder
        self.bot_config = self.load_config()
        self.process = None
        self.elo = elo
        self.__doc__ = self.load_readme()

    def load_config(self):
        """ Load the bot's configuration from its toml file. """
        config_path = os.path.join(self.bot_folder, "config.toml")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found for bot: {self.bot_folder}")
        with open(config_path, 'rb') as fp:
            return tomllib.load(fp)

    def load_readme(self):
        """ Load the bot's README into a docstring if it exists. """
        readme_path = os.path.join(self.bot_folder, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                return f.read()
        return ""

    def start(self):
        """ Start the bot's subprocess using the 'run' command from its config. """
        run_command = self.bot_config['bot']['run'].split()
        self.process = subprocess.Popen(
            run_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            cwd=self.bot_folder  # Ensure subprocess runs in the correct directory
        )

    def make_move(self, symbol: Tokens, board: "Board") -> int:
        """ Send the board state to the bot and retrieve its move. """
        if not self.process:
            raise Exception(f"Bot {self.bot_folder} is not started.")

        # Send board state to bot
        self.process.stdin.write(f"{symbol.value}{board.board_state}\n")
        self.process.stdin.flush()

        # Get the move from bot
        move = self.process.stdout.readline().strip()
        return move

    def stop(self):
        """ Terminate the bot's subprocess. """
        if self.process:
            self.process.terminate()
            self.process = None

