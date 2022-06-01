"""
This program draws a checkerboard
author: Noah Landis
"""
import turtle
import random
import time
PIXEL_SIZE = 200
ROWS = 3
COLS = 3

COORD_TO_SPOT = {"Top Middle": (0, 120), "Middle Middle": (0, -80), "Bottom Middle": (0, -280), 
    "Top Left": (-200, 120), "Middle Left": (-200, -80), "Bottom Left": (-200, -280),
    "Top Right": (200, 120), "Middle Right": (200, -80), "Bottom Right": (200, -280)}

SPOTS_FILLED = {"Top Middle": False, "Middle Middle": False, "Bottom Middle": False, 
    "Top Left": False, "Middle Left": False, "Bottom Left": False,
    "Top Right": False, "Middle Right": False, "Bottom Right": False}

PLACEMENT = {"Top Middle": None, "Middle Middle": None, "Bottom Middle": None, 
    "Top Left": None, "Middle Left": None, "Bottom Left": None,
    "Top Right": None, "Middle Right": None, "Bottom Right": None}
def initalize():
    turtle.speed(0)
    turtle.up()
    turtle.setheading(0)
    turtle.pensize(1)
    turtle.pencolor("black")
    turtle.fillcolor("white")
    turtle.setpos(-COLS / 2 * PIXEL_SIZE, ROWS / 2 * PIXEL_SIZE)

def draw_pixel(color="white"):
    turtle.pencolor("black")
    turtle.fillcolor(color)
    sides = 0
    turtle.down()
    turtle.begin_fill()
    while sides < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        sides += 1
    turtle.end_fill()
    turtle.up()
    turtle.forward(PIXEL_SIZE)

def next_row():
    y = turtle.ycor() - PIXEL_SIZE
    x  = -COLS / 2 * PIXEL_SIZE
    turtle.goto(x, y)

def draw_board():
    """
    This function draws a checkerboard
    """
    # initialze loop control variables
    pixel_count = 0
    row_count = 0
    while (pixel_count < 9):
        # alternate between pixels based on odd or even row number
        draw_pixel()
        pixel_count += 1
        # move rows every 20 pixels
        if (pixel_count % 3 == 0):
            next_row()
            row_count += 1
            continue

def draw_circle(cord):
    turtle.goto(cord)
    turtle.down()
    turtle.color("red")
    turtle.pensize(10)
    turtle.circle(80)
    turtle.up()


def draw_x(cord):
    x, y = cord
    turtle.goto(x, y + 80) # compensate for X starting at lower y value
    turtle.color("blue")
    turtle.pensize(10)
    turtle.down()
    turtle.right(45)
    turtle.forward(80)
    turtle.backward(160)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.backward(160)
    turtle.up()
    turtle.right(45)


def get_mouse_click_coor(x, y):
    if x >= -101 and x <= 99:
        turtle.onscreenclick(None)
        if y >= 100 and y <= 298 and not SPOTS_FILLED["Top Middle"]:
            SPOTS_FILLED["Top Middle"] = True
            draw_x(COORD_TO_SPOT["Top Middle"])
            PLACEMENT["Top Middle"] = "X"
        elif y >= -96 and y <= 99 and not SPOTS_FILLED["Middle Middle"]:
            draw_x(COORD_TO_SPOT["Middle Middle"])
            SPOTS_FILLED["Middle Middle"] = True
            PLACEMENT["Middle Middle"] = "X"
        elif y >= -300 and y <= -100 and not SPOTS_FILLED["Bottom Middle"]:
            
            draw_x(COORD_TO_SPOT["Bottom Middle"])
            SPOTS_FILLED["Bottom Middle"] = True
            PLACEMENT["Bottom Middle"] = "X"
    elif x >= -300 and x <= -100:
        turtle.onscreenclick(None)
        if y >= 100 and y <= 298 and not SPOTS_FILLED["Top Left"]:
            draw_x(COORD_TO_SPOT["Top Left"])
            SPOTS_FILLED["Top Left"] = True
            PLACEMENT["Top Left"] = "X"
        elif y >= -96 and y <= 99 and not SPOTS_FILLED["Middle Left"]:
            draw_x(COORD_TO_SPOT["Middle Left"])
            PLACEMENT["Middle Left"] = "X"
            SPOTS_FILLED["Middle Left"] = True
        elif y >= -300 and y <= -100 and not SPOTS_FILLED["Bottom Left"]:
            draw_x(COORD_TO_SPOT["Bottom Left"])
            SPOTS_FILLED["Bottom Left"] = True
            PLACEMENT["Bottom Left"] = "X"
    elif x >= 100 and x <= 300:
        turtle.onscreenclick(None)
        if y >= 100 and y <= 298 and not SPOTS_FILLED["Top Right"]:
            draw_x(COORD_TO_SPOT["Top Right"])
            SPOTS_FILLED["Top Right"] = True
        elif y >= -96 and y <= 99 and not SPOTS_FILLED["Middle Right"]:
            draw_x(COORD_TO_SPOT["Middle Right"])
            SPOTS_FILLED["Middle Right"] = True
        elif y >= -300 and y <= -100 and not SPOTS_FILLED["Bottom Right"]:
            draw_x(COORD_TO_SPOT["Bottom Right"])
            SPOTS_FILLED["Bottom Right"] = True
            
    spot = random.choice(list(COORD_TO_SPOT.keys()))
    for spot in SPOTS_FILLED:
        if win():
            turtle.write("YOU WIN!", font=("Verdana", 44, "normal"))
            break
        if not SPOTS_FILLED[spot]:
            turtle.onscreenclick(None)
            draw_circle(COORD_TO_SPOT[spot])
            SPOTS_FILLED[spot] = True
            break
        else:
            spot = random.choice(list(COORD_TO_SPOT.keys()))
  
    turtle.onscreenclick(get_mouse_click_coor)
        



    
    
        

    
def win():
    win = False
    if PLACEMENT["Top Middle"] == "X" and PLACEMENT["Middle Middle"] == "X" and PLACEMENT["Bottom Middle"] == "X":
        win = True
    elif PLACEMENT["Top Left"] == "X" and PLACEMENT["Middle Left"] == "X" and PLACEMENT["Bottom Left"] == "X":
        win = True
    elif PLACEMENT["Top Right"] == "X" and PLACEMENT["Middle Right"] == "X" and PLACEMENT["Bottom Right"] == "X":
        win = True
    elif PLACEMENT["Top Left"] == "X" and PLACEMENT["Top Middle"] == "X" and PLACEMENT["Top Right"] == "X":
        win = True
    elif PLACEMENT["Middle Left"] == "X" and PLACEMENT["Middle Middle"] == "X" and PLACEMENT["Middle Right"] == "X":
        win = True
    elif PLACEMENT["Bottom Left"] == "X" and PLACEMENT["Bottom Middle"] == "X" and PLACEMENT["Bottom Right"] == "X":
        win = True
    elif PLACEMENT["Bottom Right"] == "X" and PLACEMENT["Middle Middle"] == "X" and PLACEMENT["Top Left"] == "X":
        win = True
    elif PLACEMENT["Top Right"] == "X" and PLACEMENT["Middle Middle"] == "X" and PLACEMENT["Bottom Left"] == "X":
        win = True
    return win
    
    

   
    

    
        
            

            

        

   
        


def main():    
    
    initalize()
    turtle.tracer(False)
    draw_board()
    turtle.tracer(True)

    turtle.speed(6)
    
    turtle.onscreenclick(get_mouse_click_coor)
    
    

    input()

main()