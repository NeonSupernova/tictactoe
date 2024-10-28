import time
from concurrent.futures import ThreadPoolExecutor
from .tournament import RoundRobin, DoubleElimination


class TournamentManager:
    def __init__(self, game_manager, elo_system, update_rate=20):
        self.game_manager = game_manager
        self.elo_system = elo_system
        self.update_rate = update_rate  # Updates per minute

    def run_tournament(self):
        # Round-Robin Stage
        round_robin = RoundRobin(self.game_manager, self.elo_system)
        round_robin.run()

        # Double-Elimination Stage
        double_elimination = DoubleElimination(self.game_manager)
        double_elimination.run()

    def run_matches_multithreaded(self, matchups):
        with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust as needed
            futures = [executor.submit(self.game_manager.run_match, m[0], m[1]) for m in matchups]
            for future in futures:
                future.result()

    def send_updates(self):
        while True:
            time.sleep(60 / self.update_rate)  # Send updates at the specified rate
            print(f"Sending update: {self.game_manager.results}")
            # Add logic to send updates to the server