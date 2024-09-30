import pgzrun

import random 

HEIGHT = 800
WIDTH = 800

message = ""

#Creating Alien character 
a1 = Actor("alien2")
a1.pos = 300,300

def draw():
    screen.clear()
    a1.draw()
    screen.draw.text(message,center = (300,10))

def move_alien():
    a1.x = random.randint(80,WIDTH-80)
    a1.y = random.randint(80,HEIGHT-80)

def on_mouse_down(pos):
    global message
    #checking the collition between actor a1 and the point of click
    if a1.collidepoint(pos):
        move_alien()
        message = "good shot"
    else:
        message = "Better luck next time"



move_alien()

pgzrun.go()