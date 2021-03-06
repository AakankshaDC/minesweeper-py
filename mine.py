from graphics import * 
import random
from math import *
from time import sleep
import os
from itertools import chain
import numbers
#31

def gameInstructions(): # set up! 
  instr = GraphWin("Instructions", 292,350)
  instr.setBackground("light gray")

  box = Rectangle(Point(5,5),Point(287,50))
  box.draw(instr)
  txt = Text(Point(144,15),"Clear the rectangular board containing mines")
  txt.draw(instr)
  txt = Text(Point(143,28),"without detonating any mines with help from")
  txt.draw(instr)
  txt = Text(Point(144,41),"clues about the number of neighboring mines")
  txt.draw(instr)
  
  box = Rectangle(Point(5,55),Point(287,220))
  box.draw(instr)
  txt = Text(Point(83,70),"DETAILED INSTRUCTIONS:")
  txt.setStyle('bold')
  txt.draw(instr)
  txt = Text(Point(141,85),"The game is played by clicking and revealing squares")
  txt.draw(instr)
  txt = Text(Point(139,100),"If a square containing a mine is revealed the player'd")
  txt.draw(instr)
  txt = Text(Point(143,115),"loose the game. If no mine is revealed a digit's instead")
  txt.draw(instr)
  txt = Text(Point(141,130),"displayed in the square indicating how many adjacent")
  txt.draw(instr)
  txt = Text(Point(138,145),"squares contain mines; if no mines are adjacent the")
  txt.draw(instr)
  txt = Text(Point(141,160),"square would become blank and all adjacent squares")
  txt.draw(instr)
  txt = Text(Point(138,175),"will be recursively revealed. The player needs to use")
  txt.draw(instr)
  txt = Text(Point(147,190),"this information to deduce the contents of other squares")
  txt.draw(instr)
  txt = Text(Point(145,205),"and reveal all the squares that arent mines the quickest")
  txt.draw(instr)
  
  txt = Text(Point(140,260),"GOOD LUCK\nHAVE FUN!")
  txt.setSize(16)
  txt.setStyle("bold")
  txt.draw(instr)

  #create exit button
  exitbox = Rectangle(Point(110,300),Point(170,330))
  exitbox.setFill("grey")
  exitbox.draw(instr)
  exit_text = Text(Point(140,315),"EXIT")
  exit_text.setStyle('bold')
  exit_text.setSize(10)
  exit_text.draw(instr)

  #if exit is clicked close instr window
  for i in range(100):
    q = instr.getMouse()
    x3 = q.getX()
    y3 = q.getY()
    if x3 in range(110,170) and y3 in range(300,330):
      instr.close()
      break
    else:
      q = instr.getMouse() 

