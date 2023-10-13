from pygame import *
import pygame
import random
import time


def verifie_doublon(zone_pour_bombe):
    for elem in zone_pour_bombe:
        nombre_doublon = 0
        for i in range (len(zone_pour_bombe)):
            if elem == zone_pour_bombe[i]:
                nombre_doublon+=1
    
                
                if nombre_doublon >= 2:
                    return True, elem # le test est faux donc je recommence
    
    return False,  zone_pour_bombe# le test est vrai



def choisir_les_zones(tour):  # [0] = hauteur_1  [1] = largeur_1;    [2] = hauteur_2 etcc....
    
    zone_pour_bombe = []
        
    for _ in range (tour): 
        valeur_x = random.randint(0, 2)
        valeur_y = random.randint(0, 2)
        zone_pour_bombe.append([valeur_x, valeur_y])
        
    cherche_pas_de_doublon = True
    while cherche_pas_de_doublon:
        # je cherche un doublon : 
        vrai_ou_faux, valeur_doublon = verifie_doublon(zone_pour_bombe)
        
        if vrai_ou_faux == False:
            cherche_pas_de_doublon = False
        
        else:
            valeur_x = random.randint(0, 2)
            valeur_y = random.randint(0, 2)
            
            # je cherche la possition du doublon : 
            coordone_soublon = zone_pour_bombe.index(valeur_doublon)
            # je replace le doublon par une autre valeur :
            zone_pour_bombe.pop(coordone_soublon)
            zone_pour_bombe.insert(coordone_soublon, [valeur_x, valeur_y])
            
    return zone_pour_bombe
       
     
    
    
