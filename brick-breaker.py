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
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
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
                (x*brickW) + 1 + (x*2),
                ((x+1)*brickW) + 1 + (x*2),
                (y*brickH) + 1 + (y*2),
                ((y+1)*brickH) + 1 + (y*2),
                ))

r = 7
ball = Ball(
            int(WIDTH/2),
            int(HEIGHT/2),
            r,
            (12 - r) / 2,
            (12 - r) / 2,
            YELLOW,
        )


BG = display.create_pen(0, 0, 0)

playing = True
win = False

while playing:
    display.set_pen(BG)
    display.clear()
    
    
    display.set_pen(brickCol)
    for brick in bricks:
        display.rectangle(brick.minx, brick.miny, brickW, brickH)
        
    if button_y.read() and paddle.x > 0:
        paddle.x -= 10
        
    if button_x.read() and (paddle.x + paddleW) < WIDTH:
        paddle.x += 10
    
    display.set_pen(BLUE)
    display.rectangle(paddle.x, paddleY, paddleW, paddleH)
    
    if len(bricks) == 0:
        playing = False
        
    ball.x += ball.dx
    ball.y += ball.dy

    xmax = WIDTH - ball.r
    xmin = ball.r
    ymax = HEIGHT - ball.r
    ymin = ball.r
        
    if ball.x >= paddle.x and ball.x <= paddle.x + paddleW and ball.y >= paddleY - paddleH:
        ball.dy *= -1

    if ball.x < xmin or ball.x > xmax:
        ball.dx *= -1

    if ball.y < ymin:
        ball.dy *= -1
    if ball.y > ymax:
        playing = False
        
        
    for brick in bricks:
        if ball.x >= brick.minx and ball.x <= brick.maxx and ball.y - ball.r >= brick.miny and ball.y - ball.r <= brick.maxy:
            ball.dy *= -1
            bricks.remove(brick)
    

    display.set_pen(ball.pen)
    display.circle(int(ball.x), int(ball.y), int(ball.r))
  

    display.update()
    time.sleep(0.015)
    

display.set_pen(BLACK)
display.clear()

if len(bricks) == 0:
    display.set_pen(GREEN)
    display.text("You Win!", 10, 10, WIDTH, 5)
    led.set_rgb(0,50,0)
else:
    display.set_pen(RED)
    display.text("Game Over!", 10, 10, WIDTH, 5)
    led.set_rgb(50,0,0)

display.update()
