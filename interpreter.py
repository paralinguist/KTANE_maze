#This is not needed to run the module - it is solely for use as a tester/maze image creator and must be run on a system with a GUI.
#Do not look too closely at this code please. It was cobbled together between classes as a quick-and-dirty solution.
from turtle import *

normal = 0
down = 1
up = 2
lefte = 1
righte = 2
vrighte = 3
vlefte = 4

#To read the maze:
#0s indicate spaces that may be occupied by the red and white dots (player and target)
#1s indicate a wall - replaces 2s only
#2s indicate padding - spaces that are not occupied by the wall
#3s indicate the "signature" for this maze - to help the defuser identify the correct maze in the manual. Replaces a 0
"""Blank Maze:
       [
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
       ],
"""

mazes = [
       [
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
        [2,1,1,1,1,1,1,2,1,1,1,1,1,1,2],
        [0,1,0,2,0,2,0,2,0,2,0,2,0,1,0],
        [2,1,2,1,1,1,1,1,1,1,1,1,2,1,2],
        [0,1,0,2,0,2,0,2,0,2,0,1,0,1,0],
        [2,1,2,1,2,1,1,1,1,1,2,1,2,1,2],
        [0,2,0,1,3,1,0,2,0,1,0,2,0,1,0],
        [2,1,2,1,2,1,2,1,1,1,2,1,2,2,2],
        [0,1,0,1,0,1,0,2,0,2,0,1,0,1,0],
        [2,1,2,1,2,1,1,1,1,1,1,1,2,1,2],
        [0,1,0,1,0,2,0,2,0,2,0,2,0,1,0],
        [2,1,2,1,2,1,1,1,1,1,1,1,1,1,2],
        [0,1,0,2,3,2,0,2,0,2,0,2,0,2,0],
        [2,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
        [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
       ],
  
       [
        [0,1,0,1,0,1,0,1,0,1,0,2,0,2,0],
        [2,1,2,1,2,1,2,1,2,1,2,1,1,1,1],
        [0,1,0,1,0,1,0,1,0,1,0,2,0,2,0],
        [2,2,2,2,2,1,2,1,2,1,2,1,1,1,1],
        [0,2,0,2,0,1,0,2,0,1,0,2,0,2,0],
        [1,1,1,1,2,1,2,1,2,1,2,1,1,1,1],
        [0,2,0,2,0,1,0,1,0,1,0,2,0,2,0],
        [1,1,1,1,2,1,2,1,2,1,2,1,1,1,1],
        [0,2,0,2,0,1,0,1,0,1,0,2,3,2,0],
        [1,1,1,1,2,1,2,1,2,1,2,1,1,1,1],
        [0,2,0,2,0,2,0,1,0,2,0,2,0,2,0],
        [2,1,2,1,2,1,2,1,2,2,2,2,2,2,2],
        [0,1,0,1,0,1,0,1,0,1,0,1,3,1,0],
        [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
        [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       ],
       [
        [0,2,0,2,0,2,0,2,0,1,0,1,0,2,0],
        [1,1,1,1,2,1,1,1,1,1,2,1,2,1,2],
        [0,2,0,1,0,2,0,2,0,1,0,1,0,1,0],
        [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2],
        [0,2,0,1,0,1,3,2,0,1,3,1,0,1,0],
        [1,1,2,1,2,1,1,1,2,1,2,1,2,1,1],
        [0,2,0,1,0,2,0,2,0,1,0,1,0,2,0],
        [2,1,2,1,2,1,1,1,1,1,2,2,2,1,2],
        [0,1,0,2,0,2,0,2,0,2,0,1,0,1,0],
        [2,1,1,1,1,2,1,1,1,1,2,1,1,1,2],
        [0,1,0,2,0,2,0,1,0,1,0,2,0,1,0],
        [2,1,2,1,2,1,2,1,2,1,1,1,2,1,2],
        [0,2,0,1,0,1,0,1,0,1,0,2,0,1,0],
        [2,1,1,1,1,1,2,1,2,1,2,1,1,1,2],
        [0,2,0,2,0,1,0,2,0,1,0,2,0,2,0],
       ],
       [
        [0,2,0,2,0,2,0,1,0,1,0,2,0,1,0],
        [2,1,1,1,1,1,1,1,2,1,2,1,2,1,2],
        [0,2,0,2,0,2,0,1,0,1,0,1,0,1,0],
        [1,1,1,1,1,1,2,1,2,1,2,1,2,1,2],
        [0,2,0,2,0,2,0,1,0,1,0,1,0,1,0],
        [2,1,1,1,1,1,1,1,2,1,2,1,2,1,2],
        [0,2,0,2,0,2,0,2,0,2,0,1,0,2,0],
        [1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],
        [0,2,0,2,0,2,0,2,0,2,0,1,0,2,0],
        [1,1,1,1,1,1,2,1,2,1,2,1,2,1,2],
        [0,2,0,2,0,2,3,1,3,1,0,1,0,1,0],
        [2,1,1,1,1,1,1,1,2,1,2,1,2,1,2],
        [0,2,0,2,0,2,0,1,0,1,0,1,0,1,0],
        [1,1,1,1,1,1,2,1,2,1,2,1,2,1,2],
        [0,2,0,2,0,2,0,1,0,1,0,2,0,1,0],
       ],

       [
        [0,2,0,2,0,1,0,1,0,2,0,2,0,2,0],
        [2,1,1,1,2,2,2,1,1,1,2,1,1,1,1],
        [0,1,0,1,0,2,0,1,0,1,0,2,0,2,0],
        [2,2,2,2,2,1,1,1,2,2,2,1,1,1,1],
        [0,1,0,2,3,2,0,1,0,2,0,2,0,2,0],
        [2,1,1,1,2,2,2,2,2,1,1,1,2,1,2],
        [0,1,0,2,0,1,0,1,0,1,0,2,0,1,0],
        [2,2,2,2,2,2,2,2,2,2,2,1,1,1,1],
        [0,1,0,1,0,1,0,2,0,1,3,2,0,2,0],
        [2,2,2,2,2,0,2,2,2,1,1,1,1,1,2],
        [0,1,0,1,0,2,0,1,0,2,0,1,0,2,0],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [0,2,0,2,0,2,0,1,0,2,0,1,0,2,0],
        [2,2,1,1,1,1,2,2,2,2,2,1,1,1,2],
        [0,2,0,2,0,1,0,2,0,1,0,2,0,1,0],
       ],
       [
        [3,2,0,2,0,2,0,1,0,2,0,2,0,2,0],
        [1,1,1,1,2,1,2,1,2,1,1,1,1,1,1],
        [0,1,0,2,0,1,0,1,0,1,0,2,0,2,0],
        [2,1,2,1,2,1,2,2,2,1,2,1,1,1,1],
        [0,1,0,1,0,1,0,2,0,2,0,1,0,2,0],
        [2,2,2,1,2,1,1,1,1,1,2,1,2,1,2],
        [0,2,0,1,0,2,0,2,0,2,0,1,0,1,0],
        [2,1,1,1,1,1,2,2,2,1,1,1,2,1,1],
        [0,2,0,2,0,1,0,1,0,2,0,2,0,2,0],
        [1,1,2,1,1,1,2,1,2,1,2,1,1,1,1],
        [0,1,0,2,0,1,0,1,0,1,0,1,0,1,0],
        [2,2,2,1,2,1,2,1,1,1,1,1,2,1,2],
        [0,2,0,1,0,1,0,2,0,2,0,2,0,2,0],
        [1,1,2,1,2,1,1,1,1,1,1,1,1,1,2],
        [0,2,0,1,0,2,0,2,0,2,0,2,0,2,3],
       ],
       
       ]

size = len(mazes[0])
unit = 20

def diamond():
  penup()
  left(90)
  forward(unit/1.5)
  pendown()
  right(135)
  forward(unit)
  right(90)
  forward(unit)
  right(90)
  forward(unit)
  right(90)
  forward(unit)
  right(135)
  penup()
  forward(unit/1.5)
  left(90)

def vertical_edge(length):
  if length == normal:
    left(90)
    pendown()
    forward(unit/2)
    backward(unit)
    forward(unit/2)
    right(90)
    penup()
  elif length == down:
    pendown()
    left(90)
    forward(unit/2)
    backward(unit*1.5)
    forward(unit)
    right(90)
    penup()
  elif length == up:
    pendown()
    left(90)
    forward(unit)
    backward(unit*1.5)
    forward(unit/2)
    right(90)
    penup()

def horizontal_edge(length):
  if length == vrighte:
    pendown()
    forward(unit)
    backward(unit)
    penup()
  elif length == lefte:
    pendown()
    backward(unit/2)
    forward(unit/2)
    penup()
  elif length == righte:
    pendown()
    forward(unit/2)
    backward(unit/2)
    penup()
  else:
    pendown()
    backward(unit)
    forward(unit)
    penup()

def next_row():
  backward(unit * size)
  right(90)
  forward(unit)
  left(90)

def side_edges(row, col):
  edges = False
  if row - 1 > 0 and maze[row-1][col] == 1:
    edges = True
  elif row + 1 < size and maze[row+1][col] == 1:
    edges = True
  return edges

speed(10)

penup()
goto(-200,200)

maze_num = 0

for maze in mazes:
  start_coords = pos()

  row_num = 0
  col_num = 0
  penup()
  for row in maze:
    #check for horizontal edges
    if row[0] == 2 or row[0] == 1:
      for column in row:
        if column == 1:
          if col_num-1 >= 0 and maze[row_num][col_num-1] == 1:
            horizontal_edge(lefte)
          if col_num+1 < size and maze[row_num][col_num+1] == 1:
            horizontal_edge(righte)
          if col_num == 0:
            horizontal_edge(vlefte)
          if col_num == size-1:
            horizontal_edge(vrighte)
        forward(unit)
        col_num += 1
    else:
      for column in row:
        if column == 0 or column == 3:
          if column == 3:
            diamond()
          dot()
        elif column == 1:
          if (row_num + 2 < size and maze[row_num][col_num] == 1) or row_num == size-1:
            vertical_edge(down)
          if (row_num - 2 >= 0 and (maze[row_num-2][col_num] == 1) or (maze[row_num-1][col_num] == 1)) or row_num == 0:
            vertical_edge(up)
          vertical_edge(normal)
        forward(unit)
        col_num += 1
    next_row()
    row_num += 1
    col_num = 0
  goto(start_coords)
  backward(unit)
  left(90)
  forward(unit)
  right(90)
  pendown()
  forward(unit * (size + 1))
  right(90)
  forward(unit * (size + 1))
  right(90)
  forward(unit * (size + 1))
  right(90)
  forward(unit * (size + 1))

  penup()
  right(90)
  forward(unit*size + 4*unit)
  right(90)
  forward(unit)
  left(90)
  maze_num += 1
  if maze_num % 3 == 0:
    backward((unit*size)*3 + 4*unit*2+unit)
    right(90)
    forward(unit*size + 3*unit)
    left(90)

hideturtle()
