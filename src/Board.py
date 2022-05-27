from Wincheck import Wincheck
class Board():
  def __init__(self): 
    self.grid = [["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]]
    self.winningperson = ""
    
  
  def print_self(self): 
      print (self.grid[0])
      print (self.grid[1])
      print (self.grid[2])
  def check_win(self):
    wc = Wincheck(self.grid)
    wc.checkwin()
    print (wc.winner)
    self.winningperson = wc.person
    return wc.winner


    
  
  def take_turnX(self):
    # not yet built
    print("not yet built")
  def take_turnO(self):
    # not yet built
    print("not yet built")
  def get_board_img(self):
    board_as_string = str(self.grid[0][0]) + " | " + str(self.grid[0][1]) + " | "+ str(self.grid[0][2])+ "\n---------\n"+ str(self.grid[1][0]) + " | " + str(self.grid[1][1]) + " | "+ str(self.grid[1][2])+ "\n---------\n"+ str(self.grid[2][0]) + " | " + str(self.grid[2][1]) + " | "+ str(self.grid[2][2])
    return board_as_string 

  def receive_data(self,row,column,letter):
    self.grid[row][column] = letter
    
