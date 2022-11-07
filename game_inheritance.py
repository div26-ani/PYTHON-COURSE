from random import randiant as ri
import pgzrun

WIDTH = 800
HEIGHT = 500

# all the class logic
class Player(Actor):
    

def _init_(self, image, speed=5):
    pos = ri(0, WIDTH), ri(0,HEIGHT) #generate a random x,y coordinate
    super()._init_(image, pos) #call the parent class constructor and pass image and pos
    self.speed = speed # add a new instance variable 


def move(self):
    if keyboard.W:
        self.y -= self.speed
    elif keyboard.S:
        self.y += self.speed
    elif keyboard.A:
        self.x -= self.speed
        self.angle = +10
    elif keyboard.D:
        self.x += self.speed
        self.angle = -10
    else:
        self.angle = 0

def check_boundary(self):
    pass

# main game code
P = Player('ironman')

def draw():
    screen.fill('black')
    P.draw()

def update():
    P.move
    P.check_boundary()

pgzrun.go()






