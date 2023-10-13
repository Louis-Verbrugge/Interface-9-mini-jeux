import pygame
import time


BLACK = (0, 0, 0)




def start_transition(SCREEN, HEIGHT, WIDTH): 
    rec_x = 0
    while rec_x < WIDTH:
        pygame.draw.rect(SCREEN, BLACK, (0, 0, rec_x, HEIGHT))
        rec_x+=0.4
            
        pygame.display.update()
        
        
def end_transition(SCREEN, HEIGHT, WIDTH): 

    vitesse_x = (WIDTH/2)/50  #je cherche une vitesse en x et y pour que la page spon normalement donc je fait v = d/t
    vitesse_y = (HEIGHT/2)/50
    coord_x = 0
    coord_y = 0
    
    image_demineur = pygame.image.load("./image/image_main.jpg")
    
    while coord_x < WIDTH:
            
        
        

        
        

        
        affiche_image_2048 = pygame.transform.scale(image_demineur, (coord_x+vitesse_x, coord_y+vitesse_y))
        SCREEN.blit(affiche_image_2048, ((WIDTH/2)-(coord_x+vitesse_x)/2, (HEIGHT/2)-(coord_y+vitesse_y)/2))
        coord_x += vitesse_x
        coord_y += vitesse_y 
        
        pygame.display.update()
        time.sleep(0.01)
        
    time.sleep(1)

def main_credit(SCREEN, HEIGHT, WIDTH):
    
    
    #pygame.init()
    #SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    #pygame.display.set_caption(f"CREDIT")

    avec_aide = pygame.font.SysFont("bahnschrift", 70).render("CODE python :", True, "white")
    louis_verbreugge = pygame.font.SysFont("bahnschrift", 50).render("- Louis Verbrugge", True, "white")

    aide_design = pygame.font.SysFont("bahnschrift", 70).render("design + soutien:", True, "white")
    margot_urbaniak = pygame.font.SysFont("bahnschrift", 50).render("- Margot Urbaniak", True, "white")

    
        
    
    
    
    
    
    
    
    
    
    start_transition(SCREEN, HEIGHT, WIDTH)
    
    hauteur = HEIGHT
    run = True
    while run:


        
        SCREEN.fill(BLACK)
        code_python = avec_aide.get_rect(center=(WIDTH/2, HEIGHT+hauteur))
        louis_v = louis_verbreugge.get_rect(center=(WIDTH/2, HEIGHT+hauteur+200))
        design = aide_design.get_rect(center=(WIDTH/2, HEIGHT+hauteur+500))
        margot_u = margot_urbaniak.get_rect(center=(WIDTH/2, HEIGHT+hauteur+700))


        SCREEN.blit(avec_aide, code_python) # CODE : python :
        SCREEN.blit(louis_verbreugge, louis_v) # louis verrbugge
        SCREEN.blit(aide_design, design)
        SCREEN.blit(margot_urbaniak, margot_u)

        pygame.display.update()
        hauteur-=0.5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if HEIGHT+hauteur+700 < -100: # les crédits sont fini
            run = False
            
    end_transition(SCREEN, HEIGHT, WIDTH)