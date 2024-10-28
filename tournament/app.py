#from example_submission.bot import main

from src.game import GameManager, Board, Tokens


if __name__ == '__main__':
    gm = GameManager()
    #bot_directory = "./bots"

    gm.register("/Users/novapy/PycharmProjects/tictactoeEnv/example_submission")
    gm.register("/Users/novapy/PycharmProjects/tictactoeEnv/example_submission")
    board = Board()
    bot = gm.bots[0]
    bot.start()

    for i in range(9):
        board.display()
        move = bot.make_move(Tokens.O, board)
        board.update(move)
        move = bot.make_move(Tokens.X, board)
        board.update(move)

    board.display()


