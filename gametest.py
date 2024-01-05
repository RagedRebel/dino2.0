import pygame
pygame.init()

screen_width=800
screen_height=600

#=====================TITLE AND ICON===============================
pygame.display.set_caption("Dino Game")
icon=pygame.image.load("velociraptor.png")
pygame.display.set_icon(icon)


#======================OBSTACLE IMAGES========================
jellyfish=pygame.image.load("jellyfish.png")
ob1x=300
ob1y=300
def ob1(x,y):
	screen.blit(jellyfish,(x,y))



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