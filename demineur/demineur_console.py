import random 
import copy

def créeation_grille(niveau):
    maps = []
    #for _ in range (niveau[0]):
    #    maps.append(i* niveau[1])  # il faut que ca me crée une liste qui contient que des 0 !
    #    print(len(maps))
    #    
    #for elem in maps:
    #    print(elem)
    
    
    
    
    
def mise_en_place_bombe(maps, niveau):
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
    zone_1_hauteur = random.randint(0, 2)
    zone_1_largeur = random.randint(0, 2)
    
    zone_2_hauteur = random.randint(0, 2)
    zone_2_largeur = random.randint(0, 2)
    
    if zone_1_hauteur == zone_2_hauteur:
        while zone_1_largeur == zone_2_largeur:
            zone_2_largeur = random.randint(0, 2)
    
    # maintenant j ai les deux zone !  
    
    # je cherche la moitie du nombre de bombe total :
    
    moitie_bombe = niveau[2]//2
    
    nombre_de_bombe_dans_zone_1 = random.randint(moitie_bombe-moitie_bombe//2, moitie_bombe+moitie_bombe//2)  # si il y a 10 bombes, nombre alea pour zone 1 de (3-8)  et le reste donc 10-rep =...  = nombre de bombe dans la zone 2 
    
    
    print(f"zone 1 : hauteur : {zone_1_hauteur} largeur : {zone_1_largeur}")
    print(f"zone 2 : hauteur : {zone_2_hauteur} largeur : {zone_2_largeur}")
    #print(moitie_bombe-moitie_bombe//2, moitie_bombe+moitie_bombe//2)
    print(f"le nombre dans la zone 1 : {nombre_de_bombe_dans_zone_1}")
    print(f"le nombre dans la zone 2 : {10-nombre_de_bombe_dans_zone_1}")
    nombre_de_bombe_dans_zone_2 = niveau[2] - nombre_de_bombe_dans_zone_1

    #print(len(maps))
    #print(len(maps[0]), maps[4])
    """maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]"""
    
        

           
    # maintenant avec les zones je dois crée un lien pour que la zone 2 c'est .. dans la maps
    zone_1_hauteur = zone_1_hauteur*len(maps)//3
    zone_1_largeur = zone_1_largeur*len(maps[0])//3
    
    zone_2_hauteur = zone_2_hauteur*len(maps)//3
    zone_2_largeur = zone_2_largeur*len(maps[0])//3    

        
   
    
    
    zone_1 = []
    
    for i in range (len(maps)//3):
        zone_1.append([maps[zone_1_hauteur+i][zone_1_largeur+lar] for lar in range (len(maps[0])//3)])
        
        
        
    zone_2 = []
    for i in range (len(maps)//3):
        zone_2.append([maps[zone_2_hauteur+i][zone_2_largeur+lar] for lar in range (len(maps[0])//3)])    
        

    
    # maintenant j ajoute aleatoirement des bombes dans les zones 1 et 2
    
    # "le nombre dans la zone 1 : {nombre_de_bombe_dans_zone_1}"
    # "le nombre dans la zone 2 : {10-nombre_de_bombe_dans_zone_1}"
    
    # zone 1
    for _ in range (nombre_de_bombe_dans_zone_1): # niveau [2] == le nombre de bombe
        bombe_y = random.randint(0, len(zone_1)-1)
        bombe_x = random.randint(0, len(zone_1[0])-1)
        while zone_1[bombe_y][bombe_x] == "B":
            bombe_y = random.randint(0, len(zone_1)-1)
            bombe_x = random.randint(0, len(zone_1[0])-1)    
        zone_1[bombe_y][bombe_x] = "B"
        
    
    for _ in range (nombre_de_bombe_dans_zone_2): # niveau [2] == le nombre de bombe
        bombe_y = random.randint(0, len(zone_2)-1)
        bombe_x = random.randint(0, len(zone_2[0])-1)
        while zone_2[bombe_y][bombe_x] == "B":
            bombe_y = random.randint(0, len(zone_2)-1)
            bombe_x = random.randint(0, len(zone_2[0])-1)    
        zone_2[bombe_y][bombe_x] = "B"    

    
    #maintenant que j ai modifie les zones pour avoir des bombes, je vais remplacer les emplecement de la map par les zones
    
 
    
    # ca fonctionne quand la maps contient des chiffres mais pas des strings ...
    
    # dans un premier temps je supprime les valeurs en trop dans la maps : 
    
    for i in range (2):
        for _ in range (4):
            maps[zone_1_hauteur+i].pop(zone_1_largeur)
    
    # dans un deuxieme temps j ajoute les valeurs de la zone 1 et zone 2 a la bonne place :
    
    for i in range (len(zone_1)):
        for lar in range (len(zone_1[0])):
            maps[zone_1_hauteur+i].insert(zone_1_largeur, zone_1[i][lar])    


    # dans un premier temps je supprime les valeurs en trop dans la maps : 
    
    for i in range (2):
        for _ in range (4):
            maps[zone_2_hauteur+i].pop(zone_2_largeur)   
    
    # dans un deuxieme temps j ajoute les valeurs de la zone 1 et zone 2 a la bonne place :
    
    for i in range (len(zone_2)):
        for lar in range (len(zone_1[0])):
            maps[zone_2_hauteur+i].insert(zone_2_largeur, zone_2[i][lar])   
        

    print("voila.. c'est fini... en 4h..")
    for elem in maps:
        print(elem)   
    
    

    maps_affiche_j = maps.copy()
    
    for i in range (2):
        for _ in range (4):
            maps_affiche_j[zone_1_hauteur+i].pop(zone_1_largeur)  

    for i in range (len(zone_1)):
        for lar in range (len(zone_1[0])):
            maps_affiche_j[zone_1_hauteur+i].insert(zone_1_largeur, 9)   


    for i in range (2):
        for _ in range (4):
            maps_affiche_j[zone_2_hauteur+i].pop(zone_2_largeur)  

    for i in range (len(zone_2)):
        for lar in range (len(zone_1[0])):
            maps_affiche_j[zone_2_hauteur+i].insert(zone_2_largeur, 9) 


    print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH : ')
    for elem in maps_affiche_j:
        print(elem)
    print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH : ')
    #xk = int(input('G'))

def affiche_maps_utilisateur(maps, zone_1_hauteur, zone_1_largeur, zone_2_hauteur, zone_2_largeur):
    maps_affiche_j = maps.copy()

    for i in range (2):
        for _ in range (4):
            maps[zone_2_hauteur+i].pop(zone_2_largeur)  

    for i in range (len(zone_2)):
        for lar in range (len(zone_1[0])):
            maps[zone_2_hauteur+i].insert(zone_2_largeur, zone_2[i][lar])   

    for i in range (2):
        for _ in range (4):
            maps[zone_2_hauteur+i].pop(zone_2_largeur)  

    for i in range (len(zone_2)):
        for lar in range (len(zone_1[0])):
            maps[zone_2_hauteur+i].insert(zone_2_largeur, zone_2[i][lar]) 


    
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
                   
                    
          

           
def main():
    créeation_grille(niveau)
    mise_en_place_bombe(maps, niveau)
    chiffre_a_cote_bombe(maps)             
 
 
maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
niveau = [10, 8, 10]   # les valeurs dans l'ordre 0, 1, 2 = hauteur, largeur, nombre_de_bombe
main()




#chiffre_a_cote_bombe(maps)

#créeation_grille(niveau)

a = random.sample((0, 10), 2)
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [a[i] for i in (4+y for y in range (3))]

c = [a[4+i] for i in range (3)]
print(b)
print(c)

for i in range(5):
    print(i)