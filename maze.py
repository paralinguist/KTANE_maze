#!/usr/bin/python3
import time, math, random
import sense_hat
from blueprints import mazes

defused = False

red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)
off = (0,0,0)
br = 255

e = blue
f = (127,127,0)
n = (255,165,127)
o = off
d = red

sense = sense_hat.SenseHat()
blue_dots = []
red_x = 0
red_y = 0
x = 0
y = 0
maze = []

def rand_place(restrict=1):
  if restrict == 1:
    minx = 0
    miny = 0
    maxx = 3
    maxy = 3
  else:
    minx = 4
    maxx = 7
    miny = 4
    maxy = 7
  locx = random.randint(minx,maxx)
  locy = random.randint(miny,maxy)
  if [locx, locy] in blue_dots:
    if locx + 2 <= 7:
      locx = locx + 2
    elif locy + 2 <= 7:
      locy = locy + 2
    elif locy - 2 >= 0:
      locy = locy - 2
    else:
      locx = locx - 2

  if [locx, locy] in blue_dots:
    if locx + 1 <= 7:
      locx = locx + 1
    elif locy + 1 <= 7:
      locy = locy + 1
    elif locy - 1 >= 0:
      locy = locy - 1
    else:
      locx = locx - 1

  return locx,locy

def reset_module():
  global maze
  maze = random.choice(mazes)
  sense.clear(0, 0, 0)
  row_num = 0
  global defused
  defused = False
  global blue_dots
  blue_dots = []
  for row in maze:
    if 3 in row:
      by = row_num//2
      bx = row.index(3)//2
      blue_dots.append([bx,by])
      if row.count(3) == 2:
        bx = (len(row) - 1 - row[::-1].index(3))//2
        blue_dots.append([bx,by])
    row_num += 1
  global x
  global y
  global red_x
  global red_y
  red_x, red_y = rand_place()
  x, y = rand_place(2)
  draw_screen()

def draw_screen():
  sense.clear(0, 0, 0)
  sense.set_pixel(red_x, red_y, red)
  sense.set_pixel(x, y, white)
  for dot in blue_dots:
    sense.set_pixel(dot[0], dot[1], blue)

def sad():
  image = [
            d,o,d,o,o,d,o,d,
            o,d,o,o,o,o,d,o,
            d,o,d,o,o,d,o,d,
            o,o,o,o,f,o,o,o,
            o,o,o,f,f,o,o,o,
            o,o,o,o,o,o,o,o,
            o,f,f,f,f,f,f,o,
            f,o,o,o,o,o,o,f
          ]
  sense.set_pixels(image)
  time.sleep(1)
  draw_screen()

def smile():
  image = [
            o,e,o,o,o,o,e,o,
            e,e,e,o,o,e,e,e,
            o,e,o,o,o,o,e,o,
            o,o,o,o,f,o,o,o,
            o,o,o,f,f,o,o,o,
            f,o,o,o,o,o,o,f,
            o,f,o,o,o,o,f,o,
            o,o,f,f,f,f,o,o
          ]
  sense.set_pixels(image)
  
def defuse():
  global defused
  defused = True
  smile()

def collide(ox,oy,dx,dy):
  collision = False
  if maze[oy+dy][ox+dx] == 1:
    collision = True
  return collision

def move_player(event, x, y):
  if not (event.action == sense_hat.ACTION_RELEASED):
    sense.set_pixel(x, y, off)
    if event.direction == sense_hat.DIRECTION_UP and y > 0:
      if collide(x,y,x,y-1):
        sad()
      else:
        y = y - 1
    elif event.direction == sense_hat.DIRECTION_DOWN and y < 7:
      if collide(x,y,x,y+1):
        sad()
      else:
        y = y + 1
    elif event.direction == sense_hat.DIRECTION_RIGHT and x < 7:
      if collide(x,y,x+1,y):
        sad()
      else:
        x = x + 1
    elif event.direction == sense_hat.DIRECTION_LEFT and x > 0:
      if collide(x,y,x-1,y):
        sad()
      else:
        x = x - 1
    sense.set_pixel(x, y, white)
  if x == red_x and y == red_y:
    defuse()
    
  return x, y

last_tick = round(time.time(),1) * 10

get_brighter = False

draw_screen()

while True:
  reset_module()
  while not defused:
    for event in sense.stick.get_events():
      x, y = move_player(event, x, y)
  
    timer = 0.5

    tick = round(time.time(),1) * 10
    #This should stop red flashing when finished. Doesn't work.
    if not defused:
      if (tick % timer == 0) and (tick > last_tick):
        if get_brighter:
          if br >= 255:
            br = br - 10
            get_brighter = False
          else:
            br = br + 10
        else:
          if br <= 20:
            br = br + 10
            get_brighter = True
          else:
            br = br - 10
        sense.set_pixel(red_x, red_y, (br,0,0))
      last_tick = tick
  time.sleep(10)
