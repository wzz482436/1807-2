import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,600)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

	def __init__(self,imagename,speed=10):#speed=10,背景刷新的频率
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
		self.rect.bottom = 0
		maxvalue = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,maxvalue)
		self.speed = random.randint(1,5)
	def update(self):
		super().update()
		#判断敌机是否移除屏幕
		if self.rect.y >= SCREEN_RECT.height:
			#将精灵从所有组中删除
			self.kill()
			print('敌机摧毁')

class BackgroundSprite(GameSprite):

	def __init__(self,is_alt=False):
		self.imagename = './images/lalala.png'
		super().__init__(self.imagename)
		if is_alt:
			self.rect.y = -self.rect.height
	
	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
			


class Hero(GameSprite):
	"""英雄精灵"""
	def __init__(self):
	

		self.imagename = './images/hero2.png'
		super().__init__(self.imagename,0)#0速度

		self.rect.centerx = SCREEN_RECT.centerx


		self.rect.top = 550

		self.bullet_group = pygame.sprite.Group()
	def fire(self):
		print('发射子弹...')

		bullet = Bullet()#子弹精灵组
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.y = self.rect.top - 20
		# 3. 将精灵添加到精灵组
		self.bullet_group.add(bullet)

		bullet1 = Bullet()
		bullet1.rect.centerx = self.rect.centerx - 35
		bullet1.rect.y = self.rect.top +35
		self.bullet_group.add(bullet1)

		bullet2 = Bullet()
		bullet2.rect.centerx = self.rect.centerx + 35
		bullet2.rect.y = self.rect.top +35
		self.bullet_group.add(bullet2)

	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed1
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width

		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height

class Bullet(GameSprite):
	"""子弹精灵"""

	def __init__(self):
		self.imagename = "./images/bullet.png"

		super().__init__(self.imagename, -20)

	def __del__(self):
		print("轻轻地我走了")

	def update(self):

		super().update()

		# 判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom <=0:
			self.kill()
