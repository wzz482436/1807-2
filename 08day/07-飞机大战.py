import pygame

from txt import *

pygame.init()

clock = pygame.time.Clock()
i=0


pygame.display.set_mode((480,700))



hero_rect = pygame.Rect(180, 500, 120, 120)
#screen.blit(hero,herorect)
print(hero_rect.x)
print(hero_rect.y)
print(hero_rect.width)
print(hero_rect.height)


screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()


hero = pygame.image.load("./images/hero.gif")
screen.blit(hero,(180,500))
pygame.display.update()



enemy = EnemySprite()
enemy1 = EnemySprite()
enemy2 = EnemySprite()
enemy1.rect.x = 50
enemy1.rect.y = 100
enemy1.speed = 2
enemy_group = pygame.sprite.Group(enemy,enemy1,enemy2)


while True:
# 设置屏幕刷新帧率
	clock.tick(60)
	print(i)
	i += 1


	hero_rect.y -=3
	#覆盖背景
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)

	if hero_rect.bottom <= 0:
		hero_rect.top = 700
	enemy_group.update()#更新
	enemy_group.draw(screen)


	for event in pygame.event.get():
		# 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()
			# 直接退出系统
			exit()
	pygame.display.update()#更新


pygame.quit()
