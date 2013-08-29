from copy import deepcopy

directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
line = (0, 1, 2, 3, 4, 5, 6, 7)

class Board:
    """represents reversi board"""

    def __init__(self, arg):
        self._internal_state = deepcopy(arg)

    def is_move_allowed(self, x, y, player):
        if self._internal_state[x][y] != 0:
            return False
        for direction in directions:
            if self.get_affected_checks((x, y), direction, player):
                return True
        return False

    def has_moves(self, player):
        return len(self.possible_moves(player)) > 0

    def _apply_rotations(self, x, y, player):
        self._internal_state[x][y] = player
        for directon in directions:
            affected_checks = self.get_affected_checks((x, y), directon, player)
            if affected_checks:
                for r, c in affected_checks:
                    self._internal_state[r][c] = player


    def move(self, x, y, player):
        if not self.is_move_allowed(x, y, player):
            return deepcopy(self)
        new_board = Board(self._internal_state)
        new_board._apply_rotations(x, y, player)
        return new_board

    def pprint(self):
        from pprint import pprint
        pprint(self._internal_state)

    def get_affected_checks(self, position, direction, player):
        def increment(p, d):
            return p[0] + d[0], p[1] + d[1]

        affected = []
        cx, cy = position

        while True:
            cx, cy = increment((cx, cy), direction)
            if not (0 <= cx <= 7 and 0 <= cy <= 7):
                return

            if self._internal_state[cx][cy] == 0:
                affected = []
                break

            if self._internal_state[cx][cy] == player:
                break

            if self._internal_state[cx][cy] != 0:
                affected.append((cx, cy))

        if len(affected) == 0:
            return

        return affected

    def possible_moves(self, player):
        moves = []
        for r in line:
            for c in line:
                if self.is_move_allowed(r, c, player):
                    moves.append((r, c))
        return moves

    def score(self, player):
        score = 0
        for r in line:
            for c in line:
                if self._internal_state[r][c] == player:
                    score += 1
        return score


