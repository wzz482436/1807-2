import pygame

pygame.init()

pygame.display.set_mode((480,700))

hero_rect = pygame.Rect(100, 500, 120, 126)
print(hero_rect.x)
print(hero_rect.y)
print(hero_rect.width)
print(hero_rect.height)

while True:
	pass

pygame.quit()
