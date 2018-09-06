import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,600)

#刷新帧率
FRAME_PER_SEC = 60
#敌机事件的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

#子弹事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1

#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy0_down1.png')
bg2 = pygame.image.load('./images/enemy0_down2.png')
bg3 = pygame.image.load('./images/enemy0_down3.png')
bg4= pygame.image.load('./images/enemy0_down4.png')

#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):

	def __init__(self,imagename,speed=10):#speed=10,背景刷新的频率
		super().__init__()
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y+=self.speed

class Enemy(GameSprite):

	def __init__(self):
		self.imagename = './images/enemy1.png'
		super().__init__(self.imagename)
		self.speed  = random.randint(1,5)

		maxvalue = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,maxvalue)#随机位置

		self.rect.bottom = 0

		self.down_index = 0 #敌机销毁图片索引

	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			self.kill()

class Background(GameSprite):

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
		self.speed1 = 0

		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

		#子弹精灵族
		self.bullet_group = pygame.sprite.Group()

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



		

	def fire(self):
		bullet = Bullet()#子弹精灵组
		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx

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

#创建子弹精灵

class Bullet(GameSprite):
	"""子弹精灵"""

	def __init__(self):
		self.imagename = "./images/bullet.png"

		super().__init__(self.imagename, -20)

	def __del__(self):
		print("轻轻地我走了")

	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()

class Soruce(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		


	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()