def mise_en_place_bombe_sur_la_maps(maps, niveau):  # voici la zone impossible, maintenant je dois test que la zone ne peut pas avoir de bombe.
    """_summary_

    Args:
        zone_pour_bombe (liste de liste): contient les coordonnes de toute les zones
        maps (liste): maps du jeu 
        nb_bombe_par_zone (integer): nombre de bombe par zone
    """
    zone_pour_bombe = choisir_les_zones(niveau[3])
    nb_bombe_par_zone = niveau[2] // niveau[3]
    
    for elem in zone_pour_bombe:
        emplacement_bombe_sur_la_maps = []
        zone_largeur = elem[0]*len(maps[0])//3
        zone_hauteur = elem[1]*len(maps)//3
        
        for _ in range (nb_bombe_par_zone):
            possition_largeur_bombe = random.randint(zone_largeur, zone_largeur+len(maps[0])//3-1)
            possition_hauteur_bombe = random.randint(zone_hauteur, zone_hauteur+len(maps)//3-1)
            emplacement_bombe_sur_la_maps.append([possition_largeur_bombe, possition_hauteur_bombe])
            
            verif = True
            while verif:
                
                vrai_ou_faux, valeur_doublon = verifie_doublon(emplacement_bombe_sur_la_maps)
                
                if vrai_ou_faux == False:
                    verif = False
                    
                else:
                    possition_largeur_bombe = random.randint(zone_largeur, zone_largeur+len(maps[0])//3-1)
                    possition_hauteur_bombe = random.randint(zone_hauteur, zone_hauteur+len(maps)//3-1)   
                    
                    # je cherche la possition du doublon : 
                    coordone_soublon = emplacement_bombe_sur_la_maps.index(valeur_doublon)
                    # je replace le doublon par une autre valeur :
                    emplacement_bombe_sur_la_maps.pop(coordone_soublon)
                    emplacement_bombe_sur_la_maps.insert(coordone_soublon, [possition_largeur_bombe, possition_hauteur_bombe]) 
                   
                   
        for i in range (len(emplacement_bombe_sur_la_maps)):
            maps[emplacement_bombe_sur_la_maps[i][1]].pop(emplacement_bombe_sur_la_maps[i][0])
            maps[emplacement_bombe_sur_la_maps[i][1]].insert(emplacement_bombe_sur_la_maps[i][0], "B")
    

 
    
def est_dans_la_grille(maps, coordonne_y, coordonne_x):
      
    if 0 <= coordonne_y <= len(maps)-1 and 0 <= coordonne_x <= len(maps[0])-1:
        if maps[coordonne_y][coordonne_x] == "B":  #~si les deux coordonne sont dans la grille la fonction renvoie True, sinon False
            return False
        return True
    return False
    
    
    
    

def chiffre_a_cote_bombe(maps):
    
    for coordonne_y in range (len(maps)):
        for coordonne_x in range (len(maps[coordonne_y])):
            if maps[coordonne_y][coordonne_x] == "B":
                # dans ce cas je dois modifier les valeurs autour de ce chiffre pour les ajouter; mais je dois tester si elles ne sont pas hors maps ou que c'est des bombes
                
                for hauteur in range (3):
                    for largeur in range (3):
                        #  if hauteur != 1 and largeur != 1:  # ca signifie que on multiplie une bombe par + 1, mais je dois rajoute un test
                        
                        if est_dans_la_grille(maps, coordonne_y-1+hauteur, coordonne_x-1+largeur):
                            maps[coordonne_y-1+hauteur][coordonne_x-1+largeur] += 1
                            
                            
                            

def emplacement_case(maps): # (x x' y y')
    emplacement_casee = []
    for ligne in range (len(maps)):
        emplacement_casee.append([])
        for col in range (len(maps[0])):
            emplacement_casee[ligne].append([300+((WIDTH-600)/len(maps[0]))*col, 300+((WIDTH-600)/len(maps[0]))*col + ((WIDTH-600)/len(maps[0])), 150+((HEIGHT-300)/len((maps)))*ligne, 150+((HEIGHT-300)/len((maps)))*ligne + ((HEIGHT-300)/len((maps)))])
            
    return emplacement_casee


            
            
            
            
            
        
def affiche_maps_debut_game(SCREEN, maps, emplacement_decouvert, nb_bombe, emplacement_drapeau):
    
    

    # AFFICHE LE FOND EN NOIR :
    pygame.draw.rect(SCREEN, BLACK, (344, 49, 70, 56))   

    
    # j'affiche la ligne verticale :
    pygame.draw.line(SCREEN, RED, (300, 50), (300, 100), 4)   # la ligne vertical
    

    # premier point : (300, 50 + rep_y)              - "en haut a gauche"
    # deuxième point : (300, 50 + rep_y2)            - "en bas a gauche"
    # troisième point : (300+rep_y, 50 + rep_y/3)    - "a droite"

    # j'affiche le triangle pour faire le drapeau :
    pygame.draw.polygon(SCREEN, RED, [
                        [300, 50], # (x, y) du point du triangle
                        [300, 75], # (x, y) du point du triangle
                        [343, 62.5]])# (x, y) du point du triangle
    
    
    
    numbre_drapeau_reste = pygame.font.SysFont("bahnschrift", 50).render(str(nb_bombe-len(emplacement_drapeau)), True, WHITE)  # affiche le gagnant !
    affiche_numbre_drapeau_reste = numbre_drapeau_reste.get_rect(center=(385, 75))  # c'est la position ou j 'affiche le gagnant
    SCREEN.blit(numbre_drapeau_reste, affiche_numbre_drapeau_reste)    
    
    
    for ligne in range (len(maps)):
        accu = 0
        for col in range (len(maps[0])):
            
            if accu % 2 == 0 or maps[ligne][col] == 0:
                if maps[ligne][col] != "B":  # je cherche si les autres valeur sont a cote d'un 0, si oui j affiche cette case
                    affiche_choix_chiffre(SCREEN, maps, col, ligne)
                    emplacement_decouvert.append([col, ligne])
            accu+=1
            display.update()
    
    return emplacement_decouvert
        
        
        
        
def affiche_drapeau(SCREEN, possition_case, coordonne_case_x, coordonne_case_y, maps, emplacement_drapeau, nb_bombe):
    
    # création du drapeau
    
    # je cherche le premier point x :
    
    # je sais que toute les cases font la meme taille, donc j vais prendre la premier pour cherche leur taille:
    taille_x = possition_case[0][0][1] - possition_case[0][0][0]
    taille_y = possition_case[0][0][3] - possition_case[0][0][2]
    
    rep_x = (2/3)*taille_x
    point_x_depart = (taille_x-rep_x)/2 # point base ligne drapeau - x
    
    rep_y = (2/3)*taille_y
    point_y_depart = (taille_y-rep_y)/2 # point base ligne drapeau - y
    
    # AFFICHE LE FOND EN NOIR : 
    pygame.draw.rect(SCREEN, BLACK, (344, 49, 70, 56))  
    
    
    # j'affiche la ligne verticale :
    pygame.draw.line(SCREEN, RED, (300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart, 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart), (300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart, 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart + rep_y), 4)   # la ligne vertical



    # j'affiche le triangle pour faire le drapeau :
    pygame.draw.polygon(SCREEN, RED, [
                        [300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart , 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart], # (x, y) du point du triangle
                        [300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart , 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart + (rep_y)/2], # (x, y) du point du triangle
                        [300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart + taille_x/2, 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart + (rep_y/4)]])# (x, y) du point du triangle
        
        
        
        
        
    # AFFICHE LE NOMBRE DE DRAPEAU QUI RESTE A POSER :

    taille_y = possition_case[0][0][3] - possition_case[0][0][2]
    
    
    rep_y = (2/3)*taille_y        
        
    numbre_drapeau_reste = pygame.font.SysFont("bahnschrift", 50).render(str(nb_bombe - len(emplacement_drapeau)), True, WHITE)  # affiche le gagnant !
    affiche_numbre_drapeau_reste = numbre_drapeau_reste.get_rect(center=(385, 75))  # c'est la position ou j 'affiche le gagnant
    SCREEN.blit(numbre_drapeau_reste, affiche_numbre_drapeau_reste)        
    display.update()
        
        
        
        
def affiche_supprimer_drapeau(SCREEN, maps, coordonne_x, coordonne_y, emplacement_drapeau, nb_bombe):
    
    if coordonne_y%2 == 0:
        if coordonne_x%2 == 0: 
            pygame.draw.rect(SCREEN, GREEN_CLAIR, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
        else:
            pygame.draw.rect(SCREEN, GREEN_FONCE, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))

            
    else:
        if coordonne_x%2 == 0: 
            pygame.draw.rect(SCREEN, GREEN_FONCE, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
        else:
            pygame.draw.rect(SCREEN, GREEN_CLAIR, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
        
   
    # AFFICHE LE FOND EN NOIR :
    pygame.draw.rect(SCREEN, BLACK, (344, 49, 70, 56))   
   
        
    numbre_drapeau_reste = pygame.font.SysFont("bahnschrift", 50).render(str(nb_bombe-len(emplacement_drapeau)), True, WHITE)  # affiche le gagnant !
    affiche_numbre_drapeau_reste = numbre_drapeau_reste.get_rect(center=(385, 75))  # c'est la position ou j 'affiche le gagnant
    SCREEN.blit(numbre_drapeau_reste, affiche_numbre_drapeau_reste)  
    
    display.update()
        
        
        
        
        
        
        
        
def affiche_toute_les_cases(SCREEN, maps, emplacement_decouvert, resultat):
    if resultat == "DEFAITE":
        
        for ligne in range (len(maps)):
            for col in range (len(maps[0])):
                if [col, ligne] not in emplacement_decouvert:
                    affiche_choix_chiffre(SCREEN, maps, col, ligne)
        couleur = RED
        
    else:
        couleur = GREEN
                
    affche_world_clique = pygame.font.SysFont("bahnschrift", 100).render("CLIQUE pour continuer", True, "red")
    world_clique = affche_world_clique.get_rect(center=(WIDTH/2, HEIGHT-100))    
    
    
    resultat = pygame.font.SysFont("bahnschrift", 100).render(resultat, True, couleur)
    affiche_resultat = resultat.get_rect(center=(WIDTH/1.5, 100))    
    
    SCREEN.blit(affche_world_clique, world_clique)
    SCREEN.blit(resultat, affiche_resultat)
      
    display.update()  
    
    fin = ""
    run_defaite = True
    while run_defaite:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return "quitte"

            if event.type == pygame.MOUSEBUTTONDOWN: # test si il y a un clique
                return ""

          
def creation_maps(collun, ligne, valeur):
    maps = []
    for _ in range (ligne):
        maps.append([x-x+valeur for x in range (collun)])
    return maps




def affichage_maps_init(SCREEN, maps):
    accu = 0
    
    for ligne in range (len(maps)):
        for col in range (len(maps[0])):
            
            
            if accu % 2 == 0:
                pygame.draw.rect(SCREEN, GREEN_CLAIR, (300+((WIDTH-600)/len(maps[0]))*col, 150+((HEIGHT-300)/len(maps))*ligne, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps))))) 
                
            else:
                pygame.draw.rect(SCREEN, GREEN_FONCE, (300+((WIDTH-600)/len(maps[0]))*col, 150+((HEIGHT-300)/len(maps))*ligne, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
            
                        
            accu+=1
    
    
    
    
    
    
def initilisation_cherche_maps_adapte(SCREEN, maps):
      # je dois crée une fonction qui contient les coordonnes des 9 zones, 
    # ensuite je recherche le clique pour revoier la zone qui ne peut pas contenir de bombe
    
    affichage_maps_init(SCREEN, maps)
    display.update()
    
    fin = ""
    run_init = True
    while run_init:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = "quitte"
                run_init = False
                
            
            if event.type == MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= WIDTH-300 and 150 <= mouse[1] <= HEIGHT-150:
                    run_init = False
              
    return fin     
    
    
    
def affiche_choix_chiffre(SCREEN, maps, coordonne_x, coordonne_y):
    chiffre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    if maps[coordonne_y][coordonne_x] in chiffre:#l'utilisateur a clique sur un chiffre !
        pygame.draw.rect(SCREEN, SABLE, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
            
            
        nombre_trouve = pygame.font.SysFont("bahnschrift", 30).render(str(maps[coordonne_y][coordonne_x]), True, "white")
        affiche_nombre_trouve = nombre_trouve.get_rect(center=((300+((WIDTH-600)/len(maps[0]))*coordonne_x)+ ((WIDTH-600)/len(maps[0]))/2, (150+((HEIGHT-300)/len(maps))*coordonne_y)+((HEIGHT-300)/len(maps))/2))
        SCREEN.blit(nombre_trouve, affiche_nombre_trouve)
        
            
    else: #l'utilisateur a cliqué sur une bombe..
        pygame.draw.rect(SCREEN, RED, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps))))) 
        
    

    
    
    
def choix_du_niveau(SCREEN):
    
    fond_acceil = pygame.image.load('./image/main.jpg')
    fond_acceil = fond_acceil.convert()
    
    
    
    
    
    choix_du_niveau = pygame.font.SysFont("bahnschrift", 50).render("Choisissez un niveau :", True, "white")
    affiche_niveau = choix_du_niveau.get_rect(center=(WIDTH/2, HEIGHT/3))

    facilee = pygame.font.SysFont("bahnschrift", 50).render("FACILE", True, "white")
    nieau_facilee = facilee.get_rect(center=(WIDTH/4, HEIGHT/1.5))

    moyenn = pygame.font.SysFont("bahnschrift", 50).render("MOYEN", True, "white")
    niveau_moyenn = moyenn.get_rect(center=(WIDTH/2, HEIGHT/1.5))

    hardd = pygame.font.SysFont("bahnschrift", 50).render("HARD", True, "white")
    niveau_hardd = hardd.get_rect(center=(WIDTH/1.4, HEIGHT/1.5))        
    
    
    # affiche les commentaires pour le choix du niveau
    facile = pygame.font.SysFont("bahnschrift", 30).render("plutôt facile", True, "white")
    nieau_facile = facile.get_rect(center=(WIDTH/4, HEIGHT/1.5+50))   
    
    moyen = pygame.font.SysFont("bahnschrift", 30).render("c'est complexe", True, "white")
    niveau_moyen = moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5+50))    
    
    hard = pygame.font.SysFont("bahnschrift", 30).render("c'est vraiment très complexe", True, "white")
    niveau_hard = hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5+50))    
    
    
    affiche_choix_niveau = True
    while affiche_choix_niveau:


        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                affiche_choix_niveau = False

            

        if (WIDTH/4)-80 <= mouse[0] <= (WIDTH/4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
                 
            SCREEN.blit(facile, nieau_facile)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [12, 9, 15, 3]

            
        # je test si l'utilisateur clique dans la case MOYEN !
        elif (WIDTH/2)-80 <= mouse[0] <= (WIDTH/2)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
            
            SCREEN.blit(moyen, niveau_moyen)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [18, 15, 40, 5]
                
        # je test si l'utilisateur clique dans la case HARD !
        elif (WIDTH/1.4)-80 <= mouse[0] <= (WIDTH/1.4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
            
            SCREEN.blit(hard, niveau_hard)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [24, 21, 96, 8]

       
        else:
            SCREEN.blit(fond_acceil, (0,0))
            SCREEN.blit(choix_du_niveau, affiche_niveau)

            SCREEN.blit(facilee, nieau_facilee)
            SCREEN.blit(moyenn, niveau_moyenn)
            SCREEN.blit(hardd, niveau_hardd)   
            
            
            pygame.draw.rect(SCREEN, WHITE, ((WIDTH/4)-85, (HEIGHT/1.5)-40, 175, 70), 2) #  facile 
            pygame.draw.rect(SCREEN, WHITE, ((WIDTH/2)-85, (HEIGHT/1.5)-40, 175, 70), 2) # moyen
            pygame.draw.rect(SCREEN, WHITE, ((WIDTH/1.4)-70, (HEIGHT/1.5)-40, 150, 70), 2) # hard  
    
        pygame.display.update()
     
    return "quitte"   
    
    
    
    
    
    
    

def affiche_fin_partie(SCREEN, resultat_fin_partie):
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
                run_affice_fin = False
                        
            if event.type == pygame.MOUSEBUTTONDOWN: #je test si il y a un clique sur le boutton pour recommence une partie 
                if WIDTH-420 <= mouse[0] <= WIDTH and HEIGHT-120 <= mouse[1] <= HEIGHT: 
                    main_demineur()
                    run_affice_fin = False
                    
    print('LE programme est fini !') 
    
    



BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SABLE = (218, 229, 179)

GREEN_CLAIR = (57, 255, 4)
GREEN_FONCE = (0, 113, 14)

WIDTH, HEIGHT = 1300, 1000   ### WIDTH, HEIGHT = 1000, 800













def main_demineur():
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Démineur") 
    
    
    emplacement_drapeau = []
    emplacement_decouvert = [] 
    resultat_fin_partie = ""
    
    niveau = choix_du_niveau(SCREEN)  # [0] = tuple qui contient les info du niveau;   [1] = nom du niveau ('facile', 'moyen', 'hard')
    if niveau == "quitte":
        fin_game = niveau
    
    else:    
        SCREEN.fill(BLACK)  # fond en noir
        maps = creation_maps(niveau[1], niveau[0], -1) # je crée la map vierge
        possition_case = emplacement_case(maps)   # cette fonction contient tout les coordonnes des cases
        maps = creation_maps(niveau[1], niveau[0], 0)  #je modifie la map vierge    
        mise_en_place_bombe_sur_la_maps(maps, niveau)  #je modifie la map pour y poser les bombes
        chiffre_a_cote_bombe(maps)   # je modifie la map pour mettre les chiffres a cote des bombes
        
        fin_game = initilisation_cherche_maps_adapte(SCREEN, maps)  # j'attend qu'il y est un clique avant d'afficher la maps
        emplacement_decouvert = affiche_maps_debut_game(SCREEN, maps, emplacement_decouvert, niveau[2], emplacement_drapeau) # affiche la map
        
        display.update() # mise a jour pour affiche tout les modifications.
        
        
        print(f"nombre de case decouvert : {len(emplacement_decouvert)},  nombre de bombe : {niveau[2]}")
        print(f"nombre de toute les case : {niveau[0]*niveau[1]}")

    if fin_game == "":
        run = True
    else:
        run = False
    
    
    while run:
        
        
        mouse = pygame.mouse.get_pos()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_game = "quitte"
                run = False
                
                
            if event.type == MOUSEBUTTONDOWN:
                for ligne in range (len(maps)):
                    for col in range (len(maps[0])):
                        if possition_case[ligne][col][0] <= mouse[0] <= possition_case[ligne][col][1] and possition_case[ligne][col][2] <= mouse[1] <= possition_case[ligne][col][3]:
                            if event.button == 1:  # 1 = LEFT 
                                if [col, ligne] not in emplacement_drapeau and [col, ligne] not in emplacement_decouvert: 
                                    if maps[ligne][col] == "B": # l"utilisateur a clique sur une bombe, donc il a perdu..
                                        fin_game = affiche_toute_les_cases(SCREEN, maps, emplacement_decouvert, "DEFAITE")
                                        run = False
                                    else:
                                        affiche_choix_chiffre(SCREEN, maps, col, ligne)
                                        emplacement_decouvert.append([col, ligne])
                                        print(emplacement_decouvert[len(emplacement_decouvert)-1])
                                    display.update()
                            
                            elif event.button == 3: # 3 = RIGHT
                                if [col, ligne] not in emplacement_drapeau: # l'utilisateur a fait un clique gauche sur une case vide
                                    if [col, ligne] not in emplacement_decouvert and len(emplacement_drapeau) < niveau[2]:  # pas possible de mettre plus de drapeau que de bombe
                                            emplacement_drapeau.append([col, ligne]) # x, y
                                            affiche_drapeau(SCREEN, possition_case, col, ligne, maps, emplacement_drapeau, niveau[2])# cree une fonction qui affiche un drapeau
                                else: #l'utilisateur a fait un clique gauche sur une case avec un drapeau
                                    emplacement_drapeau.pop(emplacement_drapeau.index([col, ligne]))
                                    affiche_supprimer_drapeau(SCREEN, maps, col, ligne, emplacement_drapeau, niveau[2]) #crée une fonction pour enlever le drapeau 
                            
                            if len(emplacement_decouvert)+len(emplacement_drapeau) == niveau[0]*niveau[1]:
                             
                             
                                    
                                fin_game = affiche_toute_les_cases(SCREEN, maps, emplacement_decouvert, "VICTOIRE")
                                run = False
    
    
    if fin_game == "":           
        main_demineur()

