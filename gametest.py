import pygame
import random
pygame.init()

screen_width=800
screen_height=600

#=====================TITLE AND ICON===============================
pygame.display.set_caption("Dino Game")
icon=pygame.image.load("velociraptor.png")
pygame.display.set_icon(icon)


#======================OBSTACLE IMAGES===========================
jellyfish=pygame.image.load("jellyfish.png")	
fish=pygame.image.load("angler.png")


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
		

	



#===========================SCREEN CREATION===========================
screen=pygame.display.set_mode((screen_width,screen_height))
run =True


#=============================GAME LOOP==============================
while run:
	screen.fill((53, 118, 230))    #BACKGROUND FILL
	
#=======================OBSTACLES================================



	ob1(ob1x)
	if ob1x<0:
		ob1x=750
		rl1=random.randint(1,3)
	else:
		ob1x-=0.12
	
	ob2(ob2x)
	if ob2x<0:
		ob2x=750
		rl2=random.randint(1,3)
	else:
		ob2x-=0.15



	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False


	pygame.display.update() 
pygame.quit()