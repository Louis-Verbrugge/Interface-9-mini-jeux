from pygame import *
import pygame
import sys
import random




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
       
     
       
       
            
def nombre_de_bombe_dans_les_zones(nb_bombe, nb_zone):
    """_summary_

    Args:
        nb_bombe (integer): nombre de bombe
        nb_zone (integer): nombre de zone
    """
    return
    
    
    
    
def mise_en_place_bombe_sur_la_maps(zone_pour_bombe, maps, nb_bombe_par_zone):  # voici la zone impossible, maintenant je dois test que la zone ne peut pas avoir de bombe.
    """_summary_

    Args:
        zone_pour_bombe (liste de liste): contient les coordonnes de toute les zones
        maps (liste): maps du jeu 
        nb_bombe_par_zone (integer): nombre de bombe par zone
    """
    
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
    
    
    
    
    
def mise_en_place_bombe(maps, niveau): # les valeurs dans l'ordre 0, 1, 2, 3 = hauteur, largeur, nombre_de_bombe, nb_zone
    """_summary_

    Args:
        maps (_type_): _description_
        niveau (_type_): _description_
    """
    # EXPLICATION #
    """
    cette fonctioon a pour but de modifier la maps pour poser les bombes, pour ca je prends la carte et je prends un certain nombre aléatoire entre 0, 4, c'est deux nombre signifie la ou les bombe vont etre.
    et ensuite je vais modifie la maps pour mettre les bombes pour ensuite return la maps
    """
    
    zone_pour_bombe = choisir_les_zones(niveau[3])
    # maintenant j ai les deux zone !  
    
    # je cherche la moitie du nombre de bombe total :
    
    """
    crée une fonction ou les bombes sont mieux dispersé !
    """
    # nb_bombe_par_zone = nb_bombe / nb _zone
    nb_bombe_par_zone = niveau[2] // niveau[3]
    
    mise_en_place_bombe_sur_la_maps(zone_pour_bombe, maps, nb_bombe_par_zone)


    
    
    
    
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
                            #print(maps[coordonne_y-1+hauteur][coordonne_x-1+largeur])
                            maps[coordonne_y-1+hauteur][coordonne_x-1+largeur] = maps[coordonne_y-1+hauteur][coordonne_x-1+largeur]+1
                            
                            
                            

def emplacement_case(maps): # (x x' y y')
    emplacement_casee = []
    for ligne in range (len(maps)):
        emplacement_casee.append([])
        for col in range (len(maps[0])):
            emplacement_casee[ligne].append([300+((WIDTH-600)/len(maps[0]))*col, 300+((WIDTH-600)/len(maps[0]))*col + ((WIDTH-600)/len(maps[0])), 150+((HEIGHT-300)/len((maps)))*ligne, 150+((HEIGHT-300)/len((maps)))*ligne + ((HEIGHT-300)/len((maps)))])
            
    return emplacement_casee

            
            
def emplacement_zone():
    taille_x = 3  # 3 car je divise la maps en 9 donc 3 largeur et 3 hauteur
    taille_y = 3
    print(taille_x, taille_y)
    
    emplacement_zonee = []
    
    for ligne in range (taille_x):
        for col in range (taille_y):
            
            emplacement_zonee.append([300+((WIDTH-600)/3)*col, 300+((WIDTH-600)/3)*(col+1) , 150+((HEIGHT-300)/3)*ligne , 150+((HEIGHT-300)/3)*(ligne+1)])
            
    
    return emplacement_zonee     
            
            
            
            
            
            
            
        
def affiche_maps_debut_game(maps, emplacement_decouvert):
    
    for ligne in range (len(maps)):
        accu = 0
        for col in range (len(maps[0])):
            
    
            
            if maps[ligne][col] == 0: # j'affiche les valeurs == 0
                affiche_choix_chiffre(maps, col, ligne)
                emplacement_decouvert.append([col, ligne])
    
    
            elif accu % 2 == 0:
                if maps[ligne][col] != "B":  # je cherche si les autres valeur sont a cote d'un 0, si oui j affiche cette case
                    affiche_choix_chiffre(maps, col, ligne)
                    emplacement_decouvert.append([col, ligne])
            accu+=1
    
    print('4TTTTTTTTTTT')
    print(accu)
    for elem in emplacement_decouvert:
        print(elem)
        
    return emplacement_decouvert
        
        
        
        
