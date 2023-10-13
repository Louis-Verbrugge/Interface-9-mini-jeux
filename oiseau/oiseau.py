import pygame
import sys
import random
import time

WIDTH, HEIGHT = 700, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

pygame.display.set_caption("Bird fly but it's not a bird, it's a circle") #titre de la page, fin  pas sur 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)



class Oiseau:
    def __init__(self, x, y, Vx, Vy, rayon):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.rayon = rayon
        

    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y  
    
    
    def get_Vx(self):
        return self.Vx
 
    def get_Vy(self):
        return self.Vy
    
            
    def set_x(self, nouveau_x):
        self.x = nouveau_x
        
    def set_y(self, nouveau_y):
        self.y = nouveau_y
    
    def set_Vx(self, nouveau_Vx):
        self.Vx = nouveau_Vx
        
    def set_Vy(self, nouveau_Vy):
        self.Vy = nouveau_Vy
    
    
    def get_rayon(self):
        return self.rayon
    
    
          
    def __str__(self):
        return "coordonne x : " + str(self.x) + " coordonne y : " + str(self.y)
  
  

  
  
  
def deplace_birds(birds, possition):
    birds.set_x(birds.get_x() + birds.get_Vx())
    birds.set_y(birds.get_y() + birds.get_Vy())
    
    defaire_or_continue = test_si_defaite(birds, possition)
    return defaire_or_continue
     
     
     

def rebond_mur(birds, possition, score):
    
    
    if 0 >= birds.get_x() - birds.get_rayon():   # JE vrif si la birds touche le mur a gauche
        birds.set_Vx(-1*birds.get_Vx())
        
        possition.clear()
        possition = trouve_possition_spick_wall(5, possition)
        
        score+=1
        SCREEN.fill((0, 0, 0))

    elif WIDTH <= birds.get_rayon()+birds.get_x():   # JE vrif si la birds touche le mur a droite
        birds.set_Vx(-1*birds.get_Vx())
        
        possition.clear()
        possition = trouve_possition_spick_wall(5, possition)
        score+=1 
        SCREEN.fill((0, 0, 0))

    
    return possition, score
     
     
     
     
     
     
   
def spick_plafond_and_sol_score(possition, score):
    
    for i in range (14):
        
        # plafond:
        pygame.draw.line(SCREEN, RED, (0+50*i, 0), (25+50*i, 25))
        pygame.draw.line(SCREEN, RED, (50+50*i, 0), (25+50*i, 25))
        
        # sol:
        pygame.draw.line(SCREEN, RED, (0+50*i, HEIGHT), (25+50*i, HEIGHT-25))
        pygame.draw.line(SCREEN, RED, (50+50*i, HEIGHT), (25+50*i, HEIGHT-25))         
    
    
    spick_mur(possition)

    #affiche_resultatt = pygame.font.SysFont("bahnschrift", 100).render(str(score), True, "white")
    #SCREEN.blit(pygame.font.SysFont("bahnschrift", 100).render(str(score), True, "white"), (WIDTH/2, 100))





def trouve_possition_spick_wall(nombre_spick, possition):
    pique = [x for x in range(18)] # il y a 18 piques possible sur les cotes
    
    for _ in range (nombre_spick):
        
        choix_pique = random.choice(pique)
        pique.pop(pique.index(choix_pique))
        possition.append(choix_pique)        
      

    return possition
      
      
      
def spick_mur(possition_spick):
    for i in range (len(possition_spick)):
        
        pygame.draw.line(SCREEN, WHITE, (0, 0+50*possition_spick[i]), (25, 25+50*possition_spick[i]))
        pygame.draw.line(SCREEN, WHITE, (0, 50+50*possition_spick[i]), (25, 25+50*possition_spick[i]))  
   
   
   
        pygame.draw.line(SCREEN, WHITE, (WIDTH, 0+50*possition_spick[i]), (WIDTH-25, 25+50*possition_spick[i]))
        pygame.draw.line(SCREEN, WHITE, (WIDTH, 50+50*possition_spick[i]), (WIDTH-25, 25+50*possition_spick[i]))     

    return possition_spick

     
     
