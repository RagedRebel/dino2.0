import pygame
dinocolour = 255,255,255
DINOHEIGHT = 60
DINOWIDTH = 60
screen = pygame.display.set_mode((800,600))
image = pygame.image.load('Ples2.png')
X=300
Y=400
def dinos():
  screen.blit(image,(X,Y))
class Dinosaur:
  def __init__(self, surfaceHeight):
    self.x = 60
    self.y = 0
    self.yvelocity = 0
    self.height = DINOHEIGHT
    self.width = DINOWIDTH
    self.surfaceHeight = surfaceHeight
  def swimup(self): #When adding classes into function, the first parameter must be the parameter
    if(self.y == 0): #Only allow jumping if the dinosaur is on the ground to prevent mid air jumps.
      self.yvelocity = 500
  def swimdown(self): 
    if(self.y == 200): 
      self.yvelocity = -500
  def update(self, deltaTime): #Updates the y position of the dinosaur each second
    self.yvelocity += 0 #Gravity
    self.y += self.yvelocity * deltaTime
    if self.y < 0: #if the dinosaur sinks into the ground, make velocity and y = 0
      self.y = 0
      self.yvelocity = 0
    elif self.y > 200:
      self.y = 200
      self.yvelocity=0
  def draw(self,display):
    pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])