def affiche_drapeau(possition_case, coordonne_case_x, coordonne_case_y):
    
    # création du drapeau
    
    # je cherche le premier point x :
    
    # je sais que toute les cases font la meme taille, donc j vais prendre la premier pour cherche leur taille:
    taille_x = possition_case[0][0][1] - possition_case[0][0][0]
    taille_y = possition_case[0][0][3] - possition_case[0][0][2]
    
    rep_x = (2/3)*taille_x
    point_x_depart = (taille_x-rep_x)/2 # point base ligne drapeau - x
    
    rep_y = (2/3)*taille_y
    point_y_depart = (taille_y-rep_y)/2 # point base ligne drapeau - y
    
    # j'affiche la ligne verticale :
    pygame.draw.line(SCREEN, RED, (300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart, 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart), (300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart, 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart + rep_y), 4)   # la ligne vertical



    # j'affiche le triangle pour faire le drapeau :
    pygame.draw.polygon(SCREEN, RED, [
                        [300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart , 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart], # (x, y) du point du triangle
                        [300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart , 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart + (rep_y)/2], # (x, y) du point du triangle
                        [300+((WIDTH-600)/len(maps[0]))*coordonne_case_x + point_x_depart + taille_x/2, 150+((HEIGHT-300)/len(maps))*coordonne_case_y + point_y_depart + (rep_y/4)]])# (x, y) du point du triangle
        
        
        
        
        
        
        
        
def affiche_supprimer_drapeau(maps, coordonne_x, coordonne_y):
    
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
        
        
        
        
        
        
        
        
        
        
        
        
        
def affiche_toute_les_cases(maps, emplacement_decouvert):
    accu = 0 # A SUPPRIMER
    print('mais juste pourquoi ?') # A SUPPRIMER
    for ligne in range (len(maps)):
        for col in range (len(maps[0])):
            if [col, ligne] not in emplacement_decouvert:
                accu+=1 # A SUPPRIMER
                print(f"TREZ {accu}") # A SUPPRIMER
                
                print(ligne, col)
                affiche_choix_chiffre(maps, col, ligne)
      
                display.update()      
    run_defaite = True
    while run_defaite:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                run_defaite = False

        
        
        
        
        
        
        
        
        
            
            
            
def creation_maps(collun, ligne, valeur):
    maps = []
    for _ in range (ligne):
        maps.append([x-x+valeur for x in range (collun)])
    return maps




def affichage_maps_init(maps):
    print('FFF')
    print(maps)
    accu = 0
    
    for ligne in range (len(maps)):
        for col in range (len(maps[0])):
            
            
            if accu % 2 == 0:
                pygame.draw.rect(SCREEN, GREEN_CLAIR, (300+((WIDTH-600)/len(maps[0]))*col, 150+((HEIGHT-300)/len(maps))*ligne, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps))))) 
                
            else:
                pygame.draw.rect(SCREEN, GREEN_FONCE, (300+((WIDTH-600)/len(maps[0]))*col, 150+((HEIGHT-300)/len(maps))*ligne, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
            
                        
            accu+=1
    
    
    
    
    
    
def initilisation_cherche_maps_adapte(maps, possition_zone):
      # je dois crée une fonction qui contient les coordonnes des 9 zones, 
    # ensuite je recherche le clique pour revoier la zone qui ne peut pas contenir de bombe
    affichage_maps_init(maps)
    
    
    for elem in possition_zone:
        print(elem)
    
    
    
    print("OKOIKKF")
    display.update()
    
    run_init = True
    while run_init:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
                
            
            if event.type == MOUSEBUTTONDOWN:
                for zone in range (len(possition_zone)):
                    if possition_zone[zone][0] <= mouse[0] <= possition_zone[zone][1] and possition_zone[zone][2] <= mouse[1] <= possition_zone[zone][3]:
                     
                            
                     
                            print(f"c'est la ZONE : {zone}")  # col = x ///  ligne = y
                            run_init = False
              
          
    
    
    
    
    
def affiche_choix_chiffre(maps, coordonne_x, coordonne_y):
    chiffre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    if maps[coordonne_y][coordonne_x] in chiffre:#l'utilisateur a clique sur un chiffre !
        pygame.draw.rect(SCREEN, SABLE, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
            
            
        nombre_trouve = pygame.font.SysFont("bahnschrift", 30).render(str(maps[coordonne_y][coordonne_x]), True, "white")
        affiche_nombre_trouve = nombre_trouve.get_rect(center=((300+((WIDTH-600)/len(maps[0]))*coordonne_x)+ ((WIDTH-600)/len(maps[0]))/2, (150+((HEIGHT-300)/len(maps))*coordonne_y)+((HEIGHT-300)/len(maps))/2))
        SCREEN.blit(nombre_trouve, affiche_nombre_trouve)
        
            
    else: #l'utilisateur a cliqué sur une bombe..
        pygame.draw.rect(SCREEN, RED, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps))))) 
        print('TTTT')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
