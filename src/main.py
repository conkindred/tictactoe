from Board import Board
from easygui import *
b = Board()




def start_game():
  #print("Developer credit: Constantine Kindred")
  #print("Take turns placing Xs and Os on the board to try to get three in a row!")
  #print("Rules: Players take turns placing symbols only in empty spaces. Get three in a row to win.")
  #print("How to win: Be the first player to have three of your symbols in a row, try placing strategically to block opportunities for your opponnent to get three in a row.")
  #print("Game will start automatically.")
  title = "Tic-Tac-Toe Game"
  msg = "___________    ___________    ___________\n\__    ___/    \__    ___/    \__    ___/\n  |    |  ______ |    |  ______ |    |   \n  |    | /_____/ |    | /_____/ |    |  \n  |____|         |____|         |____|  \n Developer credit: Constantine Kindred \n Take turns placing Xs and Os on the board to try to get three in a row! \n Rules: Players take turns placing symbols only in empty spaces. Get three in a row to win. \n How to win: Be the first player to have three of your symbols in a row, try placing strategically to block opportunities for your opponnent to get three in a row. \n Game will start automatically. "
  button = "Let's Go"
  msgbox(msg, title, button )

def end_game():
  title = "Tic-Tac-Toe Game" 
  msg = "___________    ___________    ___________\n\__    ___/    \__    ___/    \__    ___/\n  |    |  ______ |    |  ______ |    |   \n  |    | /_____/ |    | /_____/ |    |  \n  |____|         |____|         |____|  \n Developer credit: Constantine Kindred \n Player 1 wins! \n Thank you for playing!   "
  button = "Click here to play again"
  msgbox(msg, title, button )


def game_turn():
  title = "Tic-Tac-Toe Game" 
  msg = b.get_board_img()
  button = "Click here to play again"
  msgbox(msg, title, button )

  
start_game()

game_turn()

print("Tic-Tac-Toe")
end_game()