def des_spick_mur(possition_spick):
    for i in range (len(possition_spick)):
        
        pygame.draw.line(SCREEN, BLACK, (0, 0+50*possition_spick[i]), (25, 25+50*possition_spick[i]))
        pygame.draw.line(SCREEN, BLACK, (0, 50+50*possition_spick[i]), (25, 25+50*possition_spick[i]))  
   
   
   
        pygame.draw.line(SCREEN, BLACK, (WIDTH, 0+50*possition_spick[i]), (WIDTH-25, 25+50*possition_spick[i]))
        pygame.draw.line(SCREEN, BLACK, (WIDTH, 50+50*possition_spick[i]), (WIDTH-25, 25+50*possition_spick[i]))

    return possition_spick





def test_si_defaite(birds, possition_spick):
    
    if birds.get_Vx() > 0 and birds.get_x() > WIDTH-35 or birds.get_Vx() < 0 and birds.get_x() < 35: # je le ( y ):
        
        for i in range (len(possition_spick)):
            
            # test si touche pointe des spick
            #if birds.get_y() - birds.get_rayon() <= 25+50*possition_spick[i]: # je test le ( x )
                #print('0.55')
                #if birds.get_Vx() > 0 and birds.get_x() > WHITE-100 or birds.get_Vx() < 0 and birds.get_x() < 100: # je le ( y )
                    #print('111')
                    #return "fin"
                
            # je test la base
            if birds.get_y()-birds.get_rayon() < 50*possition_spick[i] < birds.get_y()+birds.get_rayon() <= 50+50*possition_spick[i]:
                #print('222')
                return True
            
            elif 50*possition_spick[i] <= birds.get_y()-birds.get_rayon() <= 50+50*possition_spick[i] <= birds.get_y()+birds.get_rayon():
                #print('333')
                return True
            
            
    
    elif 25 >= birds.get_y()-birds.get_rayon():   # JE vrif si la birds touche le mur en haut
        print('444')
        return True
    
    elif HEIGHT <= birds.get_y()+birds.get_rayon():   # JE vrif si la birds touche le mur en bas
        print('555')
        return True
    
    
    return False



   
     
     
def affiche_oiseau(SCREEN, birds):
    position = (birds.get_x(),birds.get_y())
    pygame.draw.circle(SCREEN, RED, position, birds.get_rayon())
     
     
     
def des_affiche_oiseau(SCREEN, birds):
    position = (birds.get_x(),birds.get_y())
    pygame.draw.circle(SCREEN, BLACK, position, birds.get_rayon())
 

def saut(birds, possition, score):
    
    pos_y_a_atteindre = birds.get_y()-150
    while pos_y_a_atteindre <= birds.get_y():
 
        
        birds.set_x(birds.get_x() + birds.get_Vx())
        birds.set_y(birds.get_y() - birds.get_Vy() )
        #SCREEN.fill([0, 0, 0])
        affiche_oiseau(SCREEN, birds)
        possition, score = rebond_mur(birds, possition, score)
        
        defaire_or_continue = test_si_defaite(birds, possition)
        if defaire_or_continue:
            return True, score
            
        spick_plafond_and_sol_score(possition, score)
        pygame.display.update()
        
        des_affiche_oiseau(SCREEN, birds) # colorier l'ancienne possition de l'oiseau en noir pour pas devoir tout replire en noir
    
    
    
    accu = 0
    while accu != 20:  # c'est le temps que l'oiseau reste dans les aires apres le saut ( le mileiu de saut ) donc plus le chiffre et grand plus l'oiseau reste dans les aires longtemps
 
        birds.set_x(birds.get_x() + birds.get_Vx())
        #birds.set_y(birds.get_y() - 0.9 )
        #SCREEN.fill([0, 0, 0])
        affiche_oiseau(SCREEN, birds)
        possition, score = rebond_mur(birds, possition, score)
        
        defaire_or_continue = test_si_defaite(birds, possition)
        if defaire_or_continue:
            return True, score
        
        spick_plafond_and_sol_score(possition, score)
        pygame.display.update()  
        des_affiche_oiseau(SCREEN, birds)
        accu+=1
        
    return False, score
        
 
 
 
 
 