def choix_du_niveau():
    affiche_choix_niveau = True
    fond_acceil = pygame.image.load('main.jpg')
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0)) 
    while affiche_choix_niveau:


        fond_acceil = pygame.image.load('main.jpg')
        fond_acceil = fond_acceil.convert()
        SCREEN.blit(fond_acceil, (0,0)) 

        
        choix_du_niveau = pygame.font.SysFont("bahnschrift", 50).render("Choisissez un niveau :", True, "white")
        affiche_niveau = choix_du_niveau.get_rect(center=(WIDTH/2, HEIGHT/3))

        facile = pygame.font.SysFont("bahnschrift", 50).render("FACILE", True, "white")
        nieau_facile = facile.get_rect(center=(WIDTH/4, HEIGHT/1.5))

        moyen = pygame.font.SysFont("bahnschrift", 50).render("MOYEN", True, "white")
        niveau_moyen = moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5))

        hard = pygame.font.SysFont("bahnschrift", 50).render("HARD", True, "white")
        niveau_hard = hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5))        

    

        SCREEN.blit(choix_du_niveau, affiche_niveau)

        SCREEN.blit(facile, nieau_facile)
        SCREEN.blit(moyen, niveau_moyen)
        SCREEN.blit(hard, niveau_hard)

        pygame.draw.rect(SCREEN, (0, 0, 0), ((WIDTH/4)-85, (HEIGHT/1.5)-40, 175, 70), 2) #  facile 
        pygame.draw.rect(SCREEN, (0, 0, 0), ((WIDTH/2)-85, (HEIGHT/1.5)-40, 175, 70), 2) # moyen
        pygame.draw.rect(SCREEN, (0, 0, 0), ((WIDTH/1.4)-70, (HEIGHT/1.5)-40, 150, 70), 2) # hard

        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            

        if (WIDTH/4)-80 <= mouse[0] <= (WIDTH/4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
                    
            facile = pygame.font.SysFont("bahnschrift", 30).render("plutôt facile", True, "white")
            nieau_facile = facile.get_rect(center=(WIDTH/4, HEIGHT/1.5+50))
            
            SCREEN.blit(facile, nieau_facile)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [12, 9, 15, 3], 'facile'

            
        # je test si l'utilisateur clique dans la case MOYEN !
        elif (WIDTH/2)-80 <= mouse[0] <= (WIDTH/2)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
                    
            moyen = pygame.font.SysFont("bahnschrift", 30).render("c'est complexe", True, "white")
            niveau_moyen = moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5+50))
                    

            SCREEN.blit(moyen, niveau_moyen)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [18, 15, 40, 5], 'moyen'
                


        # je test si l'utilisateur clique dans la case HARD !
        elif (WIDTH/1.4)-80 <= mouse[0] <= (WIDTH/1.4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
                                
            hard = pygame.font.SysFont("bahnschrift", 30).render("c'est vraiment très complexe", True, "white")
            niveau_hard = hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5+50))
            
            SCREEN.blit(hard, niveau_hard)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [24, 21, 96, 8], 'difficile'

        
    
        pygame.display.update()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SABLE = (218, 229, 179)

GREEN_CLAIR = (57, 255, 4)
GREEN_FONCE = (0, 113, 14)

WIDTH, HEIGHT = 1400, 1100   ### WIDTH, HEIGHT = 1000, 800

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Démineur")



niveau = choix_du_niveau()[0]  # [0] = tuple qui contient les info du niveau;   [1] = nom du niveau ('facile', 'moyen', 'hard')
print(niveau, type(niveau))

