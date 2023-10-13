import pygame
import sys
import random
import time

def distrubution_des_cartes(carte, carte_utilisateur, carte_ordi):
    
    for _ in range (4):
        if len(carte_utilisateur) < 2:
            choix = random.choice(carte)
            carte_utilisateur.append(choix)
            carte.pop(carte.index(choix))
            
        else:
            choix = random.choice(carte)
            carte_ordi.append(choix)
            carte.pop(carte.index(choix))
            
    return carte_utilisateur, carte_ordi
    
    
 
 
def utilisateur_joue(carte_utilisateur, carte): 
    choix = random.choice(carte)
    carte_utilisateur.append(choix)
    carte.pop(carte.index(choix)) 
    return carte_utilisateur
 
 
    
def ordinateur_joue(carte_ordi, carte):
    if sum(carte_ordi) < 16:
        choix = random.choice(carte)
        carte_ordi.append(choix)
        carte.pop(carte.index(choix))        
        return True, carte_ordi
    
    else:
        return False, carte_ordi



def test_si_defaite(utilisateur_a_test):
    return  sum(utilisateur_a_test) <= 22  # True game pas fini;  False game fini
        




def affiche_carte(carte_utilisateur, carte_ordi, win, loose, egalite):
    for i in range (len(carte_utilisateur)):
        score_carte = pygame.font.SysFont("bahnschrift", 60).render(str(carte_utilisateur[i]), True, "black")
        pygame.draw.rect(SCREEN, WHITE, (75+70*i, 50+8*i, 175, 225))
        pygame.draw.rect(SCREEN, BLUE, (75+70*i, 50+8*i, 175, 225), 8)
        SCREEN.blit(score_carte, (85+70*i, 60+8*i))
        
 
    for i in range (len(carte_ordi)):
        
        if i == 0:
            score_carte = pygame.font.SysFont("bahnschrift", 60).render("?", True, "black")
        else:
            score_carte = pygame.font.SysFont("bahnschrift", 60).render(str(carte_ordi[i]), True, "black")
        pygame.draw.rect(SCREEN, WHITE, (75+70*i, 325+8*i, 175, 225))
        pygame.draw.rect(SCREEN, RED, (75+70*i, 325+8*i, 175, 225), 8)    
        SCREEN.blit(score_carte, (85+70*i, 335+8*i))
    
    #affiche la somme des scores:
    score_utilisateur = pygame.font.SysFont("bahnschrift", 40).render(f"Score {sum(carte_utilisateur)}", True, "white")
    score_bot = pygame.font.SysFont("bahnschrift", 40).render(f"Score {sum(carte_ordi)-carte_ordi[0]} + ?", True, "white")
    
    SCREEN.blit(score_utilisateur, (WIDTH-300, 35))
    SCREEN.blit(score_bot, (WIDTH-300, 310))
    
    affiche_bouton()
    affiche_score(win, loose, egalite)
    pygame.display.update()
    SCREEN.fill((0, 0, 0))
    

def affiche_bouton():
    
    pygame.draw.rect(SCREEN, WHITE, (0, 605, WIDTH/2, 100))    
    pygame.draw.rect(SCREEN, GREEN, (0, 605, WIDTH/2, 100), 2)
    
    pygame.draw.rect(SCREEN, WHITE, (WIDTH/2, 605, WIDTH/2, 100))
    pygame.draw.rect(SCREEN, GREEN, (WIDTH/2, 605, WIDTH/2, 100), 2)


def affiche_score(win, loose, egalite):
    affiche_win = pygame.font.SysFont("bahnschrift", 30).render(f"GAGNE : {win}", True, "white")
    affiche_loose = pygame.font.SysFont("bahnschrift", 30).render(f"PERDU : {loose}", True, "white")
    affiche_egalite = pygame.font.SysFont("bahnschrift", 30).render(f"EGALITE : {egalite}", True, "white")
    
    SCREEN.blit(affiche_win, (50, 775))
    SCREEN.blit(affiche_loose, (250, 775))
    SCREEN.blit(affiche_egalite, (450, 775))
    
    
carte = [t+1 for _ in range (4) for t in range (10)]
carte.sort()

carte_utilisateur = []
carte_ordi = []



WIDTH, HEIGHT = 700, 850
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

pygame.display.set_caption("Blackjack") #titre de la page, fin  pas sur 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)


carte_utilisateur, carte_ordi = distrubution_des_cartes(carte, carte_utilisateur, carte_ordi)
win = 0
loose = 0
egalite = 0
game = True
run = True
while game:
    affiche_carte(carte_utilisateur, carte_ordi, win, loose, egalite)
    
    mouse = pygame.mouse.get_pos()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= WIDTH/2 and 605 <= mouse[1] <= 705:
                
                carte_utilisateur = utilisateur_joue(carte_utilisateur, carte)
                run = test_si_defaite(carte_utilisateur)
                if run:
                    carte_ordi = ordinateur_joue(carte_ordi, carte)[1]
                    run = test_si_defaite(carte_ordi)
                    
                affiche_carte(carte_utilisateur, carte_ordi, win, loose, egalite)
                time.sleep(0.5)    
                
            elif WIDTH/2 <= mouse[0] <= WIDTH and 605 <= mouse[1] <= 705:
                
                continuee = ordinateur_joue(carte_ordi, carte)[0]
                run = test_si_defaite(carte_ordi)
                print(continuee, run)
                while continuee and run:
                    continuee = ordinateur_joue(carte_ordi, carte)[0]
                    affiche_carte(carte_utilisateur, carte_ordi, win, loose, egalite)
                    run = test_si_defaite(carte_ordi)
            
                    
                    
                  
                run = False
      
    if run == False:
        time.sleep(0.5)
        
        
        if not test_si_defaite(carte_utilisateur) or sum(carte_utilisateur) < sum(carte_ordi):
            
            loose+=1
            
        elif not test_si_defaite(carte_ordi) or sum(carte_utilisateur) > sum(carte_ordi):
            win+=1
            
        else:
            egalite+=1
          
          
          
        # la manche est fini je re initialise tout les parametres:  
        SCREEN.fill((0, 0, 0)) 
          
        carte = [t+1 for _ in range (4) for t in range (10)]
        carte.sort()

        carte_utilisateur = []
        carte_ordi = []      
        game = True
        run = True
        
        carte_utilisateur, carte_ordi = distrubution_des_cartes(carte, carte_utilisateur, carte_ordi)
        affiche_carte(carte_utilisateur, carte_ordi, win, loose, egalite)