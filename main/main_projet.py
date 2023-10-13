
import pygame
import sys

# DANS UN PREMIER TEMPS SI VOUS AVEZ PAS LA VIDEO DU GIF IL FAUT EXECUTER LE FICHIER "modifier_image.py"  !!!

sys.path.append('./code')


# je crée un lien entre ce fichier et tout les fichiers contenant les jeux :
from nim_pygame import*
from juste_prix_pygame import*
from demineur_pygame import*
from morpion_pygame import*
from jeu_2048 import*
from piere_feuille_ciseaux import*
from oiseau import*
from blackjack import*
from credit import*
from snake import*


WIDTH, HEIGHT = 1300, 1000 # 1200, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.display.set_caption(f"page principals")
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



# tuple qui contient les coordonnes des bouttons pour chaque jeu : 
def emplacement_buttonn():
    emplacement_button = []
    for y in range (3):
        for x in range (3):
            if x != 1 or y != 1:
                emplacement_button.append([WIDTH/10 + (WIDTH/10)*3*x, (WIDTH/10)*3 + (WIDTH/10)*3*x,   HEIGHT/12 + (HEIGHT/12)*4*y, (HEIGHT/12)*3 + (HEIGHT/12)*4*y])  # ( 'xx', yy' )
            
    return emplacement_button


emplacement_button = emplacement_buttonn()

#fond ecran:
fond_acceil = pygame.image.load('./image/image_main.jpg')
fond_acceil = fond_acceil.convert()
fond_acceil = pygame.transform.scale(fond_acceil, (WIDTH, HEIGHT))


# image du jeu 2048:
image_2048 = pygame.image.load("./image/image_2048.png")
affiche_image_2048 = pygame.transform.scale(image_2048, ((WIDTH/10)*2, (HEIGHT/12)*2))

# image du jeu tic tac toe:
image_tic_tac_toe = pygame.image.load("./image/image_tic-tac-toe.png")
affiche_image_tic_tac_toe = pygame.transform.scale(image_tic_tac_toe, ((WIDTH/10)*2, (HEIGHT/12)*2))         
   
# image du jeu de nim:
image_nim = pygame.image.load("./image/image_nim.png")
affiche_image_nim = pygame.transform.scale(image_nim, ((WIDTH/10)*2, (HEIGHT/12)*2))  

# image du juste prix:
image_juste_prix = pygame.image.load("./image/image_juste_prix.png")
affiche_image_juste_prix = pygame.transform.scale(image_juste_prix, ((WIDTH/10)*2, (HEIGHT/12)*2))

# image du demineur:
image_demineur = pygame.image.load("./image/image_demineur.png")
affiche_image_demineur = pygame.transform.scale(image_demineur, ((WIDTH/10)*2, (HEIGHT/12)*2))
         
# image du chifoumi:
image_chifoumi = pygame.image.load("./image/image_chifoumi.png")
affiche_image_chifoumi = pygame.transform.scale(image_chifoumi, ((WIDTH/10)*2, (HEIGHT/12)*2)) 

# image du oiseau:
image_oiseau = pygame.image.load("./image/image_oiseau.png")
affiche_image_oiseau = pygame.transform.scale(image_oiseau, ((WIDTH/10)*2, (HEIGHT/12)*2)) 

# image du blackjack:
image_blackjack = pygame.image.load("./image/image_blackjack.png")
affiche_image_blackjack = pygame.transform.scale(image_blackjack, ((WIDTH/10)*2, (HEIGHT/12)*2)) 
       
 
 
 
def affiche_jeu(SCREEN):
       
       
        
    SCREEN.blit(fond_acceil, (0,0))   # fond ecran
    
    SCREEN.blit(affiche_image_juste_prix, (WIDTH/10, (HEIGHT/12)))      # en haut a gauche
    SCREEN.blit(affiche_image_nim, ((WIDTH/10)*4, (HEIGHT/12)))         # en haut au milieu
    SCREEN.blit(affiche_image_demineur, ((WIDTH/10)*7, HEIGHT/12))      # en haut a droite
                
                
    SCREEN.blit(affiche_image_tic_tac_toe, (WIDTH/10, (HEIGHT/12)*5))   # en haut a gauche
    SCREEN.blit(affiche_image_2048, ((WIDTH/10)*7, (HEIGHT/12)*5))      # en haut a droite
                
                
    SCREEN.blit(affiche_image_chifoumi, ((WIDTH/10), (HEIGHT/12)*9))    # en haut a gauche
    SCREEN.blit(affiche_image_oiseau, ((WIDTH/10)*475, (HEIGHT/12)*9))  # en haut au milieu  
    SCREEN.blit(affiche_image_blackjack, ((WIDTH/10)*7, (HEIGHT/12)*9)) # en haut a droite
          
    #affiche snake:
    snake = [[(WIDTH/10)*2, (HEIGHT/12)*4], [(WIDTH/10)-20, (HEIGHT/12)]]
    pygame.draw.rect(SCREEN, GREEN, (snake[0][0]-20, snake[0][1], 40, 20))
    pygame.draw.rect(SCREEN, RED, (snake[0][0]+5, snake[0][1]+6, 10, 5))
       
    pygame.display.update() 
        
     
def main_projet_main(SCREEN):
    run = True
    
    affiche_jeu(SCREEN)
    
    while run:
        
        mouse = pygame.mouse.get_pos()
        
    
        for event in pygame.event.get():
            
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                for i in range (len(emplacement_button)):
                    if emplacement_button[i][0] <= mouse[0] <= emplacement_button[i][1] and emplacement_button[i][2] <= mouse[1] <= emplacement_button[i][3]:
                        joue = True
                        
                        if i == 0: # le jeu n°0 = jeu de min
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_juste_prix()
                            joue = True # oui il a joué !
                            
                        elif i == 1: # le jeu n°1 = juste prix
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_jeu_de_min()
                            joue = True # oui il a joué !
                            
                        elif i == 2: # le jeu n°2 = demineur
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_demineur()
                            joue = True # oui il a joué !
                            
                        elif i == 3:
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_morpion(nb_victoire)
                            joue = True # oui il a joué !
                            
                        elif i == 4:
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_2048()
                            joue = True # oui il a joué !

                        elif i == 5:
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_chifoumi()
                            joue = True # oui il a joué !
                            
                        elif i == 6:
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_oiseau()
                            joue = True # oui il a joué !
                            
                        elif i == 7:
                            pygame.quit() # je quitte l'affichage du menu pour jouer au jeu
                            main_blackjack()
                            joue = True # oui il a joué !
                        
                        
                        
                        if joue: # c'est pour pas recopier 9fois la meme chose...
                            pygame.quit() # je quitte l'affichage du jeu pour affichage le menu
                            
                            SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
                            pygame.init()
                            pygame.display.set_caption(f"page principals")
                            affiche_jeu(SCREEN)
                        
                        
                        


            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT: # clique a gauche
                    main_credit(SCREEN, HEIGHT, WIDTH)  
                    affiche_jeu(SCREEN) 
            
                elif event.key == pygame.K_RIGHT: # clique a gauche
                    print('ok')
                    main_snake(SCREEN, HEIGHT, WIDTH)
                    affiche_jeu(SCREEN)  
                    

main_projet_main(SCREEN)