def entryWindow(): #set up! 

  # Create Game Control window
  gameControl = GraphWin('Start',250,200)
  gameControl.setBackground('light gray')
  
  # New Game Box
  newGameButton = Rectangle(Point(5,160),Point(110,195))
  newGameButton.setFill("grey")
  newGameButton.draw(gameControl)
  newGameText = Text(Point(60,177), "NEW GAME")
  newGameText.setStyle('bold')
  newGameText.setSize(10)
  newGameText.draw(gameControl)
  
  # Exit Box
  exitButton = Rectangle(Point(180,160),Point(245,195))
  exitButton.setFill("black")
  exitButton.draw(gameControl)
  exitMessage = Text(Point(215,177), "EXIT")
  exitMessage.setFill('White')
  exitMessage.setStyle('bold')
  exitMessage.setSize(10)
  exitMessage.draw(gameControl)
  
  # Player Name
  player = Entry(Point(160,60),10)
  player.setFill("white")
  player.draw(gameControl)
  playerText = Text(Point(75,60), "PLAYER NAME")
  playerText.setStyle('bold')
  playerText.setSize(10)
  playerText.draw(gameControl)
  
  # Header
  header = Rectangle(Point(0,0),Point(250,35))
  header.setFill("grey")
  header.draw(gameControl)
  messageH = Text(Point(125,20), "MINESWEEPER")
  messageH.setFill("black")
  messageH.setSize(13)
  messageH.setStyle('bold')
  messageH.draw(gameControl)

  # Top Scorers chart
  messageTop = Text(Point(125,90),"TOP SCORERS")
  messageTop.setStyle('bold')
  messageTop.setSize(12)
  messageTop.draw(gameControl)

  # Top 3 scores from file
  topList = []
  if os.path.exists("scores.txt"):
    scoresFile = open('scores.txt','r')
    contents = scoresFile.readlines()
    for i in range(len(contents)):
      topList.append(contents[i].rstrip('\n').split(','))
    scoresFile.close()
  
  if len(topList) > 2:
    message1N = Text(Point(95,110),topList[0][0])
    message1N.setSize(10)
    message1N.draw(gameControl)
    message1S = Text(Point(150,110),topList[0][1])
    message1S.setSize(10)
    message1S.draw(gameControl)

    message2N = Text(Point(95,130),topList[1][0])
    message2N.setSize(10)
    message2N.draw(gameControl)
    message2S = Text(Point(150,130),topList[1][1])
    message2S.setSize(10)
    message2S.draw(gameControl)

    message3N = Text(Point(95,150),topList[2][0])
    message3N.setSize(10)
    message3N.draw(gameControl)
    message3S = Text(Point(150,150),topList[2][1])
    message3S.setSize(10)
    message3S.draw(gameControl)

  if len(topList) == 2:
    message1N = Text(Point(95,100),topList[0][0])
    message1N.setSize(10)
    message1N.draw(gameControl)
    message1S = Text(Point(150,100),topList[0][1])
    message1S.setSize(10)
    message1S.draw(gameControl)

    message2N = Text(Point(95,120),topList[1][0])
    message2N.setSize(10)
    message2N.draw(gameControl)
    message2S = Text(Point(150,120),topList[1][1])
    message2S.setSize(10)
    message2S.draw(gameControl)

  if len(topList) == 1:
    message1N = Text(Point(95,100),topList[0][0])
    message1N.setSize(10)
    message1N.draw(gameControl)
    message1S = Text(Point(150,100),topList[0][1])
    message1S.setSize(10)
    message1S.draw(gameControl)
  
  return gameControl, newGameButton, exitButton, player, header


# Define Game Window function
def window(): # todo
  # add timer and makee it Player Reset Timer

  # Window
  GoldHunt = GraphWin("Game Window",480,520,autoflush = False)

  # Header
  header = Rectangle(Point(0,0),Point(480,40))
  header.setFill("black")
  header.draw(GoldHunt)
  # messageR = Text(Point(40,20),"Round:")
  # messageR.setFill("yellow")
  # messageR.draw(GoldHunt)

  # Click Counter
  messageC = Text(Point(430,20),"Score:")
  messageC.setFill("yellow")
  messageC.draw(GoldHunt)

  # Player Name
  name = Text(Point(230,20),"Player: ")
  name.setFill('yellow')
  name.draw(GoldHunt)

  return GoldHunt, messageC, name

def grid(GoldHunt,inputP,name): # fixed for 2d
  squares = [['' for i in range(15)] for j in range(15)]
  sqValues = []
  name.setText('Player: ' + inputP) # set player name at top of the window

  # sqmatrix = [[0 for i in range(15)] for j in range(15)]
  # Create for loop within for loop for the 15x15 circle grid
  for i in range (15):
    for k in range(15):
      sq = Rectangle(Point(k*32,i*32+40), Point(k*32+35,i*32+40+35))
      sq.setFill('light grey')
      squares[i][k] = sq
      sq.draw(GoldHunt)

  mineIndices = []
  excluded = set()
  i = 0
  while i<35:
      x = random.randrange(*(0,15))
      y = random.randrange(*(0,15))
      if (x,y) in excluded: continue
      mineIndices.append((x,y))
      i += 1

  mineSquareList = [squares[x][y] for x,y in mineIndices]
  sqValues = [[0 for i in range(15)] for j in range(15)] # defaulting each sq value to be blank
  # start setting up mine valus and then calculated adjacent values
  for x,y in mineIndices:
    sqValues[x][y] = 'X'

  for i in range(len(squares)):
    for j in range(len(squares[i])):
      if (i,j) not in mineIndices:
        val = 0
        if (i-1, j) in mineIndices: val += 1
        if (i+1, j) in mineIndices: val += 1
        if (i, j-1) in mineIndices: val += 1
        if (i, j+1) in mineIndices: val += 1
        if (i-1, j-1) in mineIndices: val += 1
        if (i-1, j+1) in mineIndices: val += 1
        if (i+1, j-1) in mineIndices: val += 1
        if (i+1, j+1) in mineIndices: val += 1
        sqValues[i][j] = val
  
  return squares, sqValues, mineIndices
  
