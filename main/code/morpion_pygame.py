from pygame import * 
import pygame
import random


# NOM : Verbrugge
# PRENOM : Louis 
# CLASSE : T09



# _____ initialisation des fonctions pour le morpion _____ #

def initialise():
    '''
    cette fonction initialise les paramètre pour jouer'''
    plateau = ['.','.','.','.','.','.','.','.','.']
    joueur = random.randint(0,1)
    symboles = ('X','O')
    humain = 0
    ordinateur = 1
        
    return plateau, joueur, symboles, humain, ordinateur



def ordinateur_atac(plateau,symboles):
    
    case = random.randint(0, 8)
    
    if plateau[0] == plateau[1] and plateau[0] in symboles and plateau[2] not in symboles:
        case=2
        return case
        
    if plateau[1] == plateau[2] and plateau[1] in symboles and plateau[0] not in symboles:
        case=0
        return case
        
    if plateau[0] == plateau[2] and plateau[0] in symboles and plateau[1] not in symboles:
        case=1
        return case
        
        
#___________________________________________________________        
        
        
    if plateau[3] == plateau[4] and plateau[3] in symboles and plateau[5] not in symboles:
        case=5
        return case
        
    if plateau[4] == plateau[5] and plateau[4] in symboles and plateau[3] not in symboles:
        case=3
        return case
        
    if plateau[3] == plateau[5] and plateau[3] in symboles and plateau[4] not in symboles:
        case=4
        return case
        
    
#___________________________________________________________  
         
        
    if plateau[6] == plateau[7] and plateau[6] in symboles and plateau[8] not in symboles:
        case=8
        print('11111')
        return case
    if plateau[7] == plateau[8] and plateau[7] in symboles and plateau[6] not in symboles:
        case=6
        return case 
    if plateau[6] == plateau[8] and plateau[6] in symboles and plateau[7] not in symboles:
        case=7   
        return case  
        
#___________________________________________________________              
        
        
    if plateau[0] == plateau[3] and plateau[0] in symboles and plateau[6] not in symboles:
        case=6
        return case
    if plateau[3] == plateau[6] and plateau[3] in symboles and plateau[0] not in symboles:
        case=0
        return case
    if plateau[0] == plateau[6] and plateau[0] in symboles and plateau[3] not in symboles:
        case=3
        return case
        
#___________________________________________________________              
        
        
    if plateau[1] == plateau[4] and plateau[1] in symboles and plateau[7] not in symboles:
        case=7
        return case
        
    if plateau[4] == plateau[7] and plateau[4] in symboles and plateau[1] not in symboles:
        case=1
        return case
        
    if plateau[1] == plateau[7] and plateau[1] in symboles and plateau[4] not in symboles:
        case=4
        return case
        
       
#___________________________________________________________             
        
    if plateau[2] == plateau[5] and plateau[2] in symboles and plateau[8] not in symboles:
        case=8
        print('222222222222')
        return case
        
    if plateau[5] == plateau[8] and plateau[5] in symboles and plateau[2] not in symboles:
        case=2
        return case
        
    if plateau[2] == plateau[8] and plateau[2] in symboles and plateau[5] not in symboles:
        case=5
        return case
        
        
#___________________________________________________________              
        
    if plateau[0] == plateau[4] and plateau[0] in symboles and plateau[8] not in symboles:
        case=8
        print('333333333333333')
        return case
        
    if plateau[4] == plateau[8] and plateau[4] in symboles and plateau[0] not in symboles:
        case=0
        return case
        
    if plateau[0] == plateau[8] and plateau[0] in symboles and plateau[4] not in symboles:
        case=4
        return case
        
        
#___________________________________________________________              
        
    print("GGGGGGGGGG HH")
    print(plateau[2], plateau[4], plateau[6])
    
    if plateau[2] == plateau[4] and plateau[2] in symboles and plateau[6] not in symboles:
        case = 6
        print('WOW mais quoi ?!')
        return case
        
    if plateau[4] == plateau[6] and plateau[4] in symboles and plateau[2] not in symboles:
        case=2
        return case
        
    if plateau[2] == plateau[6] and plateau[2] in symboles and plateau[4] not in symboles:
        case=4
        return case

    
    else:
        #case=ordinateur_def(plateau, symboles)
        while plateau[case] in symboles:
            case = random.randint(0,8)  
        return case
        


def verifier_victoire(plateau, symboles):
    '''
    cette fonction verifie si il n'y a pas de gagnant
    '''
    accu = 0
    for i in range (len(plateau)):
        if plateau[i] != '.':
            accu += 1
    
    print(len(plateau), accu)
    if len(plateau) == accu or (plateau[0] == plateau[1] == plateau[2] and plateau[0] in symboles or 
    plateau[3] == plateau[4] == plateau[5] and plateau[3] in symboles or
    plateau[6] == plateau[7] == plateau[8] and plateau[6] in symboles or
    plateau[0] == plateau[3] == plateau[6] and plateau[0] in symboles or
    plateau[1] == plateau[4] == plateau[7] and plateau[1] in symboles or
    plateau[2] == plateau[5] == plateau[8] and plateau[2] in symboles or
    plateau[2] == plateau[4] == plateau[6] and plateau[2] in symboles or
    plateau[0] == plateau[4] == plateau[8] and plateau[0] in symboles ):
        return True
    else:
        return False
   


