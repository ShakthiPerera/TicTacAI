class TicTac:
  def __init__(self, size=3):
    self.size = size
    self.board = [['.' for _ in range(size)] for _ in range(size)]

  def display(self):
    for i in range(self.size):
      for j in range(self.size):
        print(self.board[i][j],' | ',  end=' ')
      print()
    print()

  def make_move(self,playerMark, row, col):
    if self.is_valid(playerMark, row, col):
      self.board[row][col] = playerMark
    else:
      print("Invalid Play.Enter a Valid Move!")
      print()

  def is_valid(self, playerMark, row, col):
    if row < 0 or row > self.size-1 or col < 0 or col> self.size-1:
      return False
    elif playerMark != 'X' and playerMark != 'O':
      return False
    elif self.board[row][col] != '.':
      return False
    else:
      return True

  def is_end(self):
    for i in range(self.size):
      # Horizontal
      if self.board[i] == ['X', 'X', 'X']:
        return 'X'
      elif self.board[i] == ['O', 'O', 'O']:
        return 'O'
      # Vertical
      elif self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[2][i] != '.':
        return self.board[0][i]
    if self.board[0][0] == self.board[1][1] and  self.board[1][1] == self.board[2][2] and self.board[2][i] != '.':
      return self.board[0][0]

    dot_count = 0
    for i in range(self.size):
      for j in range(self.size):
        if self.board[i][j] == '.':
          dot_count += 1
    if dot_count == 0:
      return 'TIE'
    return None

  #max player is 'O'
  def max(self):
    max_score = -2
    px = py = 0
    result = self.is_end()
    if result == 'X':
        return -1, 0, 0
    elif result == 'O':
        return 1, 0, 0
    elif result == 'TIE':
        return 0, 0, 0
    for i in range(3):
      for j in range(3):
        if self.is_valid('O', i, j):
            self.board[i][j] == 'O'
            m, px, py = self.min()
            if m > max_score:
                max_score = m
                px = i
                py = j
            self.board[i][j] == '.'
    return max_score, px, py

  def min(self):
    max_score = 2
    px = py = 0
    result = self.is_end()
    if result == 'X':
        return 1, 0, 0
    elif result == 'O':
        return -1, 0, 0
    elif result == 'TIE':
        return 0, 0, 0
    for i in range(3):
      for j in range(3):
        if self.is_valid('X', i, j):
            self.board[i][j] == 'X'
            m, px, py = self.min()
            if m < max_score:
                max_score = m
                px = i
                py = j
            self.board[i][j] == '.'
    return max_score, px, py

  def play(self):
    playerMark = 'X'
    while True:
      result = self.is_end()
      if not result is None:
        if result == 'X':
          print("X is the Winner")
        elif result == 'O':
          print("O is the Winner")
        elif result == 'TIE':
          print("This is a Tie")
        break
      else:
        print(f"This is the {playerMark} Turn !!!")
        print()
        row = int(input("Enter the Row Number:"))
        col = int(input("Enter the Column Number:"))

        self.make_move(playerMark, row, col)
        print()
        self.display()
        print()
        if playerMark == 'X':
          playerMark = 'O'
        elif playerMark == 'O':
          playerMark = 'X'

if __name__ == '__main__':
  game = TicTac()
  game.play()

