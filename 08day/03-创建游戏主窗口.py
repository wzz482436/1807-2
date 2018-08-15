import pygame

pygame.init()

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

while True:
	pass

pygame.quit()
