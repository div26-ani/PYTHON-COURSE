import pgzrun
from random import radiant

WIDTH = 1000
HEIGHT = 800

c = Actor('chick',(100,100))
w = Actor('walrus',(400,400))
cookie = Actor('cookie',(radiant(100,900), radiant(100,500)))
score = 0
speed = 5


def draw():
    screen.blit('bg',pos=(0,0))
    c.draw()
    w.draw()
    screen.draw.text("A Chiken Story", (10,10), color='red')
    screen.draw.text(f"Score: {score}",(900,10),color='red')
    cookie.draw()



def update():
    global score
    if keyboard.W:
        c.y -= speed
    elif keyboard.S:
        c.y += speed
    elif keyboard.A:
        c.x -= speed
    elif keyboard.D:
        c.x += speed

    if c.colliderect(cookie):
        score += 1
        cookie.pos = (radiant(100,90),radiant(100,500))

pgzrun.go()
