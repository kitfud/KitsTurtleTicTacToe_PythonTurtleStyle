
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

buildBoard()

board = []
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


#check all combinations for win
def check_win(board,player):
  global win
  if check_for_three(board, 0, 1, 2):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(-98,95)
    t.pendown()
    t.goto(-3,97)
    t.goto(98,100) 
  elif check_for_three(board, 3, 4, 5):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(-105,-1)
    t.pendown()
    t.goto(-1,-3)
    t.goto(87,-2)
  elif check_for_three(board, 6, 7, 8):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(-104,-102)
    t.pendown()
    t.goto(1,-99)
    t.goto(92,-99)
  elif check_for_three(board, 0, 3, 6):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(-98,95)
    t.pendown()
    t.goto(-105,-1)
    t.goto(-104,-102)
  elif check_for_three(board, 1, 4, 7):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(-3,97)
    t.pendown()
    t.goto(-1,-3)
    t.goto(1,-99)
  elif check_for_three(board, 2, 5, 8):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(98,100)
    t.pendown()
    t.goto(87,-2)
    t.goto(92,-99)
  elif check_for_three(board, 0, 4, 8):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(-98,95)
    t.pendown()
    t.goto(-1,-3)
    t.goto(92,-99)
  elif check_for_three(board, 2, 4, 6):
    print("Player {} wins!".format(player))
    win = True
    t.goto(-15,177)
    t.write("Player {} wins!".format(player))
    t.goto(98,100)
    t.pendown()
    t.goto(-1,-3)
    t.goto(-104,-102)
  else:
    if turns == 9:
      print("TIE GAME")
      t.goto(-15,177)
      t.write("TIE GAME".format(player))
      win = True
    else:
      changePlayer()  
  


def placeMarker():
  global player, clickSelect,board
  #print(board)
  if win == False:
    if clickSelect == 0:
      if board[0] == "":
        if player ==1:
          board[0] = "x"
          t.goto(-98,95)
          t.write("x")

        else:
          board[0] = "o"
          t.goto(-98,95)
          t.write("o")
      else:
        print("click a new square")
        return 
    elif clickSelect == 1:
      if board[1] == "":
        if player ==1:
          board[1] = "x"
          t.goto(-3,97)
          t.write("x")
        else:
          board[0] = "o"
          t.goto(-3,97)
          t.write("o")
      else:
        print("click a new square")
        return 
    elif clickSelect == 2:
      if board[2] == "":
        if player ==1:
          board[2] = "x"
          t.goto(98,100)
          t.write("x")
        else:
          board[2] = "o"
          t.goto(98,100)
          t.write("o")
      else:
        print("click a new square")
        return
    
    elif clickSelect == 3:
      if board[3] == "":
        if player ==1:
          board[3] = "x"
          t.goto(-105,-1)
          t.write("x")
        else:
          board[3] = "o"
          t.goto(-105,-1)
          t.write("o")
      else:
        print("click a new square")
        return
    elif clickSelect == 4:
      if board[4] == "":
        if player ==1:
          board[4] = "x"
          t.goto(-1,-3)
          t.write("x")
        else:
          board[4] = "o"
          t.goto(-1,-3)
          t.write("o")
      else:
        print("click a new square")
        return
    elif clickSelect == 5:
      if board[5] == "":
        if player ==1:
          board[5] = "x"
          t.goto(87,-2)
          t.write("x")
        else:
          board[5] = "o"
          t.goto(87,-2)
          t.write("o")
      else:
        print("click a new square")
        return
    elif clickSelect == 6:
      if board[6] == "":
        if player ==1:
          board[6] = "x"
          t.goto(-104,-102)
          t.write("x")
        else:
          board[6] = "o"
          t.goto(-104,-102)
          t.write("o")
      else:
        print("click a new square")
        return
    elif clickSelect == 7:
      if board[7] == "":
        if player ==1:
          board[7] = "x"
          t.goto(1,-99)
          t.write("x")
        else:
          board[7] = "o"
          t.goto(1,-99)
          t.write("o")
      else:
        print("click a new square")
        return
    elif clickSelect == 8:
      if board[8] == "":
        if player ==1:
          board[8] = "x"
          t.goto(92,-99)
          t.write("x")
        else:
          board[8] = "o"
          t.goto(92,-99)
          t.write("o")
      else:
        print("click a new square")
        return
    check_win(board,player)

def zoneDetect(x,y):
  global clickSelect, player  
  print(x,y)
  if (x >=-150 and x<-50) and (y>50 and y<150):
    #print("0")
    clickSelect = 0
    placeMarker()

  elif (x >=-50 and x<=50) and (y>50 and y<150):
    #print("1")
    clickSelect = 1
    placeMarker()
  elif (x >50 and x<=150) and (y>50 and y<150):
    #print("2")
    clickSelect = 2
    placeMarker()
  elif (x >=-150 and x<-50) and (y>-50 and y<=150):
    #print("3")
    clickSelect = 3
    placeMarker()
  elif (x >=-50 and x<=50) and (y>-50 and y<=150):
    #print("4")
    clickSelect = 4
    placeMarker()
  elif (x>50 and x<=150) and (y>-50 and y<150):
    #print("5")
    clickSelect = 5
    placeMarker()
  elif (x >=-150 and x<-50) and (y>-150 and y<-50):
    #print("6")
    clickSelect = 6
    placeMarker()
  elif (x >=-50 and x<=50) and (y>-150 and y<-50):
    #print("7")
    clickSelect = 7
    placeMarker()
  elif (x >50 and x<=150) and (y>-150 and y<-50):
    #print("8")
    clickSelect = 8
    placeMarker()

turtle.onscreenclick(zoneDetect)
 
