import pygame
import random
import time



def init_carte():
    carte = [t+1 for _ in range (4) for t in range (10)]
    for _ in range (12): # add les 12 cartes valeur 10
        carte.append(10)
    carte.sort()
    return carte
 
    
def compte_point(personne):
    
    point = 0
    for i in range (len(personne)):
        
        if i == 0 and personne[i] == 1:
            point+=11
                
          
                
        else:
            point+=personne[i]
            
    return point
    
    
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
    if compte_point(carte_ordi) < 16:
        choix = random.choice(carte)
        carte_ordi.append(choix)
        carte.pop(carte.index(choix))        
        return True, carte_ordi
    
    else:
        return False, carte_ordi



def test_si_defaite(utilisateur_a_test):
    return compte_point(utilisateur_a_test) < 22  # True game pas fini;  False game fini
        

def affiche_solution_bot(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite):
    SCREEN.fill((0, 0, 0))
    for i in range (len(carte_utilisateur)):
        score_carte = pygame.font.SysFont("bahnschrift", 60).render(str(carte_utilisateur[i]), True, "black")
        pygame.draw.rect(SCREEN, WHITE, (75+70*i, 125+8*i, 175, 225))
        pygame.draw.rect(SCREEN, BLUE, (75+70*i, 125+8*i, 175, 225), 8)
        SCREEN.blit(score_carte, (85+70*i, 135+8*i))
        
 
    for i in range (len(carte_ordi)):
        
        score_carte = pygame.font.SysFont("bahnschrift", 60).render(str(carte_ordi[i]), True, "black")
        pygame.draw.rect(SCREEN, WHITE, (75+70*i, 400+8*i, 175, 225))
        pygame.draw.rect(SCREEN, RED, (75+70*i, 400+8*i, 175, 225), 8)    
        SCREEN.blit(score_carte, (85+70*i, 410+8*i))  
    
    #affiche la somme des scores:
    
    
    
    score_utilisateur = pygame.font.SysFont("bahnschrift", 40).render(f"Score {compte_point(carte_utilisateur)}", True, "white")
    score_bot = pygame.font.SysFont("bahnschrift", 40).render(f"Score {compte_point(carte_ordi)}", True, "white")
    
    SCREEN.blit(score_utilisateur, (WIDTH-300, 110))
    SCREEN.blit(score_bot, (WIDTH-300, 385))
    
    affiche_bouton(SCREEN)
    affiche_score(SCREEN, win, loose, egalite)
    pygame.display.update()
    


def affiche_carte(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite):
    SCREEN.fill((0, 0, 0))
    for i in range (len(carte_utilisateur)):
        score_carte = pygame.font.SysFont("bahnschrift", 60).render(str(carte_utilisateur[i]), True, "black")
        pygame.draw.rect(SCREEN, WHITE, (75+70*i, 125+8*i, 175, 225))
        pygame.draw.rect(SCREEN, BLUE, (75+70*i, 125+8*i, 175, 225), 8)
        SCREEN.blit(score_carte, (85+70*i, 135+8*i))
        
 
    for i in range (len(carte_ordi)):
        
        if i == 0:
            score_carte = pygame.font.SysFont("bahnschrift", 60).render("?", True, "black")
        else:
            score_carte = pygame.font.SysFont("bahnschrift", 60).render(str(carte_ordi[i]), True, "black")
        pygame.draw.rect(SCREEN, WHITE, (75+70*i, 400+8*i, 175, 225))
        pygame.draw.rect(SCREEN, RED, (75+70*i, 400+8*i, 175, 225), 8)    
        SCREEN.blit(score_carte, (85+70*i, 410+8*i))
    
    #affiche la somme des scores:
    
    
    
    score_utilisateur = pygame.font.SysFont("bahnschrift", 40).render(f"Score {compte_point(carte_utilisateur)}", True, "white")
    score_bot = pygame.font.SysFont("bahnschrift", 40).render(f"Score {compte_point(carte_ordi)-carte_ordi[0]} + ?", True, "white")
    
    SCREEN.blit(score_utilisateur, (WIDTH-300, 110))
    SCREEN.blit(score_bot, (WIDTH-300, 385))
    
    affiche_bouton(SCREEN)
    affiche_score(SCREEN, win, loose, egalite)
    pygame.display.update()
    

def affiche_bouton(SCREEN):
    
    pygame.draw.rect(SCREEN, WHITE, (0, 680, WIDTH/2, 100))    
    pygame.draw.rect(SCREEN, GREEN, (0, 680, WIDTH/2, 100), 2)
    
    pygame.draw.rect(SCREEN, WHITE, (WIDTH/2, 680, WIDTH/2, 100))
    pygame.draw.rect(SCREEN, GREEN, (WIDTH/2, 680, WIDTH/2, 100), 2)
    
    tire = pygame.font.SysFont("bahnschrift", 40).render("tire", True, "black")
    affiche_tire = tire.get_rect(center=(WIDTH/4, 730))
    
    passe = pygame.font.SysFont("bahnschrift", 40).render("passe", True, "black")
    affiche_passe = passe.get_rect(center=((WIDTH/2)+(WIDTH/4), 730))
    
    SCREEN.blit(tire, affiche_tire)
    SCREEN.blit(passe, affiche_passe)


    
    
    
