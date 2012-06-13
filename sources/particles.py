import random 
import common_pygame
import load_resources

single_sprites=load_resources.single_sprites
pygame = common_pygame.pygame
screen= common_pygame.screen

explosions = list()

#size : 1 : asteroids, 2: ships, 3: boss
def addExplosion ( x, y, size):
	if size==1:
		nbParticles =  random.randrange(50, 100)
	if size==2:
		nbParticles =  random.randrange(150, 250)
	if size==3:
		nbParticles =  random.randrange(250, 550)
	
	particleList=list()
	
	for i in range(nbParticles):
		directionx=30
		directiony=0
		smoothing=15
		while directionx+directiony<=-smoothing or directionx+directiony>=smoothing or directionx-directiony<=-smoothing or directiony-directionx <=-smoothing :
			directionx = random.randrange(-10, 10)
			directiony =random.randrange(-10, 10)
		
		whatsprite=random.randrange(1, 5)
		print (whatsprite)
		spritename= "particle" + str(whatsprite) + ".png"
		sprite = single_sprites[spritename]
		#x position, y position, directionx, directiony, time, sprite size, sprite
		particleList.append((x, y, directionx, directiony, 0, sprite.get_width(), sprite ))
	
	explosions.append(particleList)

def determine(k):
	(x, y, directionx, directiony, time, size, sprite) = k
	if time > 60:
		return False
	return True

def blitAndUpdate():
	for i in range(len(explosions)):
		#delete the particles that are too old
		explosions[i][:]=[k for k in explosions[i] if determine(k)]
		for j in range(len(explosions[i])):
			#blit the concerned particle
			(x, y, directionx, directiony, time, size, sprite) = explosions[i][j]
			if size>0 and time%2 ==0:
				size=size-1
			
			toblit =  pygame.transform.scale(sprite,( size, size))
			screen.blit(toblit, (x,y))
			
			x=x+directionx
			y=y+directiony
			time=time+1
			explosions[i][j]=(x, y, directionx, directiony, time, size, sprite)
			