def isInRectangle(x, y, rect):
  x1, y1 = int(rect.getP1().getX()), int(rect.getP1().getY()) 
  x2, y2 = int(rect.getP2().getX()), int(rect.getP2().getY())
  if x in range(x1, x2) and y in range(y1,y2):
    return True
  else:
    return False

def closeGame():
  win2 = GraphWin('Start',235,150)
  win2.setBackground("light grey")

  #create the are you sure text
  are = Text(Point(120,40),"Are you sure?")
  are.setSize(14)
  are.setFill("black")
  are.draw(win2)

  #create the yes or no exitButtons
  yes_b = Rectangle(Point(30,75),Point(105,105))
  yes_b.setFill("black")
  yes_b.draw(win2)
  yes_t = Text(Point(64.5,91),"YES")
  yes_t.setStyle('bold')
  yes_t.setFill('White')
  yes_t.setSize(10)
  yes_t.draw(win2)

  no_b = Rectangle(Point(130,75),Point(205,105))
  no_b.setFill("grey")
  no_b.draw(win2)
  no_t = Text(Point(165.5,90.5),"NO")
  no_t.setFill('black')
  no_t.setStyle('bold')
  no_t.setSize(10)
  no_t.draw(win2)

  #get mouse coordinates
  m = win2.getMouse()
  x1 = m.getX()
  y1 = m.getY()

  if isInRectangle(x1, y1, yes_b):
    return 'YES', win2
  elif isInRectangle(x1, y1, no_b):
    return 'NO', win2

def revealBlockColors(v):
  vals = {
    'X' : ['red', 'black', 'revealAll'], # bg color, text color
     0 : ['grey', 'grey'],
     1 : ['grey', 'blue'],
     2 : ['grey', 'green'],
     3 : ['grey', 'red']
  }
  if v in vals:
    return vals[v]
  else:
    return ['grey', 'red']

def bfs(sqmatrix, i, j, squares, GoldHunt, score, scoreText):
  visited_SQMatrix = sqmatrix.copy()

  stack = [(i,j)] # push the co-ords on the top of the stack
  while stack:
      vertex = stack.pop() # pop from the top of the stack
      i,j = vertex
      visited_SQMatrix[i][j] = 'V' # V for visited
      if j-1>=0 and sqmatrix[i][j-1] == 0:
          stack.append((i,j-1))
          
      if j+1<len(sqmatrix[i]) and sqmatrix[i][j+1] == 0:
          stack.append((i,j+1))
          
      # check if the 4 possible neighbors are 1's
      if i-1>=0 and sqmatrix[i-1][j] == 0:
          stack.append((i-1,j))
          
      if i+1<len(sqmatrix) and sqmatrix[i+1][j] == 0:
          stack.append((i+1,j))

  # display all the flood filled blocks as V and fill it with the appropriate color
  for i in range(len(visited_SQMatrix)):
    for j in range(len(visited_SQMatrix[i])):
      if visited_SQMatrix[i][j] == 'V':
        squares[i][j].setFill('grey')
  
  # we will need one more loop to open all the cells which are adjacent of the V marked ones
  boundary_cells = []
  # if there is any visited one with an adjacent that is not marked as V then add it boundary cells
  for row in range(len(visited_SQMatrix)):
    for col in range(len(visited_SQMatrix[row])):
      if visited_SQMatrix[row][col] == 'V':
        if -1 < (row - 1) < 15 and visited_SQMatrix[row-1][col]!='V': boundary_cells.append((row-1,col))
        if -1 < (row + 1) < 15 and visited_SQMatrix[row+1][col]!='V': boundary_cells.append((row+1,col))
        if -1 < (col - 1) < 15 and visited_SQMatrix[row][col-1]!='V': boundary_cells.append((row,col-1))
        if -1 < (col + 1) < 15 and visited_SQMatrix[row][col+1]!='V': boundary_cells.append((row,col+1))
 
  for x,y in boundary_cells:
    colorList = revealBlockColors(sqmatrix[x][y])
    squares[x][y].setFill(colorList[0])
    score += sqmatrix[x][y]
    valueText = Text(squares[x][y].getCenter(),str(sqmatrix[x][y]))
    valueText.setSize(20)
    valueText.setFill(colorList[1])
    valueText.draw(GoldHunt)
  
  # update score
  scoreText.undraw() # coz initially it was a string
  messageC = Text(Point(455,20),str(score))
  messageC.setFill("yellow")
  messageC.draw(GoldHunt)

  return score, messageC

