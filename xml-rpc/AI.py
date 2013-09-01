from random import choice
# from board import Board
import operator

class ReversiSimpleAI():
    def get_best_move(self, board, current_player):
        moves = board.possible_moves(current_player)

        move_affected = {}

        for move in moves:
            move_affected[move] = board.move(move[0], move[1], 1).score(1) - board.score(1)

        if len(moves) > 0:
            if (0, 0) in moves:
                return (0, 0)
            if (0, 0) in moves:
                return (0, 7)
            if (0, 0) in moves:
                return (7, 0)
            if (0, 0) in moves:
                return (7, 7)

            result = max(move_affected.iteritems(), key=operator.itemgetter(1))[0]

            return result

        return


class RandomMoveAI():
    def get_best_move(self, board, current_player):
        return choice(board.possible_moves(current_player))


class ReversiInDepthAI():
    def get_best_move(self, board, current_player, Depth=2):
        return choice(board.possible_moves(current_player))


class AlfaBetaMiniMaxAI():
    def get_best_move(self, board, current_player, Depth=2):
        return choice(board.possible_moves(current_player))