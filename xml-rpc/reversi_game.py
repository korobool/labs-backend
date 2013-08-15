from pprint import pprint

from board import Board
from AI import RandomMoveAI
import uuid
import pymongo

initial_state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]


class ServerClass():
    def __init__(self):
        self._conn = pymongo.Connection('localhost', 27017)
        pass

    def start_game(self, user):
        id = uuid.uuid4()
        reversi = self._conn.reversi
        games = reversi.games
        games.insert({'game': str(id), 'board': initial_state, 'state': 'in_progress', 'user': user, 'moves': []})

        return str(id)

    def get_board_state(self, game_id):
        reversi = self._conn.reversi
        games = reversi.games
        game = games.find_one({"game": game_id})
        return game[u'board']

    def move(self, r, c, game_id):
        reversi = self._conn.reversi
        games = reversi.games
        game = games.find_one({"game": game_id})

        if game['state'] == 'game_over':
            return True, 'game_over'

        board = Board(game[u'board'])
        board = board.move(r, c, 1)
        games.update({'_id': game['_id']}, {"$set": {'board': board._internal_state}, '$push': {'moves': (r, c, 1)}},
                     upsert=False)

        if not board.has_moves(2):
            self.game_over(game_id)
            return True, 'game_over'

        ai = RandomMoveAI()

        x, y = ai.get_best_move(board, 2)
        board = board.move(x, y, 2)

        games.update({'_id': game['_id']}, {"$set": {'board': board._internal_state}, '$push': {'moves': (x, y, 2)}},
                     upsert=False)

        if not board.has_moves(1):
            self.game_over(game_id)
            return True, 'game_over'

        return True, 'next_step'

    def game_over(self, game_id):
        reversi = self._conn.reversi
        games = reversi.games
        game = games.find_one({"game": game_id})
        games.update({'_id': game['_id']}, {"$set": {'state': 'game_over'}},
                     upsert=False)
        pprint(games.find_one({"game": game_id}))