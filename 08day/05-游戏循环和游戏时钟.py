import pygame

pygame.init()
clock = pygame.time.Clock()
i=0

pygame.display.set_mode((480,700))

hero_rect = pygame.Rect(100, 500, 120, 120)
print(hero_rect.x)
print(hero_rect.y)
print(hero_rect.width)
print(hero_rect.height)

screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()

hero = pygame.image.load("./images/hero.gif")
screen.blit(bg,(180,500))
pygame.display.update()

while True:
# 设置屏幕刷新帧率
	clock.tick(60)
	print(i)
	i += 1


	hero_rect.y -=10
	#覆盖背景
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)

	pygame.display.update()

pygame.quit()
