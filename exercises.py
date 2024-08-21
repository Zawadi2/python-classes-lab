class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            '1': None, '2': None, '3': None,
            '4': None, '5': None, '6': None,
            '7': None, '8': None, '9': None,
        }
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Enter a number between 1 and 9 to make a move.")
        while self.winner is None and not self.tie:
            self.render()
            self.get_move()
            self.check_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()
    def render(self):
        self.print_board()
        self.print_message()
    def print_board(self):
        b = self.board
        print(f"""
 {b['1'] or '1'} | {b['2'] or '2'} | {b['3'] or '3'}
  ---------
 {b['4'] or '4'} | {b['5'] or '5'} | {b['6'] or '6'}
  ---------
 {b['7'] or '7'} | {b['8'] or '8'} | {b['9'] or '9'}
""")
    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"Player {self.winner} wins! Congratulations!")
        else:
            print(f"Player {self.turn}'s turn!")
    def get_move(self):
        while True:
            move = input(f"Player {self.turn}, enter your move (1-9): ")
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                print(f"Player {self.turn} moved to {move}.")
                break
            else:
                print("Invalid move. Try again!")
    def check_winner(self):
        winning_combinations = [
            ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),
            ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),
            ('1', '5', '9'), ('3', '5', '7')
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != None:
                self.winner = self.board[combination[0]]
                break
    def check_for_tie(self):
        if None not in self.board.values() and self.winner is None:
            self.tie = True
    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
game_instance = Game()
game_instance.play_game()