import pygame
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

#=====================PLAYER=======================================
dinoimg = pygame.image.load("allosaurus.png")
dinoX = 0
dinoY = 270

def dino():
	screen.blit(dinoimg,(dinoX,dinoY))


#======================OBSTACLE IMAGES===========================
jellyfish=pygame.image.load("jellyfish.png")	
fish=pygame.image.load("angler.png")
octo=pygame.image.load("octopus.png")
shark=pygame.image.load("megashark.png")



#====================OBSTACLE POSTIONS=======================

def yvalue(x):
	if x==1:
		return 70
	elif x==2:
		return 270
	else:
		return 470
	
#OBSTACLE 1 JELLYFISH
ob1x=750
rl1=random.randint(1,3)
ob1y=0
def ob1(x):
		ob1y=yvalue(rl1)
		screen.blit(jellyfish,(x,ob1y))

#OBSTACLE 2 ANGLER FISH
ob2x=750
ob2y=0
rl2=random.randint(1,3)
def ob2(x):
		ob2y=yvalue(rl2)
		screen.blit(fish,(x,ob2y))

#OBSTACLE 3 OCTOPUS
ob3x=750
ob3y=0
rl3=random.randint(1,3)
def ob3(x):
		ob3y=yvalue(rl3)
		screen.blit(octo,(x,ob3y))

#OBSTACLE 4 SHARK
ob4x=750
ob4y=0
rl4=random.randint(1,3)
def ob4(x):
		ob4y=yvalue(rl4)
		screen.blit(shark,(x,ob4y))





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
 #=================BACKGROUND FIL====================================L
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
	dino()

#==============================OBSTACLE CALL==============================
	ob1(ob1x)
	if ob1x<0:
		ob1x=750
		rl1=random.randint(1,3)
	else:
		ob1x-=3
	
	ob2(ob2x)
	if ob2x<0:
		ob2x=750
		rl2=random.randint(1,3)
	else:
		ob2x-=4

	ob3(ob3x)
	if ob3x<0:
		ob3x=750
		rl3=random.randint(1,3)
	else:
		ob3x-=6

	ob4(ob4x)
	if ob4x<0:
		ob4x=750
		rl4=random.randint(1,3)
	else:
		ob4x-=7
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	pygame.display.update()
pygame.quit()