nombre_de_case_decouverte = 0 # si le "nombre_de_case_decouverte" == toute les case - bombe, le joueur WiN !!! 



maps = creation_maps(niveau[1], niveau[0], -1) # (x; y, i pour l'init)
for elem in maps:
    print(elem)
    
possition_case = emplacement_case(maps)

for elem in possition_case:
    print(elem)
print(possition_case[0][0])

    
emplacement_zonee = emplacement_zone()
initilisation_cherche_maps_adapte(maps, emplacement_zonee)
#affichage_maps_init(maps) # je cherche ou l'utilisateur a clique pour ne pas prendre cette zone

maps = creation_maps(niveau[1], niveau[0], 0)


mise_en_place_bombe(maps, niveau)
chiffre_a_cote_bombe(maps) 

emplacement_drapeau = []
emplacement_decouvert = [] 
emplacement_decouvert = affiche_maps_debut_game(maps, emplacement_decouvert)
resultat_fin_partie = ""

print(len(emplacement_decouvert))
print('TTTTTTDDDDDDDDGGGGGGGGGGGGGGG')
nb_de_case_a_atteindre = (niveau[0]*niveau[1])-niveau[2]

print(maps)

#affiche_maps_debut_game() # crée une fonction qui affiche tout les cases en 0 et affiche toute les case qui touche le 0

run = True
while run:
    emplacement_decouvert = affiche_maps_debut_game(maps, emplacement_decouvert)
    
    mouse = pygame.mouse.get_pos()
    display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
        if event.type == MOUSEBUTTONDOWN:
            for ligne in range (len(maps)):
                for col in range (len(maps[0])):
                    if possition_case[ligne][col][0] <= mouse[0] <= possition_case[ligne][col][1] and possition_case[ligne][col][2] <= mouse[1] <= possition_case[ligne][col][3]:
                        
                        print(f"c'est la case x : {col} ---- y : {ligne}")  # col = x ///  ligne = y
                        if event.button == 1:  # 1 = LEFT 
                            
                            print([col, ligne] not in emplacement_drapeau)
                            print('WAITTTTT')
                            
                            
                            if [col, ligne] not in emplacement_drapeau: 
                                
                                
                        
                                if maps[ligne][col] == "B": # l"utilisateur a clique sur une bombe, donc il a perdu..
                                    affiche_toute_les_cases(maps, emplacement_decouvert)
                                    resultat_fin_partie = "DEFAITE"
                                    run = False
                                    
                                else:
                                    print("clique GAUCHEEEEE")
                                    affiche_choix_chiffre(maps, col, ligne)
                                    print('FGDCV')
                                    
                                    emplacement_decouvert.append([col, ligne])
                               
                                print('TTTTT')
                                print(len(emplacement_decouvert), niveau[2])
                                print(niveau[0]*niveau[1])
                                print('AAAAAAAAAAAAAAA')
                                

                            
                        elif event.button == 3: # 3 = RIGHT
                            if [col, ligne] not in emplacement_drapeau: # l'utilisateur a fait un clique gauche sur une case vide
                                if [col, ligne] not in emplacement_decouvert:# JE DOIS TESTE SI LA CASE EST AFFICHE OU NON, car si elle est affiche c'est inutile
                                    if len(emplacement_drapeau) < niveau[2]:  # pas possible de mettre plus de drapeau que de bombe
                                        print("clique DROITEEEE")
                                        affiche_drapeau(possition_case, col, ligne)# cree une fonction qui affiche un drapeau
                                        emplacement_drapeau.append([col, ligne]) # x, y
                        
                            else: #l'utilisateur a fait un clique gauche sur une case avec un drapeau
                                affiche_supprimer_drapeau(maps, col, ligne) #crée une fonction pour enlever le drapeau 
                                print('1')
                                emplacement_drapeau.pop(emplacement_drapeau.index([col, ligne]))
                                print('2')
                                print(emplacement_drapeau)
                           
                                
                        if len(emplacement_decouvert)+len(emplacement_drapeau) == niveau[0]*niveau[1]:
                                print('FINNN §§ TU AS WINN ! ')
                                resultat_fin_partie = "VICTOIRE"
                                run = False
                                ... # affiche la victoire
 
 
                               
print(resultat_fin_partie) # fonction mais pas tout le temps...