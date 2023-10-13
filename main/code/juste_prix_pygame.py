import pygame
import pygame_gui
import pygame as pg
import random


def test_int(chiffre_par_utilisateur):
    chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for elem in chiffre_par_utilisateur:
        if elem not in chiffre:
            return False
    return True


def nombre_alea_bot():
    choix_bot = random.randint(0, 1000)
    return choix_bot








def regle(SCREEN, nombre_bot):
    affiche_regle = True
    while affiche_regle:

        regle_3 = f"dans ce juste prix vous devez choisir un nombre entre ( 0 - 1000 ) par exemple {nombre_bot}."
        regle_2 = "Le niveau facile vous avez 20 try pour le niveau moyen vous en avez 15"
        regle_1 ="pour le niveau hard vous en avez 10 BONNE CHANCE !"



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
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                return True





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
    
    
    
    text_facile = pygame.font.SysFont("bahnschrift", 30).render("vous avez le droit a 10 try", True, "white")
    text_nieau_facile = text_facile.get_rect(center=(WIDTH/4, HEIGHT/1.5+50))
       
       
    text_moyen = pygame.font.SysFont("bahnschrift", 30).render("vous avez le droit a 15 try", True, "white")
    text_niveau_moyen = text_moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5+50))
            
    text_hard = pygame.font.SysFont("bahnschrift", 30).render("vous avez le droit a 20 try", True, "white")
    text_niveau_hard = text_hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5+50))
       
    
       
       
                        
    while affiche_choix_niveau:

        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, "quitte"

            
        # je test si l'utilisateur clique dans la case FACILE !
        if (WIDTH/4)-80 <= mouse[0] <= (WIDTH/4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                    

            SCREEN.blit(text_facile, text_nieau_facile)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return 20, 'facile'
            
        # je test si l'utilisateur clique dans la case MOYEN !
        elif (WIDTH/2)-80 <= mouse[0] <= (WIDTH/2)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                    
            SCREEN.blit(text_moyen, text_niveau_moyen)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return 15, 'moyen'
                

        # je test si l'utilisateur clique dans la case HARD !
        elif (WIDTH/1.4)-80 <= mouse[0] <= (WIDTH/1.4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+50:
                                
            SCREEN.blit(text_hard, text_niveau_hard)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return 10, 'difficile'

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




def affiche_fin_partie(SCREEN, numero_solution, numero):
    print('yyyyyyyyyyyyy')
    if numero_solution == numero:
        fin_de_partie = "VICTOIRE"
        fond = pygame.image.load('./image/victoire_carss.jpg') 
        couleur= "black"  

    else:
        fin_de_partie = "defaite.."
        fond = pygame.image.load('./image/lapin_pendu_defaite.jpg')
        couleur= "white"

    run_affice_fin = True
    while run_affice_fin:

    

        test_affiche_win = pygame.font.SysFont("bahnschrift", 100).render(fin_de_partie, True, couleur)  # affiche le gagnant !
        win = test_affiche_win.get_rect(center=(WIDTH/4, HEIGHT/3))  # c'est la position ou j 'affiche le gagnant
        
                        
        recommencer_une_partie = pygame.font.SysFont("bahnschrift", 30).render("cliquer pour RECOMMENCER !", True, "white") # affiche si le joueur veut refaire une partie !
        restart = recommencer_une_partie.get_rect(center=(WIDTH-200, HEIGHT-100))  # affiche la position du boutton !

        nombre_bot = pygame.font.SysFont("bahnschrift", 40).render(f"le nombre à trouver était: {numero_solution}", True, "white")
        affiche_nombre_bot = nombre_bot.get_rect(center=(300, HEIGHT-100))

        fond = fond.convert()
        SCREEN.blit(fond, (0,0))        
        fond = fond.convert()
        SCREEN.blit(fond, (0,0))
        SCREEN.blit(test_affiche_win, win)  
        SCREEN.blit(recommencer_une_partie, restart)
        SCREEN.blit(nombre_bot, affiche_nombre_bot)

        mouse = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_affice_fin = False
                        
            if event.type == pygame.MOUSEBUTTONDOWN: #je test si il y a un clique sur le boutton pour recommence une partie 
                if WIDTH-420 <= mouse[0] <= WIDTH and HEIGHT-120 <= mouse[1] <= HEIGHT: 
                    main_juste_prix()
                    run_affice_fin = False

    print('LE programme est fini !')




def affiche_solution(SCREEN, numero_solution, numero, nombre_de_coup_utilise):
    

    numero = int(numero)

    fin = ""
    if numero_solution == numero:
        print('okok c est win !')
        return nombre_de_coup_utilise

    if numero_solution < numero:
        text_affiche_rep = pygame.font.SysFont("bahnschrift", 40).render(f"Le chiffre est TROP GRAND", True, "white")
        lose = text_affiche_rep.get_rect(center=(WIDTH/2, HEIGHT-100))
            
    else: 
        text_affiche_rep = pygame.font.SysFont("bahnschrift", 40).render(f"Le chiffre est TROP PETIT", True, "white")
        lose = text_affiche_rep.get_rect(center=(WIDTH/2, HEIGHT-100))

            
    fond_acceil = pygame.image.load('./image/main.jpg')
    fond_acceil = fond_acceil.convert()
    SCREEN.blit(fond_acceil, (0,0)) 
    SCREEN.blit(text_affiche_rep, lose)
    pygame.display.update()
    nombre_de_coup_utilise+=1







WIDTH, HEIGHT = 1300, 1000  #  1600, 900 fixe  ; 1600, 1200







def main_juste_prix():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()
    pygame.display.set_caption(f"Le juste prix")

    manager = pygame_gui.UIManager((1600, 900))

    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH//2-300, 275), (600, 50)), manager=manager,
                                                object_id='#main_text_entry')

    clock = pg.time.Clock()

    fin = ""
    SCREEN.fill((0, 0, 0)) # fond en noir
    nombre_solution_ordinateur = nombre_alea_bot()
    run = regle(SCREEN, nombre_solution_ordinateur)
    if run == True:
        fond_acceil = pygame.image.load('./image/main.jpg')   # il faut mettre un autre foncpour le choix du niveau 
        fond_acceil = fond_acceil.convert()
        SCREEN.blit(fond_acceil, (0,0)) 


        nombre_de_coup_max, nom_niveau = choix_du_niveau(SCREEN) # cette fonction renvoie le nombre de coup que l'utilisateru a le droit d'utiliser
        if nom_niveau == "quitte":
            fin = "quitte"
            run = False
            
        else:
            nombre_de_coup_utilise = 0

            fond_acceil = pygame.image.load('./image/main.jpg')
            fond_acceil = fond_acceil.convert()
            SCREEN.blit(fond_acceil, (0,0)) 
           
    else:
        fin = "quitte"
        run = False
    
    result = 0
    
    while run:


        affiche_nombre_de_coup = pygame.font.SysFont("bahnschrift", 40).render(f"tu as utilisé : {nombre_de_coup_utilise} / {nombre_de_coup_max} dans le mode {nom_niveau}", True, "white")
        nombre_de_coup = affiche_nombre_de_coup.get_rect(center=(WIDTH/2, 100))
        SCREEN.blit(affiche_nombre_de_coup, nombre_de_coup)


        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = "quitte"
                run = False
               

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                
                if test_int(event.text):
                    affiche_solution(SCREEN, nombre_solution_ordinateur, event.text, nombre_de_coup_utilise)
                    nombre_de_coup_utilise += 1
                    
                    print(nombre_solution_ordinateur, event.text)
                    print('TTTTTTTTTT')
                    if nombre_de_coup_utilise == nombre_de_coup_max or nombre_solution_ordinateur == int(event.text):
                        result = int(event.text)
                        run = False
                        
               
            manager.process_events(event)
            

            

            manager.update(UI_REFRESH_RATE)
            manager.draw_ui(SCREEN)
            pygame.display.update()
        

   
    if fin != "quitte":
        
        affiche_fin_partie(SCREEN, nombre_solution_ordinateur, result)
