import pygame
import pygame_gui
import pygame as pg
import sys
import random


def test_int(chiffre_par_utilisateur):
    chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for elem in chiffre_par_utilisateur:
        if elem not in chiffre:
            print(elem, chiffre)
            return False
    return True

def nombre_alea_bot():
    choix_bot = random.randint(0, 1000)
    return choix_bot








def regle(nombre_bot):
    affiche_regle = True
    while affiche_regle:

        regle_1 = f"dans ce juste prix vous devez choisir un nombre entre ( 0 - 1000 ) par exemple {nombre_bot}."
        regle_2 = "Le niveau facile bous avez 20 try pour le niveau moyen vous en avez 15"
        regle_3 ="pour le niveau hard vous en avez 10 BONNE CHANCE !"



        affiche_world_regle = pygame.font.SysFont("bahnschrift", 100).render("BONNE CHANCE", True, "red")
        world_regle = affiche_world_regle.get_rect(center=(WIDTH/2, HEIGHT/5))       


        regle_juste_prix_1 = pygame.font.SysFont("bahnschrift", 20).render(regle_1, True, "white")
        regle_juste_1 = regle_juste_prix_1.get_rect(center=(WIDTH/2, HEIGHT/1.7))


        regle_juste_prix_2 = pygame.font.SysFont("bahnschrift", 20).render(regle_2, True, "white")
        regle_juste_2 = regle_juste_prix_2.get_rect(center=(WIDTH/2, HEIGHT/1.7-50))   


        
        regle_juste_prix_3 = pygame.font.SysFont("bahnschrift", 20).render(regle_3, True, "white")
        regle_juste_3 = regle_juste_prix_3.get_rect(center=(WIDTH/2, HEIGHT/1.7-100))        
        
        affche_world_clique = pygame.font.SysFont("bahnschrift", 100).render("CLIQUE pour continuer", True, "red")
        world_clique = affche_world_clique.get_rect(center=(WIDTH/2, HEIGHT-100))    


        SCREEN.blit(regle_juste_prix_1, regle_juste_1)
        SCREEN.blit(regle_juste_prix_2, regle_juste_2)
        SCREEN.blit(regle_juste_prix_3, regle_juste_3)
        SCREEN.blit(affiche_world_regle, world_regle)
        SCREEN.blit(affche_world_clique, world_clique)

        pygame.display.update()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                affiche_regle = False







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

            
            #if event.type == pygame.MOUSEBUTTONDOWN: 
                # je test si l'utilisateur clique dans la case FACILE !
            

            if (WIDTH/4)-80 <= mouse[0] <= (WIDTH/4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                    
                facile = pygame.font.SysFont("bahnschrift", 30).render("vous avez le droit a 20 try", True, "white")
                nieau_facile = facile.get_rect(center=(WIDTH/4, HEIGHT/1.5+50))
                    
           

                SCREEN.blit(facile, nieau_facile)
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    return 20, 'facile'
            
            # je test si l'utilisateur clique dans la case MOYEN !
            elif (WIDTH/2)-80 <= mouse[0] <= (WIDTH/2)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                    
                moyen = pygame.font.SysFont("bahnschrift", 30).render("vous avez le droit a 15 try", True, "white")
                niveau_moyen = moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5+50))
                    

                SCREEN.blit(moyen, niveau_moyen)
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    return 15, 'moyen'
                

            # je test si l'utilisateur clique dans la case HARD !
            elif (WIDTH/1.4)-80 <= mouse[0] <= (WIDTH/1.4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                                
                hard = pygame.font.SysFont("bahnschrift", 30).render("vous avez le droit a 10 try", True, "white")
                niveau_hard = hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5+50))
                                
                
        
                SCREEN.blit(hard, niveau_hard)
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    return 10, 'difficile'

    
        pygame.display.update()



def partie_fini(score):
    affiche_fin_partie = True
    while affiche_fin_partie:


        text_affiche_rep = pygame.font.SysFont("bahnschrift", 100).render(score, True, "blue")
        lose = text_affiche_rep.get_rect(center=(WIDTH/2, HEIGHT/2))


        recommencer_une_partie = pygame.font.SysFont("bahnschrift", 30).render("cliquer pour RECOMMENCER !", True, "white") # affiche si le joueur veut refaire une partie !
        restart = recommencer_une_partie.get_rect(center=(WIDTH-200, HEIGHT-100))  # affiche la position du boutton !
             
        fond_acceil = pygame.image.load('main.jpg') # je dois mlettre une autre image
        fond_acceil = fond_acceil.convert()
        
        SCREEN.blit(fond_acceil, (0,0)) 
        SCREEN.blit(text_affiche_rep, lose)
        SCREEN.blit(recommencer_une_partie, restart)

        pygame.display.update()
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH-420 <= mouse[0] <= WIDTH and HEIGHT-120 <= mouse[1] <= HEIGHT:
                    main_juste_prix()
        
                    affiche_fin_partie = False # c'a signifie que toute les boucles sont fini, donc je quitte le programme
        



