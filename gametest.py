import pygame
pygame.init()

screen_width=800
screen_height=600

#title and icon
pygame.display.set_caption("Dino Game")
icon=pygame.image.load("velociraptor.png")
pygame.display.set_icon(icon)

#player image
playerimg=pygame.image.load("shark.png")
px=120
py=270
def shark(x,y):
	screen.blit(playerimg,(x,y))


#screen creation
screen=pygame.display.set_mode((screen_width,screen_height))

run =True
player=pygame.Rect((300,250,50,50))

#game loop
while run:
	screen.fill((53, 118, 230))    #background fill
	pygame.draw.rect(screen,(200,200,110),player)
	shark(px,py)
	
	key=pygame.key.get_pressed()
	if key[pygame.K_a]==True:
		player.move_ip(-1,0)

	elif key[pygame.K_d]==True:
		player.move_ip(1,0)
	elif key[pygame.K_w]==True:
		player.move_ip(0,-1)

	elif key[pygame.K_s]==True:
		player.move_ip(0,1)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False


	pygame.display.update()   #updating the changes to the screen

pygame.quit()