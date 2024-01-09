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
font = pygame.font.SysFont('tahoma', 52, pygame.font.Font.bold)

#==================MUSIC=======================================
mixer.music.load("ruebbnen.mp3")
mixer.music.play(-1)

#=====================PLAYER=======================================
dinoimg = pygame.image.load("allosaurus.png")
dinoX = 20
dinoY = 270

def dino(x,y):
	screen.blit(dinoimg,(x,y))


#======================OBSTACLE IMAGES===========================
jellyfish=pygame.image.load("jellyfish.png")	
fish=pygame.image.load("angler.png")
octo=pygame.image.load("octopus.png")
shark=pygame.image.load("shark.png")



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
		y1=yvalue(rl1)
		screen.blit(jellyfish,(x,ob1y))
		return y1
#OBSTACLE 2 ANGLER FISH
ob2x=750
ob2y=0
rl2=random.randint(1,3)
def ob2(x):
		y2=yvalue(rl2)
		screen.blit(fish,(x,ob2y))
		return y2

#OBSTACLE 3 OCTOPUS
ob3x=750
ob3y=0
rl3=random.randint(1,3)
def ob3(x):
		y3=yvalue(rl3)
		screen.blit(octo,(x,ob3y))
		return y3
		

#OBSTACLE 4 SHARK
ob4x=750
ob4y=0
rl4=random.randint(1,3)
def ob4(x):
		y4=yvalue(rl4)
		screen.blit(shark,(x,ob4y))
		return y4

#=============================COLLIIONS============================
def CollisionCheck(x1,y1,x2,y2):
	distance=math.sqrt((math.pow(x2-x1,2))+(math.pow(y2-y1,2)))	
	if distance<27:
		return True
	else:
		return False

#==============================SCORE=====================================
	
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 40)

    def increase(self):
        self.value +=1


    def renderscore(self):
        score_text = self.font.render(f"Score: {self.value}", True, (0,0,0))
        return score_text

	
#===============================GAME OVER===================================
def game_over():
	text = font.render("Game Over", True,(0,0,0)) 
	screen.blit(text, (270 ,270))
	pygame.display.update()
	pygame.time.delay(2000)

#================music for jumping===================
jump_Sound = mixer.Sound("jumpp.mp3")

#=========music for death===================================
death_Sound = mixer.Sound("pewpew.mp3")

#===========================SCREEN CREATION===========================
		
screen=pygame.display.set_mode((screen_width,screen_height))
run =True
clock = pygame.time.Clock()
backg = pygame.image.load("doraaaaaaaa.jpg").convert()
scroll = 0
tiles = math.ceil(screen_width / backg.get_width()) + 1

original_image = pygame.image.load("doraaaaaaaa.jpg")
resized_image = pygame.transform.scale(original_image, (800,600))
score = Score()

#=============================GAME LOOP==============================
while run:
	screen.fill((bg_colour))  
 #=================BACKGROUND FIL====================================L
	screen.blit(resized_image, (0,0))
	clock.tick(33)
	i = 0 
	while(i < tiles): 
		screen.blit(backg, (backg.get_width()*i + scroll, 0)) 
		i += 1
	scroll -= 6
	if abs(scroll) > backg.get_width(): 
		scroll = 0
	
#========================SCORE COUNT===================================
	score_text = score.renderscore()
	screen.blit(score_text, (20, 20))
#==========================DINO MOVEMENT===============================
	
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_w:
				jump_Sound.play()
				dinoY-=200
			if event.key==pygame.K_s:
				jump_Sound.play()
				dinoY+=200
		if event.type==pygame.QUIT:
			run=False

	if dinoY<0:
		dinoY+=100						#BOUNDARY SETTING
	elif dinoY>550:
		dinoY-=100

	dino(dinoX,dinoY)


#==============================OBSTACLE CALLS==============================
	ob1y=ob1(ob1x)
	if ob1x<0:
		ob1x=750
		rl1=random.randint(1,3)
		score.increase()
	else:
		ob1x-=6
	
	ob2y=ob2(ob2x)
	if ob2x<0:
		ob2x=750
		rl2=random.randint(1,3)
		score.increase()
	else:
		ob2x-=8

	ob3y=ob3(ob3x)
	if ob3x<0:
		ob3x=750
		rl3=random.randint(1,3)
		score.increase()
	else:
		ob3x-=11

	ob4y=ob4(ob4x)
	if ob4x<0:
		ob4x=750
		rl4=random.randint(1,3)
		score.increase()
	else:
		ob4x-=13

#============================COLLLISION CHECKS==============================
	c1=CollisionCheck(dinoX,dinoY,ob1x,ob1y)
	c2=CollisionCheck(dinoX,dinoY,ob2x,ob2y)
	c3=CollisionCheck(dinoX,dinoY,ob3x,ob3y)
	c4=CollisionCheck(dinoX,dinoY,ob4x,ob4y)
	if c1 or c2 or c3 or c4:
		death_Sound.play()
		pygame.mixer.music.stop()
		game_over()
		break

	pygame.display.update()
pygame.quit()