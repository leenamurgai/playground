"""
X|-|-
O|-|-
-|-|-

1/
- Create board
- Display current board status (using design above)
- make_move function

2/
- is_full function
- Write agent that takes a board and plays a random move

3/ Create a game loop where a user can
    A/ Input a move (have clear instructions)
    B/ You validate it (and give instructions if the user input is
       wrong)
    C/ The AI plays a random move
    D/ Display the state of the board and ask for the next move

4/ Create an AI that is better. It follows these 3 rules in order:
    A/ If it can win in the next turn, it does
    B/ If it can stop the enemy from winning, it does
    C/ It tries to line up 2 tokens so that it can win the next round
"""

import random

class board:
    def __init__(self):
        self.board = [['-']*3, ['-']*3, ['-']*3]
        self.empty_cells = [(i,j) for i in range(3) for j in range(3)]

    def set_board(self, board):
        self.board = board
        self.empty_cells = [(i,j) for i in range(3) for j in range(3)
                                                if board[i][j] == '-']

    def get_board(self):
        return self.board

    def display_board(self):
        output = [''] * 3
        for i in range(3):
            output[i] = self.board[i][0]+'|'+self.board[i][1]+'|'+self.board[i][2]
            print(output[i])
        print('\n')
        return output

    def is_full(self):
        return len(self.empty_cells) == 0

    def num_empty_cells(self):
        return len(self.empty_cells)

    def make_move(self, i, j, ox):
        print(i,j)
        if i < 0 or i > 2 or j < 0 or j > 2:
            print('You are off the board - try again')
            return False
        if self.board[i][j] == '-':
            self.board[i][j] = ox
            self.empty_cells.remove((i,j))
        else:
            print('This position is taken - try again')
            return False
        return True

    def random_move(self, ox):
        assert ox =='o' or ox == 'x', "only o or x allowed"
        (i, j) = random.choice(self.empty_cells)
        self.board[i][j] = ox
        self.empty_cells.remove((i,j))
        return (i, j)

    def winning_move(self, i, j):
        # check the row
        arr = self.board[i]
        if arr[0] == arr[1] and arr[1] == arr[2]:
            return True
        # check the column
        arr = [self.board[k][j] for k in range(3)]
        if arr[0] == arr[1] and arr[1] == arr[2]:
            return True
        # check the leading diagonal
        if i == j:
            arr = [self.board[i][i] for i in range(3)]
            if arr[0] == arr[1] and arr[1] == arr[2]:
                return True
        # check the off diagonal
        if i + j == 2:
            arr = [self.board[i][2-i] for i in range(3)]
            if arr[0] == arr[1] and arr[1] == arr[2]:
                return True
        return False

    def can_win_line(self, arr, ox):
        if arr[0] == ox and arr[1] == ox and arr[2] == '-':
            return 3
        if arr[0] == ox and arr[2] == ox and arr[1] == '-':
            return 2
        if arr[1] == ox and arr[2] == ox and arr[0] == '-':
            return 1
        return 0

    def can_win(self, ox):
        print('can_win')
        for i in range(3):
            # check the rows
            n = self.can_win_line(self.board[i], ox)
            if n: return (i, n-1)
            # check the columns
            n = self.can_win_line([self.board[j][i] for j in range(3)], ox)
            if n: return (n-1, i)
        # check the leading diagonal
        n = self.can_win_line([self.board[j][j] for j in range(3)], ox)
        if n: return (n-1, n-1)
        # check the off diagonal
        n = self.can_win_line([self.board[j][2-j] for j in range(3)], ox)
        if n: return (n-1, 3-n)
        return (-1, -1)

    def find_pair(self, idx, arr, ox):
        assert arr[idx] == ox
        idxs = [0,1,2]
        del idxs[idx]
        if arr[idxs[0]] == arr[idxs[1]] == '-':
            return idxs[0]+1
        return 0

    def make_pair(self, ox):
        print('make_pair')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ox:
                    # row
                    n = self.find_pair(j, self.board[i], ox)
                    if n: return (n-1, j)
                    # column
                    n = self.find_pair(i, [self.board[k][j] for k in range(3)], ox)
                    if n: return (i, n-1)
                    # leading diagonal
                    if i == j:
                        n = self.find_pair(i, [self.board[i][i] for i in range(3)], ox)
                        if n: return (n-1, n-1)
                    # off diagonal
                    if i + j == 2:
                        n = self.find_pair(i, [self.board[i][2-i] for i in range(3)], ox)
                        if n: return (n-1, 3-n)
        return (-1, -1)

    def play_game(self):
        # display the board
        self.display_board()
        # pick o or x
        valid = False
        ai_ox = 'x'
        while not(valid):
            player_ox = input("please choose your marker, o or x: ")
            if player_ox == 'o':
                valid = True
            elif player_ox == 'x':
                ai_ox = 'o'
                valid = True

        # ai always goes first and chooses a corner at random
        self.make_move(random.choice([0,2]), random.choice([0,2]), ai_ox)
        self.display_board()
        while not(self.is_full()):
            # player make_move
            valid = False
            while not(valid):
                i = int(input('choose a row between 1 and 3: ')) - 1
                j = int(input('choose a column between 1 and 3: ')) - 1
                valid = self.make_move(i, j, player_ox)
            # display the board
            self.display_board()
            # check for win
            if self.winning_move(i, j):
                print("YOU WIN!!!")
                break
            # ai move
            n_empty = len(self.empty_cells)
            (i, j) = self.can_win(ai_ox)
            if i >= 0:
                self.make_move(i, j, ai_ox)
            else:
                (i, j) = self.can_win(player_ox)
                if i >= 0:
                    self.make_move(i, j, ai_ox)
                else:
                    (i, j) = self.make_pair(ai_ox)
                    if i >= 0:
                        self.make_move(i, j, ai_ox)
            if n_empty == len(self.empty_cells):
                i, j = self.random_move(ai_ox)
            # display the board
            self.display_board()
            # check for win
            if self.winning_move(i, j):
                print("I WIN!!!")
                break


if __name__ == "__main__":
    my_board = board()
    my_board.play_game()
