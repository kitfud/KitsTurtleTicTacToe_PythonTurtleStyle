
import turtle
import time
import os

# getting a Screen to work on
sc=turtle.Screen()
sc.setup(420,420)
# Defining Turtle instance
t=turtle.Turtle()
t.hideturtle()
# setting up turtle color to green
t.color("Red")
# Setting Up width to 2
t.width("2")
# Setting up speed to 0 for fastest
t.speed(0)

def buildBoard(): 
  # Loop for making outside square of
  # length 300
  t.penup()
  t.goto(-150,-150)
  t.pendown()
  for x in range (4):
    t.forward(300)
    t.left(90)
  #horizontal lines
  t.penup()
  t.goto(-150,-50)
  t.pendown()
  t.forward(300)
  t.goto(150,50)
  t.left(180)
  t.forward(300)
  #vertical lines
  t.penup()
  t.goto(-50,150)
  t.pendown()
  t.left(90)
  t.forward(300)
  t.goto(50,-150)
  t.left(180)
  t.forward(300)
  t.penup()
  t.goto(-100,-185)
  t.write("CLICK TO PLAY!",font= ("Verdana",20,"bold"))
buildBoard()

board = []
boardGridPos = {0:(-98,95),1:(-3,97),2:(98,100),3:(-105,-1),4:(-1,-3),5:(87,-2),6:(-104,-102),7:(1,-99),8:(92,-99)}

player = 1
board = [""]*9
win = False
turns = 1

#Checking For Win
#checks and sees if three in a row is there 
def check_for_three(board,s1,s2,s3):
  if(board[s1] != "" and board[s1] == board[s2] and board[s1]== board[s3]):
    return True
  else:
    return False

def changePlayer():
  global player,turns
  os.system('clear')
  if player ==1:
    player = 2
  else:
    player = 1
  print(f"Player {player} turn")
  turns += 1

def drawWinLine(i1,i2,i3):
  t.goto(boardGridPos[i1][0],boardGridPos[i1][1])
  t.pendown()
  t.goto(boardGridPos[i2][0],boardGridPos[i2][1])
  t.goto(boardGridPos[i3][0],boardGridPos[i3][1])

def announceWin():
  t.goto(-15,177)
  t.write("Player {} wins!".format(player))

#check all combinations for win
def check_win(board,player):
  global win
  if check_for_three(board, 0, 1, 2):
    win = True
    announceWin()
    drawWinLine(0,1,2)
  elif check_for_three(board, 3, 4, 5):
    win = True
    announceWin()
    drawWinLine(3,4,5)
  elif check_for_three(board, 6, 7, 8):
    win = True
    announceWin()
    drawWinLine(6,7,8)
  elif check_for_three(board, 0, 3, 6):
    win = True
    announceWin()
    drawWinLine(0,3,6)
  elif check_for_three(board, 1, 4, 7):
    win = True
    announceWin()
    drawWinLine(1,4,7)
  elif check_for_three(board, 2, 5, 8):
    win = True
    announceWin()
    drawWinLine(2,5,8)
  elif check_for_three(board, 0, 4, 8):
    win = True
    announceWin()
    drawWinLine(0,4,8)
  elif check_for_three(board, 2, 4, 6):
    win = True
    announceWin()
    drawWinLine(2,4,6)
  else:
    if turns == 9:
      print("TIE GAME")
      t.goto(-15,177)
      t.write("TIE GAME".format(player))
      win = True
    else:
      changePlayer()  
  
def placeMarker(select):
  global player, clickSelect,board
  if win == False:
    if board[select] == "":
      if player ==1:
        board[select] = "x"
        t.goto(boardGridPos[select][0],boardGridPos[select][1])
        t.write("x",font= ("Verdana",20,"bold"))
      else:
        board[select] = "o"
        t.goto(boardGridPos[select][0],boardGridPos[select][1])
        t.write("o",font= ("Verdana",20,"bold"))
    else:
      print("click a new square")
      return   
  check_win(board,player)

def zoneDetect(x,y):
  global clickSelect, player  
  print(x,y)
  if (x >-150 and x<-50) and (y>50 and y<150):
    #print("0")
    placeMarker(0)
  elif (x >-50 and x<50) and (y>50 and y<150):
    #print("1")
    placeMarker(1)
  elif (x >50 and x<150) and (y>50 and y<150):
    #print("2")
    placeMarker(2)
  elif (x >-150 and x<-50) and (y>-50 and y<50):
    #print("3")
    placeMarker(3)
  elif (x >-50 and x<50) and (y>-50 and y<50):
    #print("4")
    placeMarker(4)
  elif (x>50 and x<150) and (y>-50 and y<50):
    #print("5")
    placeMarker(5)
  elif (x >-150 and x<-50) and (y>-150 and y<-50):
    #print("6")
    placeMarker(6)
  elif (x >-50 and x<50) and (y>-150 and y<-50):
    #print("7")
    placeMarker(7)
  elif (x >50 and x<150) and (y>-150 and y<-50):
    #print("8")
    placeMarker(8)

turtle.onscreenclick(zoneDetect)
 
