import random
import string

class BoggleBoard:

  
  def __init__(self):
    self.game_board = ['_'] * 16
    
    


  def shake(self):
    
    for i, under_score in enumerate(self.game_board):
      random_letter = (random.choice(string.ascii_letters)).upper()
      if(random_letter == 'Q'):
        self.game_board[i] = 'Qu'
      else:
        self.game_board[i] = random_letter


  def view_game_board(self):
    return self.game_board

  def print_board(self):
    for i in range(0, len(self.game_board), 4):
      print(" ".join(self.game_board[i:i+4]))

  

boggle = BoggleBoard()
boggle.shake()
boggle.print_board()