import pygame
import math
from Plataforma import Superficie
from Pelota import Pelota
from Jugador import Jugador
from Arco import Arco

#Movimiento pelota
#salto jugador
# UPDATES
# colisiones arco
#gravedad
#colision superficie
#ordenar codigo


#Investigar vectores
#Investigar gravedad, rotacion, friccion


pygame.init()
tamaño_pantalla = [850,480]

pantalla = pygame.display.set_mode(tamaño_pantalla)
fondo = pygame.image.load("imagenes/estadio2.jpg")

reloj = pygame.time.Clock()
main_loop = True

jugador = Jugador(75,370,'personajenathal.png')
grupoJugadores = pygame.sprite.Group()
grupoJugadores.add(jugador)

grupoSuperficiesVerticales = pygame.sprite.Group()

suelo = Superficie(0,tamaño_pantalla[1] - 40,tamaño_pantalla[0],40)
grupoSuperficiesVerticales.add(suelo)

techo = Superficie(0,0,tamaño_pantalla[0],1)
grupoSuperficiesVerticales.add(techo)


grupoSuperficiesHorizontales = pygame.sprite.Group()

pared_izquierda = Superficie(0,0,1,tamaño_pantalla[1]+1)
grupoSuperficiesHorizontales.add(pared_izquierda)

pared_derecha = Superficie(tamaño_pantalla[0]-1,0,1,tamaño_pantalla[1]-5)
grupoSuperficiesHorizontales.add(pared_derecha)

grupoArcos = pygame.sprite.Group()
arco_izq = Arco(-25,tamaño_pantalla[1] - 180,'arcoizquierdo.png')
arco_der = Arco(tamaño_pantalla[0]-100,tamaño_pantalla[1] - 180,'arcoderecho.png')
grupoArcos.add(arco_der)
grupoArcos.add(arco_izq)


pelota = Pelota(tamaño_pantalla[0]/2,tamaño_pantalla[1]/2,'p5.png')

while main_loop:
    reloj.tick(50)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            main_loop = False

    jugador.actualizar_posicion()
    pelota.actualizar_posicion()

    cabesazos = pygame.sprite.spritecollide(pelota,grupoJugadores,False,pygame.sprite.collide_circle)
    if cabesazos:
        pelota.colision_circular(jugador)

    rebote_v = pygame.sprite.spritecollide(pelota, grupoSuperficiesVerticales, False,)
    if rebote_v:
        pelota.rect.bottom = tamaño_pantalla[1]-36
        pelota.velocidad_y = -0.81*pelota.velocidad_y

    rebote_h = pygame.sprite.spritecollide(pelota, grupoSuperficiesHorizontales, False, )
    if rebote_h:
        pelota.velocidad_x =-0.9*pelota.velocidad_x

    # mostrar_jugadores funcion
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(jugador.image,(jugador.rect.x,jugador.rect.y))
    pantalla.blit(pelota.image, (pelota.rect.x, pelota.rect.y))
    pantalla.blit(suelo.image,(suelo.rect.x,suelo.rect.y))
    pantalla.blit(arco_izq.image, (arco_izq.rect.x, arco_izq.rect.y))
    pantalla.blit(arco_der.image, (arco_der.rect.x, arco_der.rect.y))


    #actualizar_jugadores funcion
    pygame.display.flip()

