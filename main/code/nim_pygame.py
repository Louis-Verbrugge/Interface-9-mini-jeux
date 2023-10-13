import pygame
import random
import time




def affiche_allumette_and_button(SCREEN, nombre_allumettes, mouvement_log):

    fond_acceil = pygame.image.load('./image/main.jpg') 
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0)) 

    for i in range (nombre_allumettes):  # nombre_allumettes
        pygame.draw.rect(SCREEN, BLACK, (60+48*i, HEIGHT/3, 20, HEIGHT/2-150))
        pygame.draw.circle(SCREEN, RED, (70+48*i, HEIGHT/3-5), 12)
        
    chiffre = ['1', '2', '3']
    for i in range(len(coordonne_button)):  # j affiche le contour des boutons
        pygame.draw.rect(SCREEN, WHITE, (coordonne_button[i], HEIGHT/1.3, 300, 150)) # button 1; button 2; button 3  # centre
        pygame.draw.rect(SCREEN, BLACK, (coordonne_button[i], HEIGHT/1.3, 300, 150), 8) # button 1; button 2; button 3  # contour 


    
    for i in range (len(chiffre)):  # j'affiche le chiffre au millieu des boutons
        world = pygame.font.SysFont("bahnschrift", 30).render(chiffre[i], True, "black")
        affiche_world_1 = world.get_rect(center=(coordonne_button[i]+150, HEIGHT/1.3+75))
        SCREEN.blit(world, affiche_world_1)

    nombre_allumettes_reste = pygame.font.SysFont("bahnschrift", 40).render(f"Il reste {nombre_allumettes} allumette(s)", True, "black")  # affiche le gagnant !
    affiche_nombre_allumettes_reste = nombre_allumettes_reste.get_rect(center=(400, 100))  # c'est la position ou j 'affiche le gagnant
    SCREEN.blit(nombre_allumettes_reste, affiche_nombre_allumettes_reste)
    affiche_log(SCREEN, mouvement_log)



def affiche_log(SCREEN, mouvement_log):
    mouvement = [mouvement_log[len(mouvement_log)-1-i] for i in range(min(len(mouvement_log), 5))]
    accu = 0
    for elem in mouvement:
        log = pygame.font.SysFont("bahnschrift", 30).render(elem, True, "black")
        affiche_log = log.get_rect(center=(WIDTH-400, 100+30*accu))   # affiche_world_1 = world.get_rect(center=(WIDTH-400, 100+100*i))
        SCREEN.blit(log, affiche_log)
        accu+=1