def affiche_symbole_utilisateur(numero_case):
    x = emplacement_case[numero_case][0]+33.5
    y = emplacement_case[numero_case][2]+33.5
    x_prime = x+100
    y_prime = y+100
    return x, y, x_prime, y_prime
    
   
    
def affichage_symbole_ordinateur(numero_case):
    x_milieu = (emplacement_case[numero_case][1] - emplacement_case[numero_case][0])/2
    y_milieu = (emplacement_case[numero_case][3] - emplacement_case[numero_case][2])/2
    return emplacement_case[numero_case][0] +x_milieu, emplacement_case[numero_case][2] + y_milieu





def affiche_meilleur_joueur(nb_victoire):
    
    
    if nb_victoire[0] < nb_victoire[1]:
        return "le bot a gagné : "
        
    elif nb_victoire[0] > nb_victoire[1]:
        return "tu as gagné :"
        
    else:
        return "vous êtes à égalité"
    
        
    
    
    
    



def affiche_fin_de_partie(SCREEN, plateau, symboles, nb_victoire):
    print(f"TTTTTTTTTTTTTTTT :{plateau}")
    fin_de_partie=""
    for i in range (2):
        if (plateau[0] == plateau[1] == plateau[2] and plateau[0] in symboles[i] or 
        plateau[3] == plateau[4] == plateau[5] and plateau[3] in symboles[i] or
        plateau[6] == plateau[7] == plateau[8] and plateau[6] in symboles[i] or
        plateau[0] == plateau[3] == plateau[6] and plateau[0] in symboles[i] or
        plateau[1] == plateau[4] == plateau[7] and plateau[1] in symboles[i] or
        plateau[2] == plateau[5] == plateau[8] and plateau[2] in symboles[i] or
        plateau[2] == plateau[4] == plateau[6] and plateau[2] in symboles[i] or
        plateau[0] == plateau[4] == plateau[8] and plateau[0] in symboles[i] ):
            
            if i == 0: # la croix a gagné ! ( donc dans ce cas l'utilisateur )
                fin_de_partie = "VICTOIRE"
                
                combien_de_victoire = nb_victoire.pop(0)
                nb_victoire.insert(0, combien_de_victoire+1)  
                qui_gagne_ = "tu as gagné :"
                
                
            elif i == 1:
                fin_de_partie = "défaite.."
                
                
                combien_de_victoire = nb_victoire.pop(1)
                nb_victoire.append(combien_de_victoire+1) 
                qui_gagne_ = "le bot a gagné :  "

    if fin_de_partie == "":
        fin_de_partie = "égalite"
        qui_gagne_ = "vous êtes à égalité"

    run_affiche = True
    while run_affiche:
        

        if fin_de_partie == "VICTOIRE":
            fond = pygame.image.load('./image/victoire_carss.jpg')    
              
        else:
            fond = pygame.image.load('./image/lapin_pendu_defaite.jpg')
       
       
           
        test_affiche_win = pygame.font.SysFont("bahnschrift", 100).render(fin_de_partie, True, "black")  # affiche le gagnant !
        win = test_affiche_win.get_rect(center=(WIDTH/4, HEIGHT/3))  # c'est la position ou j 'affiche le gagnant
        
                        
        recommencer_une_partie = pygame.font.SysFont("bahnschrift", 30).render("cliquer pour RECOMMENCER !", True, "black") # affiche si le joueur veut refaire une partie !
        restart = recommencer_une_partie.get_rect(center=(WIDTH-200, HEIGHT-100))  # affiche la position du boutton !
                
                

                
                
        score_ordinateur = pygame.font.SysFont("bahnschrift", 50).render(f"{qui_gagne_} {str(max(nb_victoire[0], nb_victoire[1]))} - {min((nb_victoire[0], nb_victoire[1]))}", True, "black")
        score_o = score_ordinateur.get_rect(center=(WIDTH-300, 100))
 
        
                    
                    
        fond = fond.convert()
        SCREEN.blit(fond, (0,0))
        SCREEN.blit(test_affiche_win, win)  
        SCREEN.blit(recommencer_une_partie, restart)
        SCREEN.blit(score_ordinateur, score_o)
        draw.rect(SCREEN, RED, (WIDTH-420, HEIGHT-120, 420, 40), 5) # TTT
        
        mouse = pygame.mouse.get_pos()
        display.update()
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_affiche = False
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH-420 <= mouse[0] <= WIDTH and HEIGHT-120 <= mouse[1] <= HEIGHT:
                    print('WOWWWWW')
                    print("FALITY !")
                    if fin_de_partie == "VICTOIRE":
                        main_morpion(nb_victoire)
                        
                    else:
                        main_morpion(nb_victoire)
        
                    run_affiche = False # c'a signifie que toute les boucles sont fini, donc je quitte le programme
        
    print('LE programme est fini !')