def affiche_fin_partie(numero_solution, numero):
    if numero_solution == numero:
        fin_de_partie = "VICTOIRE"
        fond = pygame.image.load('./victoire_carss.jpg') 
        couleur= "black"  

    else:
        fin_de_partie = "defaite.."
        fond = pygame.image.load('./lapin_pendu_defaite.jpg')
        couleur= "white"

    run_affice_fin = True
    while run_affice_fin:

    

        test_affiche_win = pygame.font.SysFont("bahnschrift", 100).render(fin_de_partie, True, couleur)  # affiche le gagnant !
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
                    main_juste_prix()
            
    print('LE programme est fini !')




def affiche_solution(numero_solution, numero, nombre_de_coup_utilise):
    

    if test_int(numero):  # je test, si tout les caractere que l'utilisateur a marqué sont des chiffres, et non des lettre ou symboles.
    
        numero = int(numero)


        continuee = True

        while continuee:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if numero_solution == numero:
                partie_fini('VICTOIRE') # je dois crée une fonction qui a pour but d affiche la vitoire, et de demande si l'utilisateur veux rejouer 

            if numero_solution < numero:
                text_affiche_rep = pygame.font.SysFont("bahnschrift", 40).render(f"Le chiffre est TROP GRAND", True, "white")
                lose = text_affiche_rep.get_rect(center=(WIDTH/2, HEIGHT-100))
            
            else: 
                text_affiche_rep = pygame.font.SysFont("bahnschrift", 40).render(f"Le chiffre est TROP PETIT", True, "white")
                lose = text_affiche_rep.get_rect(center=(WIDTH/2, HEIGHT-100))

            
            fond_acceil = pygame.image.load('main.jpg')
            fond_acceil = fond_acceil.convert()
            SCREEN.blit(fond_acceil, (0,0)) 
            SCREEN.blit(text_affiche_rep, lose)
            pygame.display.update()
            nombre_de_coup_utilise+=1
            continuee = False

    return nombre_de_coup_utilise

WIDTH, HEIGHT = 1600, 900
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Text Input in PyGame | BaralTech")

manager = pygame_gui.UIManager((1600, 900))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH//2-300, 275), (600, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pg.time.Clock()








def main_juste_prix():


    nombre_solution_ordinateur = nombre_alea_bot()
    regle(nombre_solution_ordinateur)
    fond_acceil = pygame.image.load('main.jpg')   # il faut mettre un autre foncpour le choix du niveau 
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0)) 

    nombre_de_coup_max, nom_niveau = choix_du_niveau() # cette fonction re voie le nombre de coup que l'utilisateru a le droit d'utiliser
    nombre_de_coup_utilise = 0

    fond_acceil = pygame.image.load('main.jpg')
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0)) 


    #SCREEN.blit(affiche_nombre_de_coup, nombre_de_coup) 


    run = True
    while run:


        affiche_nombre_de_coup = pygame.font.SysFont("bahnschrift", 40).render(f"tu es utilisé : {nombre_de_coup_utilise} / {nombre_de_coup_max} dans le mode {nom_niveau}", True, "white")
        nombre_de_coup = affiche_nombre_de_coup.get_rect(center=(WIDTH/2, 100))
        SCREEN.blit(affiche_nombre_de_coup, nombre_de_coup) 


        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                #event.text  = c'est le texte entré par l'utilisateur
                nombre_de_coup_utilise = affiche_solution(nombre_solution_ordinateur, event.text, nombre_de_coup_utilise)
                
                if nombre_de_coup_utilise == nombre_de_coup_max:
                    run = False

            manager.process_events(event)

            

            manager.update(UI_REFRESH_RATE)
            manager.draw_ui(SCREEN)
            pygame.display.update()
        
    affiche_fin_partie(nombre_solution_ordinateur, event.type)



main_juste_prix()