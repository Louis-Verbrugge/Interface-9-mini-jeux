import pygame
import sys
import random
import time

def affiche_resultat(resul_utilisateur, resul_bot):
    if resul_utilisateur == "pierre" and resul_bot == "ciseaux":
        return "VICTOIRE"
    
    elif resul_utilisateur == "feuille" and resul_bot == "pierre":
        return "VICTOIRE"
    
    elif resul_utilisateur == "ciseaux" and resul_bot == "feuille":
        return "VICTOIRE"
    
    elif resul_bot == "pierre" and resul_utilisateur == "ciseaux":
        return "defaite"
    
    elif resul_bot == "feuille" and resul_utilisateur == "pierre":
        return "defaite"
    
    elif resul_bot == "ciseaux" and resul_utilisateur == "feuille":
        return "defaite"
    
    return "continue"

def choix_bot(symbole):
    
    choix = random.randint(0, len(symbole)-1)
    return symbole[choix]







def affiche_fin_partie(resultat_fin_partie):  
    if resultat_fin_partie == "VICTOIRE":
        fond = pygame.image.load('./victoire_carss.jpg') 
        couleur= "black"  

    else:
        fond = pygame.image.load('./lapin_pendu_defaite.jpg')
        couleur= "white"

    run_affice_fin = True
    while run_affice_fin:

    

        test_affiche_win = pygame.font.SysFont("bahnschrift", 100).render(resultat_fin_partie, True, couleur)  # affiche le gagnant !
        win = test_affiche_win.get_rect(center=(WIDTH/4, HEIGHT/3))  # c'est la position ou j 'affiche le gagnant
        
                        
        recommencer_une_partie = pygame.font.SysFont("bahnschrift", 30).render("cliquer pour RECOMMENCER !", True, "white") # affiche si le joueur veut refaire une partie !
        restart = recommencer_une_partie.get_rect(center=(WIDTH-200, HEIGHT-100))  # affiche la position du boutton !


        fond = fond.convert()
        SCREEN.blit(fond, (0,0))        
        fond = fond.convert()
        SCREEN.blit(fond, (0,0))
        SCREEN.blit(test_affiche_win, win)  
        SCREEN.blit(recommencer_une_partie, restart)

        mouse = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
            if event.type == pygame.MOUSEBUTTONDOWN: #je test si il y a un clique sur le boutton pour recommence une partie 
                if WIDTH-420 <= mouse[0] <= WIDTH and HEIGHT-120 <= mouse[1] <= HEIGHT: 
                    main_chifoumi()
                    run_affice_fin = False

    print('LE programme est fini !') 




def affiche_debut_game(emplacement_zone):
    SCREEN.fill(RED)
    for i in range (len(emplacement_zone)):
        pygame.draw.line(SCREEN, WHITE, (emplacement_zone[i][1], 0), (emplacement_zone[i][1], HEIGHT), 3)




WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

pygame.display.set_caption("Chifoumi") #titre de la page, fin  pas sur 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
symbole = ["pierre", "feuille", "ciseaux"]

emplacement_zone = [[0, WIDTH/3], [WIDTH/3, WIDTH/3+WIDTH/3], [WIDTH/3+WIDTH/3, WIDTH]]


affiche_debut_game(emplacement_zone)
pygame.display.update()

def main_chifoumi():

    fin = "continue"
    affiche_debut_game(emplacement_zone)
    pygame.display.update()
    time.sleep(1)
    run = True
    while run:

        
        

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = "quitte"
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                for i in range (len(emplacement_zone)):
                    if emplacement_zone[i][0] <= mouse[0] <= emplacement_zone[i][1]:
                        print(f"clique dans la zone n°{i+1}, donc vous avez choisi {symbole[i]}")

                        resul_bot = choix_bot(symbole)
                        fin = affiche_resultat(symbole[i], resul_bot)
                        if fin != "continue":
                            run = False

    if fin != "quitte":
        affiche_fin_partie(fin)

main_chifoumi()