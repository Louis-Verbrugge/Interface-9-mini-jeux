#from PIL import Image

import imageio # pip install imageio
import pygame
import sys
import random
import time



def transition_start(SCREEN, WIDTH, HEIGHT, snake):
    
    gif = imageio.get_reader('./image/image_main_snake.gif')

    # affichage des frames du GIF dans la fenêtre Pygame
    for frame in gif:
        # conversion de l'image en surface Pygame
        pygame_surface = pygame.surfarray.make_surface(frame)
        
        # affichage de la surface Pygame dans la fenêtre
        pygame_surface = pygame.transform.scale(pygame_surface, (WIDTH, HEIGHT))  # la taille de l'image fait tout la fenetre
        pygame_surface = pygame.transform.rotate(pygame_surface, 270) # je fais pivoter l'image 
        pygame_surface = pygame.transform.flip(pygame_surface, True, False)  # j'inverse l'image de gauche a droite 
        
        SCREEN.blit(pygame_surface, (0,0))
        pygame.display.flip()


    accu_red = 0
    direction = "rouge"
    nombre_tour = 0
    while nombre_tour != 19 :
        pygame.draw.rect(SCREEN, (accu_red, 0, 0), (snake[0][0]+5, snake[0][1]+6, taille-10, taille-15))
        pygame.display.update()
        
        
        if direction == "rouge":
            accu_red += 1
            if accu_red == 255:
                nombre_tour+=1
                direction = "noir"
            
        if direction == "noir":
            accu_red -= 1
            if accu_red == 0:
                nombre_tour+=1
                direction = "rouge"
                
        








def des_dessine_snake(SCREEN, snake):
    pygame.draw.rect(SCREEN, BLACK, (snake[len(snake)-1][0], snake[len(snake)-1][1], taille, taille))
    snake.pop(len(snake)-1)



def dessine_snake(SCREEN, snake):
    couleur = RED
    for elem in snake:
        if elem == snake[0]:# c'est la tete
            
            pygame.draw.rect(SCREEN, GREEN, (elem[0], elem[1], taille, taille), 8)
            pygame.draw.rect(SCREEN, RED, (elem[0]+5, elem[1]+6, taille-10, taille-15))
            couleur = GREEN
            
        else:
            pygame.draw.rect(SCREEN, couleur, (elem[0], elem[1], taille, taille))
        
     
        
def mouvement(snake, direction):
    if direction == "right": # mouvement gauche
        snake.insert(0, [snake[0][0]+taille, snake[0][1]])
        
                    
    elif direction == "left": # mouvement droite
        snake.insert(0, [snake[0][0]-taille, snake[0][1]])
             
                    
    elif direction == "down": # mouvement bas
        snake.insert(0, [snake[0][0], snake[0][1]+taille])
                    
    else: # mouvement haut
        snake.insert(0, [snake[0][0], snake[0][1]-taille])
    
    time.sleep(0.05)
    
def spon_bonbon(SCREEN, WIDTH, HEIGHT, snake, bonbon):   # bonbon = [coor_x, coor_y]  
    """
    je test si le snake touche un bonbon, si oui il faut respon un bonbon sinon le jeu continue
    """
    if snake[0][0] <= bonbon[0] <= snake[0][0]+taille and snake[0][1] <= bonbon[1] <= snake[0][1]+taille: # test en haut a gauche du cube
        pygame.draw.rect(SCREEN, BLACK, (bonbon[0], bonbon[1], taille, taille)) # je cache l ancien bonbon
        snake.insert(0, ([bonbon[0], bonbon[1]])) # le snake grandi
        coor_x = random.randint(taille, WIDTH-taille)
        coor_y = random.randint(taille, HEIGHT-taille)
        pygame.draw.rect(SCREEN, GREEN, (coor_x, coor_y, taille, taille)) # j affiche le nouveau bonbon
        bonbon = [coor_x, coor_y]
        
        
    if snake[0][0] <= bonbon[0]+taille <= snake[0][0]+taille and snake[0][1] <= bonbon[1] <= snake[0][1]+taille: # test en haut a droite du cube
        pygame.draw.rect(SCREEN, BLACK, (bonbon[0], bonbon[1], taille, taille)) # je cache l ancien bonbon
        snake.insert(0, ([bonbon[0], bonbon[1]])) # le snake grandi
        coor_x = random.randint(taille, WIDTH-taille)
        coor_y = random.randint(taille, HEIGHT-taille)
        pygame.draw.rect(SCREEN, GREEN, (coor_x, coor_y, taille, taille)) # j affiche le nouveau bonbon
        bonbon = [coor_x, coor_y]       
 
    if snake[0][0] <= bonbon[0] <= snake[0][0]+taille and snake[0][1] <= bonbon[1]+taille <= snake[0][1]+taille: # test en bas a gauche du cube
        pygame.draw.rect(SCREEN, BLACK, (bonbon[0], bonbon[1], taille, taille)) # je cache l ancien bonbon
        snake.insert(0, ([bonbon[0], bonbon[1]])) # le snake grandi
        coor_x = random.randint(taille, WIDTH-taille)
        coor_y = random.randint(taille, HEIGHT-taille)
        pygame.draw.rect(SCREEN, GREEN, (coor_x, coor_y, taille, taille)) # j affiche le nouveau bonbon
        bonbon = [coor_x, coor_y]          
    
    if snake[0][0] <= bonbon[0]+taille <= snake[0][0]+taille and snake[0][1] <= bonbon[1]+taille <= snake[0][1]+taille: # test en bas a droite du cube
        pygame.draw.rect(SCREEN, BLACK, (bonbon[0], bonbon[1], taille, taille)) # je cache l ancien bonbon
        snake.insert(0, ([bonbon[0], bonbon[1]])) # le snake grandi
        coor_x = random.randint(taille, WIDTH-taille)
        coor_y = random.randint(taille, HEIGHT-taille)
        pygame.draw.rect(SCREEN, GREEN, (coor_x, coor_y, taille, taille)) # j affiche le nouveau bonbon
        bonbon = [coor_x, coor_y]
        
    return bonbon
  

        
   

   
