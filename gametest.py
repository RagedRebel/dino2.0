import pygame
from pygame import mixer
import random
import math
pygame.init()

screen_width=800
screen_height=600
bg_colour = (135, 206, 250)

#=====================TITLE AND ICON===============================
pygame.display.set_caption("Dino Game <3")
icon=pygame.image.load("velociraptor.png")
pygame.display.set_icon(icon)
#==================music===================
mixer.music.load("ruebbnen.mp3")
mixer.music.play(-1)
#=====================PLAYER=======================================
dinoimg = pygame.image.load("allosaurus.png")
dinoX = 0
dinoY = 270

def dino():
	screen.blit(dinoimg,(dinoX,dinoY))

#music for jumping
jump_Sound = mixer.Sound("jumpp.mp3")
jump_Sound.play()
#music for death
death_Sound = mixer.Sound("pewpew.mp3")
death_Sound.play()

#===========================SCREEN CREATION===========================
screen=pygame.display.set_mode((screen_width,screen_height))
run =True
clock = pygame.time.Clock()
backg = pygame.image.load("doraaaaaaaa.jpg").convert()
scroll = 0
tiles = math.ceil(screen_width / backg.get_width()) + 1

original_image = pygame.image.load("doraaaaaaaa.jpg")
resized_image = pygame.transform.scale(original_image, (800,600))
#=============================GAME LOOP==============================
while run:
	screen.fill((bg_colour))  
 #BACKGROUND FILL
	screen.blit(resized_image, (0,0))
	clock.tick(33)
	i = 0 
	while(i < tiles): 
		screen.blit(backg, (backg.get_width()*i 
                         + scroll, 0)) 
		i += 1
	scroll -= 6
	if abs(scroll) > backg.get_width(): 
		scroll = 0
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	dino()
	pygame.display.update()
pygame.quit()