# _____ initialisation pygame _____ #



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 1300, 1000   ###WIDTH, HEIGHT = 800, 600
size = width, height = 1300, 1000 ### size = width, height = 800, 600







def initilisation_page_jeu(SCREEN):
    
    fond_acceil = pygame.image.load('./image/main.jpg')
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0))  
    draw.rect(SCREEN, BLACK, (150, 50, 501, 501), 5)  # carre de base

    draw.line(SCREEN, BLACK, (317, 50), (317, 550), 3)  # barre vertical ,n°1
    draw.line(SCREEN, BLACK, (484, 50), (484, 550), 3)  # barre vertical ,n°2


    draw.line(SCREEN, BLACK, (150, 217), (650, 217), 3)  # barre horizontal ,n°1
    draw.line(SCREEN, BLACK, (150, 384), (650, 384), 3)  # barre horizontal ,n°2
 
 
 
 

emplacement_case = [                   #(x, x' et y, y') de la case en haut a gauche vers la droite, puis vers le bas
    [150, 316, 50, 216], # haut gauche
    [317, 483, 50, 216], #haut milieu
    [484, 651, 50, 216], # haut droite
    [150, 316, 217, 383], # milieur gauche
    [317, 483, 217, 383], # milieu mileu
    [484, 651, 217, 383],  # milieu droite
    [150, 316, 384, 551], # bas gauche*
    [317, 483, 384, 551],  # bas milieu
    [484, 651, 384, 551]] # bas droite

    
nb_victoire = [0, 0]  # la valeur [0] est le nombre victoire utilisateur [1] victoire ordinateur
  
  
qui_gagne_= "vous etes egalite"


    




#plateau, joueur, symboles, humain, ordinateur = initialise() # pas sur de mon coup la


def main_morpion(nb_victoire):
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Tic Toc Toe")
    pygame.init()
    plateau, joueur, symboles, humain, ordinateur = initialise()
    initilisation_page_jeu(SCREEN)
    score_ordinateur = pygame.font.SysFont("bahnschrift", 50).render(f"{affiche_meilleur_joueur(nb_victoire)} {str(max(nb_victoire[0], nb_victoire[1]))} - {min((nb_victoire[0], nb_victoire[1]))}", True, "black")
    score_o = score_ordinateur.get_rect(center=(WIDTH-300, 100)) 
    SCREEN.blit(score_ordinateur, score_o)
    run = True
    while run: 
        
        
        
        
        
        
        
        

        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                for i in range (len(emplacement_case)):
                    
                    # ce test si la sourie a clique dans l'une des cases du plateau 
                    if emplacement_case[i][0] <= mouse[0] <= emplacement_case[i][1] and emplacement_case[i][2] <= mouse[1] <= emplacement_case[i][3]:  # c'est les coordeonne de la cas en haut a droite, crée une fonction qui test pour tout les case, avec l'aide d'une liste
                        if plateau[i] not in symboles:
                            
                            x, y, x_prime, y_prime = affiche_symbole_utilisateur(i)
                            
                            draw.line(SCREEN, RED, (x, y), (x_prime, y_prime), 4) # ligne diagonale n°1 pour la croix, il va falloir modif le ( x, y )
                            draw.line(SCREEN, RED, (x, y_prime), (x_prime, y), 4) # ligne diagonale n°1 pour la croix, il va falloir modif le ( x, y )        
                            
                            plateau[i] = symboles[humain] 
                            if verifier_victoire(plateau, symboles) == False:
                                
                                # le bot joue
                                print(plateau)
                                case = ordinateur_atac(plateau, symboles)
                                # affiche le roue, avec 'case' la case choisie par le bot
                                
                                x, y = affichage_symbole_ordinateur(case)
                                plateau[case] = symboles[ordinateur]
                                draw.circle(SCREEN, RED, (x, y), 50, 4) # cercle pour le joueur, il va falloir modif le ( x, y )
                                
                                
                            if verifier_victoire(plateau, symboles):
                                print(verifier_victoire(plateau, symboles))
                                run = False
                        
                            SCREEN.blit(score_ordinateur, score_o)    
                            display.update()
                        
        mouse = pygame.mouse.get_pos()
        display.update()
    
    
    # faire un test si le joueur a quitter ou si il y a un gagnant 
    print(verifier_victoire(plateau, symboles))
    if verifier_victoire(plateau, symboles):
        
        affiche_fin_de_partie(SCREEN, plateau, symboles, nb_victoire)
