import pygame,sys
from pygame.locals import *

def rango(vertices,posX,posY):
    for vertice in vertices:
        for i in range(-10,10):
            if (posX+i) == (vertice[0]):
                for i in range(-10,10):
                    if (posY+i) == (vertice[1]):
                        return True, vertice
    return False , None


def mover_vertice(lista,old_vertice,new_vertice):
    for vertice in lista:
        for i in range(-10,10):
            if (old_vertice[0]+i) == (vertice[0]):
                for i in range(-10,10):
                    if (old_vertice[1]+i) == (vertice[1]):
                        lista.remove(vertice)
                        aux = vertice
                        break
    lista.append(new_vertice)
    return lista

            
            
def actualizar_aristas(aristas,old_arista,new_arista):
    pass
    
pygame.init()

size = (800,500)

ventana = pygame.display.set_mode(size) 
pygame.display.set_caption("Hola mundo")

posX,posY = 10,5

blanco = (255,255,255)

posX_i,posY_i = -1,-1
posX_f,posY_f = -1,-1

vertices = []
dibujar_i = False
dibujar_f = False
mouse = False
BLACK = (0,0,0)
aristas = []
lis = []
diccionario = {}
while True:

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()    
            
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_x:
                posX_i,posY_i =pygame.mouse.get_pos()
            elif evento.key == K_c:
                posX_f,posY_f =pygame.mouse.get_pos()
            elif evento.key == K_z:
                posX_c,posY_c =pygame.mouse.get_pos()
                vertices.append((posX_c,posY_c))

            elif evento.key == K_b:
                pos = pygame.mouse.get_pos()
                ran = rango(vertices,pos[0],pos[1])
                if ran[0] == True:
                    vertices.remove(ran[1])
                    for i in range(len(aristas)):
                        for j in range(len(aristas[i])):
                            if aristas[i][j] == ran[1]:
                                aristas.remove(aristas[i])
                
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            aux_c = pygame.mouse.get_pos()
            if rango(vertices,aux_c[0],aux_c[1])[0]:
                for i in vertices:
                    if (rango(vertices,aux_c[0],aux_c[1])[0]):
                        aux_c = rango(vertices,aux_c[0],aux_c[1])[1]
                        mouse = True
            else:
                vertices.append((aux_c[0],aux_c[1]))
                    
        elif evento.type == pygame.MOUSEBUTTONUP:
            aux_d = pygame.mouse.get_pos()
            if mouse == True:
                mover_vertice(vertices,aux_c,aux_d)
                for i in range(len(aristas)):
                    for j in range(len(aristas[i])):
                        if aristas[i][j] == aux_c:
                            aristas[i][j] = aux_d
                mouse = False
                
                
        ventana.fill(BLACK)
        for i in aristas:
            pygame.draw.line(ventana,(50,2,90), (i[0][0],i[0][1]),(i[1][0],i[1][1]),5)
        
        for i in vertices:
            pygame.draw.circle(ventana,(120,60,10),(i),10)
            
        
            #diccionario[(i[0],i[1])]=[(i[2],i[3])]
        
                
        if posX_f != -1 and posX_i != -1:
            dibujar_i = rango(vertices,posX_i,posY_i)
            dibujar_f = rango(vertices,posX_f,posY_f)
            if (dibujar_i[0] and dibujar_f[0]):
                aux = [(dibujar_i[1][0],dibujar_i[1][1]),(dibujar_f[1][0],dibujar_f[1][1])]
                aristas.append(aux)

                dibujar_i = False
                dibujar_f = False
            posX_i,posY_i = -1,-1
            posX_f,posY_f = -1,-1



    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