def choix_du_niveau(SCREEN):
    affiche_choix_niveau = True
    fond_acceil = pygame.image.load('./image/main.jpg')
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
    
    
    
    text_facile = pygame.font.SysFont("bahnschrift", 30).render("tres facile", True, "white")
    text_nieau_facile = text_facile.get_rect(center=(WIDTH/4, HEIGHT/1.5+50))
       
       
    text_moyen = pygame.font.SysFont("bahnschrift", 30).render("moyen", True, "white")
    text_niveau_moyen = text_moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5+50))
            
    text_hard = pygame.font.SysFont("bahnschrift", 30).render("IMPOSSIBLE !", True, "white")
    text_niveau_hard = text_hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5+50))
       
    
       
       
                        
    while affiche_choix_niveau:

        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quitte'

            
        # je test si l'utilisateur clique dans la case FACILE !
        if (WIDTH/4)-80 <= mouse[0] <= (WIDTH/4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                    

            SCREEN.blit(text_facile, text_nieau_facile)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return 1
            
        # je test si l'utilisateur clique dans la case MOYEN !
        elif (WIDTH/2)-80 <= mouse[0] <= (WIDTH/2)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                    
            SCREEN.blit(text_moyen, text_niveau_moyen)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return 2
                

        # je test si l'utilisateur clique dans la case HARD !
        elif (WIDTH/1.4)-80 <= mouse[0] <= (WIDTH/1.4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                                
            SCREEN.blit(text_hard, text_niveau_hard)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return 3

        else:
            SCREEN.blit(fond_acceil, (0,0)) 
            SCREEN.blit(choix_du_niveau, affiche_niveau)

            SCREEN.blit(facile, nieau_facile)
            SCREEN.blit(moyen, niveau_moyen)
            SCREEN.blit(hard, niveau_hard)
            pygame.draw.rect(SCREEN, (0, 0, 0), ((WIDTH/4)-85, (HEIGHT/1.5)-40, 175, 70), 2) #  facile 
            pygame.draw.rect(SCREEN, (0, 0, 0), ((WIDTH/2)-85, (HEIGHT/1.5)-40, 175, 70), 2) # moyen
            pygame.draw.rect(SCREEN, (0, 0, 0), ((WIDTH/1.4)-70, (HEIGHT/1.5)-40, 150, 70), 2) # hard
        
    
        pygame.display.update()






def choix_ordinateur_facile(nombre_allumettes):
    nombre_choisi = random.randint(1,min(3,nombre_allumettes))     # nombre_choisi stocke la reponse de l'ordinateur
    
    print (f'l\'ordinateur choisi de prendre {nombre_choisi} allumette(s)')
    return nombre_choisi




def choix_ordinateur_moyen(nombre_allumettes):
    x = random.randint(1,2)      # 1 et le choix facile et 2 et le choix difficile 
    if x == 1:
        return choix_difficile(nombre_allumettes)
    else:
        return choix_ordinateur_facile(nombre_allumettes)



def choix_difficile(nombre_allumettes):
        
    if nombre_allumettes %4 == 3:
        nombre_choisi = 2   
    else:    
        if nombre_allumettes %4 == 2:                                                    
            nombre_choisi = 1   
        else:
            if nombre_allumettes %4 == 0:
                nombre_choisi = 3  
            else:
               nombre_choisi = random.randint(1,min(3,nombre_allumettes))
    print(f'l ordinateur prend {nombre_choisi} allumettes') 
    return nombre_choisi






def affiche_fin_partie(SCREEN, prochain_joueur):
    if prochain_joueur == 1: # VICTOIRE
        fin_de_partie = "VICTOIRE"
        fond = pygame.image.load('./image/victoire_carss.jpg') 
        couleur = "black"  

    else: # defaite..
        fin_de_partie = "defaite.."
        fond = pygame.image.load('./image/lapin_pendu_defaite.jpg')
        couleur = "white"

    run_affice_fin = True
    while run_affice_fin:

    

        test_affiche_win = pygame.font.SysFont("bahnschrift", 100).render(fin_de_partie, True, couleur)  # affiche le gagnant !
        win = test_affiche_win.get_rect(center=(WIDTH/4, HEIGHT/3))  # c'est la position ou j 'affiche le gagnant
        
                        
        recommencer_une_partie = pygame.font.SysFont("bahnschrift", 30).render("cliquer pour RECOMMENCER !", True, "white") # affiche si le joueur veut refaire une partie !
        restart = recommencer_une_partie.get_rect(center=(WIDTH-250, HEIGHT-100))  # affiche la position du boutton !


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
                    main_jeu_de_min()
                    run_affice_fin = False
            
    print('LE programme est fini !')




WIDTH, HEIGHT = 1300, 900   #  1600, 900 fixe


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


coordonne_button = [WIDTH/8, WIDTH/2.5, WIDTH/2.5+(WIDTH/2.5-WIDTH/8)]  # button 1; button 2; button 3



def main_jeu_de_min():

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"jeu de nim")
    pygame.init()  
    mouvement_log = []
    nombre_allumettes = 25
    niveau = choix_du_niveau(SCREEN)  # 1 = facile; 2 = moyen; 3 = hard
    fin = ""


    premier_joueur = random.randint(1,2) # 1 = humain; 2 = ordinateur
    affiche_allumette_and_button(SCREEN, nombre_allumettes, mouvement_log)


    
    
    print(f" LE CHOIX DU NIVEAU ET {niveau}")
    
    if niveau == "quitte":
        run = False
        fin = "quitte"
    else:
        run = True
        pygame.display.update()
        
    while run:
              
        
        
        if premier_joueur == 2: # l'odinateur joue !
            if niveau == 1:
                choix_bot = choix_ordinateur_facile(nombre_allumettes)
                
            elif niveau == 2:
                choix_bot = choix_ordinateur_moyen(nombre_allumettes)
                
            else:
                choix_bot = choix_difficile(nombre_allumettes)

            nombre_allumettes -= choix_bot

            mouvement_log.append(f"l'ordinateur a pris {choix_bot} allumette(s)")

            # je modifie l'affichage car il n'y a plus le meme nombre d'allumettes
            time.sleep(0.5)
            affiche_allumette_and_button(SCREEN, nombre_allumettes, mouvement_log)
            pygame.display.update()

            if nombre_allumettes == 0:
                run = False
            premier_joueur = 1

        

        elif premier_joueur == 1: # l'utilisateu joue !
            mouse = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    fin = 'quitte'



                if event.type == pygame.MOUSEBUTTONDOWN:    
                    for i in range (len(coordonne_button)):  # cette boucle test, si il y a un clique sur un des trois bouttons.
                        
                        # je test maintanant pour le boutton n°2 :  
                        if coordonne_button[i] <= mouse[0] <= coordonne_button[i]+300 and HEIGHT/1.3 <= mouse[1] <= HEIGHT/1.3+150:
                            
                            if i+1 <= nombre_allumettes:
                                nombre_allumettes-=i+1   # j'enleve le nombre d'allumette choisie par l'ulisateur    
                            
                                mouvement_log.append(f"Vous avez pris {i+1} allumette(s)")
                                # je modifie l'affichage car il n'y a plus le meme nombre d'allumettes
                                
                                
                                
                                affiche_allumette_and_button(SCREEN, nombre_allumettes, mouvement_log)
                                pygame.display.update()
                                premier_joueur = 2 # c'est a l'ordinateur de jouer !
                                if nombre_allumettes == 0:
                                    run = False
               

    if fin != "quitte":
        affiche_fin_partie(SCREEN, premier_joueur) # 1 = humain win; 2 = ordinateur win       