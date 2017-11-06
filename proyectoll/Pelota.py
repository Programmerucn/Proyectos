import pygame
import random
import math

gravedad = 0.4
tamaño_pantalla = [850,480]

class Pelota(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/pelotas/"+sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 21
        self.velocidad_x = random.randint(4,7)
        self.velocidad_y = 0
        self.velocidad = math.sqrt((self.velocidad_x**2)+(self.velocidad_y**2))
        self.masa = 0

    def actualizar_posicion(self):

        self.velocidad_y += gravedad
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        if self.rect.right > tamaño_pantalla[0]:
            self.rect.right = tamaño_pantalla[0]

        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.top < 0:
            self.rect.top = 0
    def colision_circular(self,jugador):
        diferencia_x = -(self.rect.x - jugador.rect.x)
        diferencia_y = -(self.rect.y - jugador.rect.y)
        if diferencia_x > 0:
            if diferencia_y > 0:
                Angle = math.degrees(math.atan(diferencia_y / diferencia_x))
                self.velocidad_x = -self.velocidad* math.cos(math.radians(Angle))
                self.velocidad_y = -self.velocidad* math.sin(math.radians(Angle))
            elif diferencia_y < 0:
                Angle = math.degrees(math.atan(diferencia_y / diferencia_x))
                self.velocidad_x = -self.velocidad * math.cos(math.radians(Angle))
                self.velocidad_y = -self.velocidad * math.sin(math.radians(Angle))
        elif diferencia_x < 0:
            if diferencia_y > 0:
                Angle = 180 + math.degrees(math.atan(diferencia_y / diferencia_x))
                self.velocidad_x = -self.velocidad * math.cos(math.radians(Angle))
                self.velocidad_y = -self.velocidad * math.sin(math.radians(Angle))
            elif diferencia_y < 0:
                Angle = -180 + math.degrees(math.atan(diferencia_y / diferencia_x))
                self.velocidad_x = -self.velocidad * math.cos(math.radians(Angle))
                self.velocidad_y = -self.velocidad * math.sin(math.radians(Angle))
        elif diferencia_x == 0:
            if diferencia_y > 0:
                Angle = -90
            else:
                Angle = 90
                self.velocidad_x = self.velocidad * math.cos(math.radians(Angle))
                self.velocidad_y = self.velocidad * math.sin(math.radians(Angle))
        elif diferencia_y == 0:
            if diferencia_x < 0:
                Angle = 0
            else:
                Angle = 180
                self.velocidad_x = self.velocidad * math.cos(math.radians(Angle))
                self.velocidad_y = self.velocidad * math.sin(math.radians(Angle))

        print(self.rect.x,self.rect.y,jugador.rect.x,jugador.rect.y,self.velocidad_x,self.velocidad_y)
        self.rect.y += self.velocidad_y *1.5
        self.rect.x += self.velocidad_x *1.5