def defaite(snake, WIDTH, HEIGHT):  # pour perdre il faut que le snake sorte de la fenetre 

    
    if 0 <= snake[0][0] and snake[0][0]+taille <= WIDTH:
    
        if 0 <= snake[0][1] and snake[0][1]+taille <= HEIGHT:
            return True

    return False
    
    
   
   
def spon_fin(SCREEN, WIDTH, HEIGHT):
    fond_acceil = pygame.image.load('./image/image_main.jpg')
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0)) 
    
    
    image_pierre = pygame.image.load("./image/carre_blue.jpg")
    affiche_image_pierre = pygame.transform.scale(image_pierre, (50, 30))
    SCREEN.blit(affiche_image_pierre, (((WIDTH/10)*2)-25, ((HEIGHT/12)*4)-5))
    
    pygame.display.update()
    snake = [[-10, (HEIGHT/12)*4], [(WIDTH/10)*2, (HEIGHT/12)*4]]   
     
     
    while snake[0][0] < snake[1][0]:
        SCREEN.blit(fond_acceil, (0,0)) 
        SCREEN.blit(affiche_image_pierre, (((WIDTH/10)*2)-25, ((HEIGHT/12)*4)-5))
        pygame.draw.rect(SCREEN, GREEN, (snake[0][0]-20, snake[0][1], 40, 20))
        pygame.draw.rect(SCREEN, RED, (snake[0][0]+5, snake[0][1]+6, 10, 5))

        pygame.display.update()
        snake[0][0]+=0.1






WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

taille = 20
vitesse = 0.2








def main_snake(SCREEN, HEIGHT, WIDTH):
    print('ok')
    snake = [[(WIDTH/10)*2, (HEIGHT/12)*4], [(WIDTH/10)-20, (HEIGHT/12)]] # coor_x; coor_y  ( en px )
    transition_start(SCREEN, HEIGHT, WIDTH, snake)
    
    bonbon = []
    direction = "right" # il commence vers la droite
    
    
    # spon du premier bonbon:
    coor_x = random.randint(0, WIDTH-taille)
    coor_y = random.randint(0, HEIGHT-taille)
    pygame.draw.rect(SCREEN, GREEN, (coor_x, coor_y, taille, taille))
    bonbon = [coor_x, coor_y]
    
    while defaite(snake, WIDTH, HEIGHT):
        
        
        dessine_snake(SCREEN, snake)
        mouvement(snake, direction)
        pygame.display.update()
        des_dessine_snake(SCREEN, snake)
        bonbon = spon_bonbon(SCREEN, WIDTH, HEIGHT, snake, bonbon)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                mouv = False
                if event.key == pygame.K_LEFT: # clique a gauche
                    snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]-1])
                    direction = "left"
                    mouv = True
                    
                elif event.key == pygame.K_RIGHT: # clique a droite
                    snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]+1])
                    direction = "right"
                    mouv = True
                    
                elif event.key == pygame.K_DOWN: # clique a bas
                    snake.append([snake[len(snake)-1][0]+1, snake[len(snake)-1][1]])
                    direction = "down"
                    mouv = True
                    
                elif event.key == pygame.K_UP: # clique a haut
                    snake.append([snake[len(snake)-1][0]-1, snake[len(snake)-1][1]])  
                    direction = "up"
                    mouv = True
                
                if mouv: # pour ne pas recopier 4 fois la meme chose
                    des_dessine_snake(SCREEN, snake)


    spon_fin(SCREEN, WIDTH, HEIGHT)