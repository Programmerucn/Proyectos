import pygame


tamaño_pantalla = [850,480]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/personajes/"+sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.radius = 33


    def actualizar_posicion(self):
        self.velocidad_x = 0
        self.velocidad_y = 0
        estado_tecla = pygame.key.get_pressed()

        if estado_tecla[pygame.K_RIGHT]:
                self.velocidad_x = 6

        elif estado_tecla[pygame.K_LEFT]:
                self.velocidad_x = -6

        elif estado_tecla[pygame.K_UP]:
            self.rect.y -= 20

        self.rect.x += self.velocidad_x

        if self.rect.right > tamaño_pantalla[0]:
            self.rect.right = tamaño_pantalla[0]
        elif self.rect.left < 0:
            self.rect.left = 0