def affiche_score(SCREEN, win, loose, egalite):
    affiche_win = pygame.font.SysFont("bahnschrift", 30).render(f"GAGNE : {win}", True, "white")
    affiche_loose = pygame.font.SysFont("bahnschrift", 30).render(f"PERDU : {loose}", True, "white")
    affiche_egalite = pygame.font.SysFont("bahnschrift", 30).render(f"EGALITE : {egalite}", True, "white")
    
    SCREEN.blit(affiche_win, (50, 850))
    SCREEN.blit(affiche_loose, (250, 850))
    SCREEN.blit(affiche_egalite, (450, 850))
    
    
def wait_clique(SCREEN):
    pygame.draw.rect(SCREEN, WHITE, ((WIDTH/2)-200, (HEIGHT/4)-50, 400, 100))
    pygame.draw.rect(SCREEN, GREEN, ((WIDTH/2)-200, (HEIGHT/4)-50, 400, 100), 4)
    wait_clique = pygame.font.SysFont("bahnschrift", 40).render("start game", True, "black")
    affiche_wait_clique = wait_clique.get_rect(center=(WIDTH/2, HEIGHT/4))
    SCREEN.blit(wait_clique, affiche_wait_clique)

    pygame.display.update()
    
    run = True
    while run:
        
        mouse = pygame.mouse.get_pos()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (WIDTH/2)-200 <= mouse[0] <= (WIDTH/2)+200 and (HEIGHT/4)-50 <= mouse[1] <= (HEIGHT/4)+50:
                    return True
    
    
    
    
    
    
    
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)      
WIDTH, HEIGHT = 700, 900




def main_blackjack():
    
    
    
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()

    pygame.display.set_caption("Blackjack") #titre de la page, fin  pas sur 

  
    
    
    
    carte = init_carte()

    carte_utilisateur = []
    carte_ordi = []
    carte_utilisateur, carte_ordi = distrubution_des_cartes(carte, carte_utilisateur, carte_ordi)
    win = 0
    loose = 0
    egalite = 0
    game = True
    run = True
    game = wait_clique(SCREEN)
    while game:
        affiche_carte(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite)
        
        mouse = pygame.mouse.get_pos()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= WIDTH/2 and 680 <= mouse[1] <= 780:
                    
                    carte_utilisateur = utilisateur_joue(carte_utilisateur, carte)
                    run = test_si_defaite(carte_utilisateur)
                    if run:
                        carte_ordi = ordinateur_joue(carte_ordi, carte)[1]
                        run = test_si_defaite(carte_ordi)
                    
                    affiche_carte(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite)
                    
           
                        
                    time.sleep(0.5)    
                    
                elif WIDTH/2 <= mouse[0] <= WIDTH and 680 <= mouse[1] <= 780:
                    
                    continuee = ordinateur_joue(carte_ordi, carte)[0]
                    run = test_si_defaite(carte_ordi)
                    print(continuee, run)
                    while continuee and run:
                        continuee = ordinateur_joue(carte_ordi, carte)[0]
                        affiche_carte(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite)
                        run = test_si_defaite(carte_ordi)
                  
                        
                    
                    run = False
        
        
        
        if run == False: # fin de la game:
            SCREEN.fill((0, 0, 0))
            affiche_solution_bot(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite)
            time.sleep(0.5)
            
            if compte_point(carte_utilisateur) > 21 or compte_point(carte_ordi) > 21:
                if compte_point(carte_utilisateur) > 21:
                    loose+=1
                else:
                    win+=1
                
            
            elif not test_si_defaite(carte_utilisateur) or compte_point(carte_utilisateur) < compte_point(carte_ordi):
                
                loose+=1
                False
            elif not test_si_defaite(carte_ordi) or compte_point(carte_utilisateur) > compte_point(carte_ordi):
                win+=1
                
            else:
                egalite+=1
            
            game = wait_clique(SCREEN)
            
            # la manche est fini je re initialise tout les parametres:
            SCREEN.fill((0, 0, 0))
            
            carte = [t+1 for _ in range (4) for t in range (10)]
            carte.sort()

            carte_utilisateur = []
            carte_ordi = []
            run = True
            
            carte_utilisateur, carte_ordi = distrubution_des_cartes(carte, carte_utilisateur, carte_ordi)
            affiche_carte(SCREEN, carte_utilisateur, carte_ordi, win, loose, egalite)
            
