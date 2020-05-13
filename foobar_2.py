class Board:
    def __init__(self, dim=8):
        self.config = []
        self.dim = dim
        self._set_config()

    def _set_config(self):
        for i in range(self.dim):
            self.config.append([])
            for j in range(self.dim):
                self.config[i].append(self.dim*i + j)

    def get_config(self):
        return self.config

    def get_data(self, i, j):
        if (i >= 0 and i < self.dim) and (j >= 0 and j < self.dim):
            return self.config[i][j]
        return None

    def get_coord(self, data):
        j = -1
        for row in self.config:
            if data in row:
                j = row.index(data)
        i = int((data - j) / self.dim)
        return (i,j)

class Player:
    def __init__(self, board, src, num_moves):
        self.board = board
        self.current_pos = self.board.get_coord(src)
        self.num_moves = num_moves

    def next_moves(self):
        next = []
        row, col = self.current_pos
        # print(row, col)
        '''
        Player moves to the left by one and then moves up and down by two
        '''
        if col > 0:
            if row < self.board.dim-2:
                next.append(Player(self.board, self.board.get_data(row+2, col-1), self.num_moves+1))
            if row > 1:
                next.append(Player(self.board, self.board.get_data(row-2, col-1), self.num_moves+1))
        '''
        Player moves to the right by one and then moves up and down by two
        '''
        if col >= 0 and col < self.board.dim-1:
            if row < self.board.dim-2:
                next.append(Player(self.board, self.board.get_data(row+2, col+1), self.num_moves+1))
            if row > 1:
                next.append(Player(self.board, self.board.get_data(row-2, col+1), self.num_moves+1))
        '''
        Player moves to the left by two and then moves up and down by one
        '''
        if col > 1:
            if row < self.board.dim-2:
                next.append(Player(self.board, self.board.get_data(row+1, col-2), self.num_moves+1))
            if row > 1:
                next.append(Player(self.board, self.board.get_data(row-1, col-2), self.num_moves+1))
        '''
        Player moves to the right by two and then moves up and down by one
        '''
        if col >= 0 and col < self.board.dim-2:
            if row < self.board.dim-2:
                next.append(Player(self.board, self.board.get_data(row+1, col+2), self.num_moves+1))
            if row > 1:
                next.append(Player(self.board, self.board.get_data(row-1, col+2), self.num_moves+1))

        return next

def solution(src, dest):
    board = Board()
    visited = []
    explored = []
    player = Player(board, src, 0)
    visited.append(src)
    min_moves = 0

    for next_move in player.next_moves():
        explored.append(next_move)

    # print(player.current_pos)
    while len(explored) != 0:
        next_player = explored.pop(0)
        data = next_player.board.get_data(next_player.current_pos[0], next_player.current_pos[1])
        if data not in visited:
            visited.append(data)
        # print(visited)
        if data == dest:
            min_moves = next_player.num_moves
            break

        for next_move in next_player.next_moves():
            flag = False
            data = next_move.board.get_data(next_move.current_pos[0], next_move.current_pos[1])
            for player in explored:
                if player.current_pos == next_move.current_pos:
                    flag = True
                    break
            if (data not in visited) and (not flag):
                explored.append(next_move)

    return min_moves

print(solution(19, 36))
print(solution(0, 1))
