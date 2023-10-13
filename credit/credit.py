import pygame
import sys

WIDTH, HEIGHT = 1600, 900
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"CREDIT")

avec_aide = pygame.font.SysFont("bahnschrift", 70).render("CODE python :", True, "white")
louis_verbreugge = pygame.font.SysFont("bahnschrift", 50).render("- Louis Verbrugge", True, "white")

aide_design = pygame.font.SysFont("bahnschrift", 70).render("design + soutien:", True, "white")
margot_urbaniak = pygame.font.SysFont("bahnschrift", 50).render("- Margot Urbaniak", True, "white")



hauteur = HEIGHT

run = True
while run:


    
    SCREEN.fill((0, 0, 0))
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