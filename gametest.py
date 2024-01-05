import pygame
pygame.init()

screen_width=800
screen_height=600

#=====================TITLE AND ICON===============================
pygame.display.set_caption("Dino Game")
icon=pygame.image.load("velociraptor.png")
pygame.display.set_icon(icon)




#===========================SCREEN CREATION===========================
screen=pygame.display.set_mode((screen_width,screen_height))

run =True


#=============================GAME LOOP==============================
while run:
	screen.fill((53, 118, 230))    #BACKGROUND FILL
	
	

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	pygame.display.update()
  
pygame.quit()