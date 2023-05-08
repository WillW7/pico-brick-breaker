import time
import random
from pimoroni import Button, RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
display.set_backlight(1.0)

WIDTH, HEIGHT = display.get_bounds()
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

led = RGBLED(6, 7, 8)
led.set_rgb(0,0,0)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
YELLOW = display.create_pen(245, 199, 32)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)
BLUE = display.create_pen(21, 49, 133)


class Ball:
    def __init__(self, x, y, r, dx, dy, pen):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.pen = pen
        
class Brick:
    def __init__(self, minx, maxx, miny, maxy):
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy
        

paddleW = 50
paddleH = 10
paddleY = HEIGHT - (paddleH) -1
        
class Paddle:
    def __init__(self, x):
        self.x = x

paddle = Paddle(int(WIDTH/2) - int(paddleW/2))
        
brickW = 25
brickH = 10
brickGap = 2
brickCol = display.create_pen(176, 44, 18)


bricks = []
for x in range(0,5):
    for y in range(0,5):
        bricks.append(
            Brick(
                # create 5 rows of 5 bricks as displayed in the readme
                # hint: 0,0 is top left
            )

r = 7
ball = Ball(
            int(WIDTH/2),
            int(HEIGHT/2),
            r,
            (12 - r) / 2,
            (12 - r) / 2,
            YELLOW,
        )
            
#defines the bounds of the screen the ball bounces off
xmax = WIDTH - ball.r
xmin = ball.r
ymax = HEIGHT - ball.r
ymin = ball.r


BG = display.create_pen(0, 0, 0)

playing = True
win = False

while playing:
    display.set_pen(BG)
    display.clear()
    
    
    display.set_pen(brickCol)
    #display all the bricks in bricks using display.rectangle(x,y,w,h)
        
    
    display.set_pen(BLUE)
    display.rectangle(paddle.x, paddleY, paddleW, paddleH)
            
     if button_y.read() and paddle.x > 0:
        #move the paddle to the left
        
    #do the same for button x moving the paddle right making sure the paddle doesnt fall off the screen
    
    #break from the loop if all the brokcs have been destroyed
    
    #change the balls postion
    #hint: add the change to its pos
    
    # if the ball hits the paddle bounce the ball in the opposite direction
    #hint: for dy... 1 and -1 are opposite directions

    #if the ball hits the side or top wall bounce in opposite direction
            
    #if the ball hits the bottom break from the loop
        
        
    for brick in bricks:
         #if the ball hits a brick destroy it and bounce back
    

    display.set_pen(ball.pen)
    display.circle(int(ball.x), int(ball.y), int(ball.r))
  

    display.update()
    time.sleep(0.015) #how often to check for input (also effects speed of ball)
    

display.set_pen(BLACK)
display.clear()

# when game is over display win/lose msg on display depending on how the game ended


display.update()
