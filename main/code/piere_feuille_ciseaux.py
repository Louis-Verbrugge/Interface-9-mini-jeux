import pygame
import sys
import random
import time


def affiche_resultat(SCREEN, resul_utilisateur, resul_bot, resultat, mouvement, vic):
    mouvement.append([resul_utilisateur, resul_bot])
    if len(mouvement) == 6:
        mouvement.pop(0)
    
    
    
    if resul_utilisateur == "pierre" and resul_bot == "ciseaux":
        resultat[0] += 1
        affiche_victoire(SCREEN, resultat, "VICTOIRE", mouvement, vic)
    
    elif resul_utilisateur == "feuille" and resul_bot == "pierre":
        resultat[0] += 1
        affiche_victoire(SCREEN, resultat, "VICTOIRE", mouvement, vic)
    
    elif resul_utilisateur == "ciseaux" and resul_bot == "feuille":
        resultat[0] += 1
        affiche_victoire(SCREEN, resultat, "VICTOIRE", mouvement, vic)
    
    elif resul_bot == resul_utilisateur:
        affiche_victoire(SCREEN, resultat, "EGALITE", mouvement, vic)
    
    else:
        resultat[1] += 1
        affiche_victoire(SCREEN, resultat, "DEFAITE", mouvement, vic)
    
    
    
    
    

def choix_bot(symbole):
    choix = random.randint(0, len(symbole)-1)
    return symbole[choix]


def affiche_debut_game(SCREEN, emplacement_zone):
    
    for i in range (len(emplacement_zone)-1):
        pygame.draw.line(SCREEN, BLACK, (emplacement_zone[i][1], HEIGHT/5), (emplacement_zone[i][1], HEIGHT), 3)
    pygame.draw.line(SCREEN, BLACK, (0,  HEIGHT/5), (WIDTH, HEIGHT/5), 3)
    
    # image pierre:
    image_pierre = pygame.image.load("./image/simbole_pierre.png")
    affiche_image_pierre = pygame.transform.scale(image_pierre, (200, 200))
    SCREEN.blit(affiche_image_pierre, (WIDTH/10, HEIGHT/2))
    
    
    # image feuille:
    image_feuille = pygame.image.load("./image/simbole_feuille.png")
    affiche_image_feuille = pygame.transform.scale(image_feuille, (200, 200))
    SCREEN.blit(affiche_image_feuille, (WIDTH/2.35, HEIGHT/2))
    
    # image ciseau:
    image_ciseau = pygame.image.load("./image/simbole_ciseau.png")
    affiche_image_ciseau = pygame.transform.scale(image_ciseau, (200, 200))
    SCREEN.blit(affiche_image_ciseau, (WIDTH/2.35+((WIDTH/2.35)-(WIDTH/10)), HEIGHT/2))
    
    pygame.display.update()





def affiche_victoire(SCREEN, resultat, qui_gagne, mouvement, vic):
    vic.append(qui_gagne)
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT/5))
    
    
    # affiche en haut au centre il y a combien a combien, exemple ( 5 - 8 )
    affiche_resultatt = pygame.font.SysFont("bahnschrift", int((HEIGHT/5)/2)).render(f"{str(resultat[0])} - {str(resultat[1])}", True, "black")
    SCREEN.blit(affiche_resultatt, ((WIDTH/2)-(HEIGHT/5)/2, (HEIGHT/5)/2))
    
    # affiche en haut a droite le resultat de la manche, exemple ( VICTOIRE )
    affiche_qui_gagne = pygame.font.SysFont("bahnschrift", int((HEIGHT/5)/4)).render(qui_gagne, True, "black")
    SCREEN.blit(affiche_qui_gagne, (WIDTH-(HEIGHT/4), (HEIGHT/5)/2))
    
    # affiche les lag en haut a gauche, exemple ( vous avez perdu pierre, papier )
    
 
        
    #for elem in mouvement:
    for i in range (len(mouvement)):
        
        affiche_log = pygame.font.SysFont("bahnschrift", int((HEIGHT/5)/8)).render(f"( {mouvement[i][0]}-{mouvement[i][1]} )", True, "black")
        SCREEN.blit(affiche_log, (0, (HEIGHT/5)/8+((HEIGHT/5)/8)*i))
    
    
    pygame.display.update()
    
    
    
    
    
    
    

WIDTH, HEIGHT = 1300, 1100 #1600, 800


pygame.display.set_caption("Chifoumi") #titre de la page, fin  pas sur 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

symbole = ["pierre", "feuille", "ciseaux"]

emplacement_zone = [[0, WIDTH/3], [WIDTH/3, WIDTH/3+WIDTH/3], [WIDTH/3+WIDTH/3, WIDTH]]




def main_chifoumi():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()
    resultat = [0, 0] # utilisateur; bot
    mouvement = []
    vic = []

    SCREEN.fill(WHITE)
    
    affiche_debut_game(SCREEN, emplacement_zone)
    
    run = True
    while run:
        
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # 3 = clic RIGHT
                for i in range (len(emplacement_zone)):
                    if emplacement_zone[i][0] <= mouse[0] <= emplacement_zone[i][1] and HEIGHT/5 <= mouse[1]:
                        resul_bot = choix_bot(symbole)
                        print(f"clique dans la zone n°{i+1}, donc vous avez choisi {symbole[i]} et le bot : {resul_bot}")

                        
                        affiche_resultat(SCREEN, symbole[i], resul_bot, resultat, mouvement, vic)
                        print(resultat)

        