from random import choice


class ReversiSimpleAI():
    def get_best_move(self, board, current_player):
        moves = board.possible_moves(current_player)
        if len(moves) > 0:
            return board.possible_moves(current_player)[0]
        return


class RandomMoveAI():
    def get_best_move(self, board, current_player):
        return choice(board.possible_moves(current_player))


class ReversiInDepthAI():
    def get_best_move(self, board, current_player, Depth=2):
        return choice(board.possible_moves(current_player))