def main():
  gameControl, newGameButton, exitButton, player, header = entryWindow() # Call control() function
  GoldHunt, messageC, name = window()
  Round = 0
  score = 0
  new_game = True
  scoreText = Text(Point(455,20),'0')
  scoreText.setFill("yellow")
  scoreText.draw(GoldHunt)
  # val = falsee, at thee end check if clicked on that smile face adn maake val to true if clicked and while true in here
  continueGame = True
  while continueGame:
    
    # Produce x and y components from a mouse click
    entryWindowClick = gameControl.checkMouse() # click -> entryWindowClick
    gameWindowClick = GoldHunt.checkMouse() # gameWindowClick -> gameWindowClick
    
    x = None
    y = None
    if entryWindowClick != None:
      x = entryWindowClick.getX()
      y = entryWindowClick.getY()
      
    # call instructions if it in bounds of Mineeesweeper box -> show instr()
    if isInRectangle(x, y, header):
      gameInstructions()

    # Close game if click exit button after create the are you sure window
    if isInRectangle(x, y, exitButton):
      result, win2 = closeGame()
      if result == 'YES':
        gameControl.close()
        GoldHunt.close()
        win2.close()
        break
      elif result == 'NO':
        win2.close()

    # Create grid if click new game button
    x1 = 0
    y1 = 0
    
    if isInRectangle(x, y, newGameButton):
      inputP = player.getText()
      if inputP != "": # Only run if there is a name in the name entry box
        # If new game, get rid of old grid
        if new_game == False:
          try:
            score = 0
            for i in range(len(squares)):
              for j in range(len(squares[i])):
                squares[i][j].undraw()
                scoreText.undraw()
                scoreText = Text(Point(455,20),'0')
                scoreText.setFill("yellow")
                scoreText.draw(GoldHunt)
          except:
            pass
        # Not a new game    
        new_game = False
        Round = 1
        # Call grid() function
        squares, sqValues, mineIndices = grid(GoldHunt,inputP,name) # $$
    
    # If statement if there is a click within the game
    if gameWindowClick != None:
      x1 = gameWindowClick.getX()
      y1 = gameWindowClick.getY()
                 
      if isInRectangle(x, y, exitButton):
        result, win2 = closeGame()
        if result == 'YES':
          gameControl.close()
          GoldHunt.close()
          win2.close()
          break
        elif result == 'NO':
          win2.close()

      # loop to run through list of squares to find square clicked
      for i in range(len(squares)):
        for k in range(len(squares[i])):
          # deal with it based on what value it holds ####
          # if i is a mineIndex reveal all mines and say game over
          # else
            # if val is 0 then #islands -> flood fill -> bfs list of list

          if isInRectangle(x1, y1, squares[i][k]):
            # When it finds the square, change the block to the hidden color and txt
            # it is thee ith square, so use ith sqValues forr color and text: ~~
            colorList = revealBlockColors(sqValues[i][k])
            squares[i][k].setFill(colorList[0])
            valueText = Text(squares[i][k].getCenter(),str(sqValues[i][k]))
            valueText.setSize(20)
            valueText.setFill(colorList[1])
            valueText.draw(GoldHunt)

            if sqValues[i][k] == 'X':
              # reeveal all mines
              for mx,my in mineIndices:
                colorList = revealBlockColors(sqValues[mx][my])
                squares[mx][my].setFill(colorList[0])
                valueText = Text(squares[mx][my].getCenter(),str(sqValues[mx][my]))
                valueText.setSize(20)
                valueText.setFill(colorList[1])
                valueText.draw(GoldHunt)

            elif sqValues[i][k] == 0:
              score, scoreText = bfs(sqValues,i,k, squares, GoldHunt, score, scoreText)
            else:
              score += sqValues[i][k]
              scoreText.undraw()
              scoreText = Text(Point(455,20),str(score))
              scoreText.setFill("yellow")
              scoreText.draw(GoldHunt)
      
main()
