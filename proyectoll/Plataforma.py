import pygame

class Superficie(pygame.sprite.Sprite):
    def __init__(self, x, y, largo,alto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((largo,alto))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
