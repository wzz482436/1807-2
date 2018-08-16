
import pygame
from txt import *
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class PlaneGame(object):
	"""飞机大战主游戏"""

	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()#创建游戏时钟
		self.__create_sprites()#调用私有方法,精灵和精灵组的创建
		#self.enemy_group = pygame.sprite.Group(bg1,bg2)
		
		#敌机出现的频率
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1500)
		#记录事件的频率
		pygame.time.set_timer(HERO_FIRE_EVENT, 500)
	def start_game(self):
		print("开始游戏...")
		while True:
			# 1. 设置刷新帧率
			self.clock.tick(60)

			# 2. 事件监听
			self.__event_handler()

			# 3. 碰撞检测
			self.__check_collide()

			# 4. 更新精灵组
			self.__update_sprites()

			# 5. 更新屏幕显示
			pygame.display.update()
	def __create_sprites(self):
		bg1 = BackgroundSprite()
		bg2 = BackgroundSprite()
		bg2.rect.y = -bg2.rect.height
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
	
	def __event_handler(self):
		"""事件监听"""

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print('敌机出场...')
				enemy = EnemySprite()
				self.enemy_group.add(enemy)
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 10
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -10
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -10
			self.hero.speed = 0
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 10
			self.hero.speed = 0
		else:
			self.hero.speed = 0
			self.hero.speed1 = 0
	def __check_collide(self):
		"""碰撞检测"""

		# 1. 子弹摧毁敌机
		pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group, True, True)

		# 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

		# 判断列表时候有内容
		if len(enemies) > 0:
			print(enemies)
			# 让英雄牺牲
			self.hero.kill()

			# 结束游戏
			PlaneGame.__game_over()




	def __update_sprites(self):
		"""更新精灵组"""
		self.bg_group.update()
		self.bg_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

	@staticmethod
	def __game_over():
		"""游戏结束"""

		print("游戏结束")
		pygame.quit()
		exit()


if __name__ == '__main__':
	# 创建游戏对象
	game = PlaneGame()

	# 开始游戏
	game.start_game()

