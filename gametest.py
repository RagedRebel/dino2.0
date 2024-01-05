import pygame
import random
pygame.init()

screen_width=800
screen_height=600

#=====================TITLE AND ICON===============================
pygame.display.set_caption("Dino Game")
icon=pygame.image.load("velociraptor.png")
pygame.display.set_icon(icon)


#======================OBSTACLE IMAGES========================
jellyfish=pygame.image.load("jellyfish.png")
ob1x=750
ob1y=random.randint(1,3)
def ob1(x,y):
	if y==2:
		yy=270
		screen.blit(jellyfish,(x,yy))
	elif y==1:
		yy=70
		screen.blit(jellyfish,(x,yy))
	else:
		yy=470
		screen.blit(jellyfish,(x,yy))

	



#===========================SCREEN CREATION===========================
screen=pygame.display.set_mode((screen_width,screen_height))

run =True


#=============================GAME LOOP==============================
while run:
	screen.fill((53, 118, 230))    #BACKGROUND FILL
	
	#=======================OBSTACLES================================



	ob1(ob1x,ob1y)


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False


	pygame.display.update() 
pygame.quit()