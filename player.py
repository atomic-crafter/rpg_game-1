import pygame

class Player:


	def __init__(self,z):
		self.loop = 0
		self.zoom = z
		self.player_animation = [pygame.image.load('rpg-pack/chars/gabe/gabe-run1.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run2.png')
		,pygame.image.load('rpg-pack/chars/gabe/gabe-run3.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run4.png'),
		pygame.image.load('rpg-pack/chars/gabe/gabe-run5.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run6.png'),
		pygame.image.load('rpg-pack/chars/gabe/gabe-run7.png')]
		self.health = 20
		self.hunger = 0
		self.x = 0
		self.y = 0
		



	def set_pos(self,x,y):
		self.x = x
		self.y = y

	def draw(self):
		pass

	def move(self,dx,dy):
		self.x += dx
		self.y += dy
		#print("joueur :",self.x," , ",self.y )


	def draw(self, screen,x,y):
		screen.blit(pygame.transform.scale(self.player_animation[self.loop],(16*self.zoom,16*self.zoom)),(16*self.zoom*(self.x-x),16*self.zoom*(self.y-y)))
		

	def animate(self):
		self.loop +=1
		if self.loop >= len(self.player_animation):
			self.loop = 0

		#screen.blit(self.player_animation[self.loop],(player_x,player_y))



