import pygame
#精灵组
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,speed=1):
		super().__init__()
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y+=self.speed


class EnemySprite(GameSprite):
	def __init__(self):
		self.imagename = './images/enemy1.png'
		super().__init__(self.imagename)
	def update(self):
		super().update()