def relance_game(score):
    
    # affiche score
    pygame.draw.rect(SCREEN, RED, ((WIDTH/2)-175, (HEIGHT/2)-170, 350, 150), 2)    
    SCREEN.blit(pygame.font.SysFont("bahnschrift", 60).render("score", True, "white"), ((WIDTH/2)-80, (HEIGHT/2)-170))
    SCREEN.blit(pygame.font.SysFont("bahnschrift", 80).render(str(score), True, "white"), ((WIDTH/2)-10, (HEIGHT/2)-110))
    
    # affiche " rejouer "
    pygame.draw.rect(SCREEN, RED, ((WIDTH/2)-175, HEIGHT/2, 350, 150), 2)
    SCREEN.blit(pygame.font.SysFont("bahnschrift", 60).render("REJOUER", True, "white"), ((WIDTH/2)-120, (HEIGHT/2)+40))
    
    pygame.display.update()
 
    run = True
    while run:
        
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                
                 
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (WIDTH/2)-175 <= mouse[0] <= (WIDTH/2)+175 and HEIGHT/2 <= mouse[1] <= (HEIGHT/2)+150:
                    return ""
        
    return "quitte"
            
 
 
 
 
 
 
 
 
 
 
 
 
     
#    VITESSE : 

#x : 0.3
#y en chutte: 0.7
#y en saut: -0.9
#y en plane: 0

     

print('DEBUT !!!')

fin = ""
def main_oiseau():
    
    Vx = 1.1  # VITESSE X  # cette valeur doit etre constant ou augmente pour la difficulter
    Vy = 1.5  # VITESSE y
    
    possition = []
    score = 0
    birds = Oiseau(WIDTH/2, HEIGHT/2, Vx, Vy, 25)  # x, y, Vx, Vy, rayon

    run_debut = True
    run_game = False
    
    SCREEN.fill([0, 0, 0])
    affiche_oiseau(SCREEN, birds)
    spick_plafond_and_sol_score(possition, score)
    
    pygame.display.update()
    
    
    
    mouvement = 0 # 0 = monte; 1 = dessendre
    while run_debut:
        SCREEN.fill([0, 0, 0])

        if mouvement == 0:
            birds.set_y(birds.get_y() + 0.05)
            
            if birds.get_y() >= HEIGHT/2+20:
                mouvement = 1
            
        else:
            birds.set_y(birds.get_y() - 0.05)

            if birds.get_y() <= HEIGHT/2-20:
                mouvement = 0
                    
                  
        affiche_oiseau(SCREEN, birds)
        pygame.display.update()
        des_affiche_oiseau(SCREEN, birds)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_debut = False
                fin = "quitte"
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_game = True
                defaire_or_continue, score  = saut(birds, possition, 0) # 0 car pour le moment il y a un score de 0
                
        
        
        
        
        while run_game:
            
            
            spick_plafond_and_sol_score(possition, score)
            defaire_or_continue = deplace_birds(birds, possition)
            
            affiche_oiseau(SCREEN, birds)
            
                
            possition, score = rebond_mur(birds, possition, score)
                         
            pygame.display.update()
            des_affiche_oiseau(SCREEN, birds)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or defaire_or_continue:
                    run_game = False
                    run_debut = False
                    
                    if defaire_or_continue:
                        fin = ""
                        
                    else:
                        fin = "quitte"
                        
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    continuee, score = saut(birds, possition, score)
                
                    if continuee:
                        
                        run_game = False
                        run_debut = False
                        fin = ""
            
    return fin, score
            
            
while fin != "quitte":
    fin, score = main_oiseau()
    fin = relance_game(score)
    pygame.display.update()
    
    
print('okok c est la fin !!!! ')