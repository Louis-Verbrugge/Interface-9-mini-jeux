"""from PIL import Image
import sys
import time


WIDTH, HEIGHT = 1300, 1000  #  1600, 900 fixe  ; 1600, 1200


image = Image.open("main.jpg")
frames = []
run = True


largeur_image = 50
hauteur_image = 50

for i in range (2):

                
    for y in range (hauteur_image):
        for x in range (largeur_image):
            
            r, v, b = image.getpixel((x, y))
            
            im = Image.new('RGB', (50, 50), (r, v, b))             
                            
            image.putpixel((x, y), (r-20, v-20, b-20))
            
            frames.append(im)

    print('okok')
                
frames[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=frames[1:], optimize=False, duration=40, loop=0)"""



from PIL import Image
import imageio

# Chargement de l'image
image = Image.open("chemin/vers/image.jpg")
# Conversion en niveaux de gris               23.1.2
image = image.convert("L")

# Création de la liste d'images pour le GIF
images = []
# Ajout de l'image originale à la liste
images.append(image)

# Boucle pour créer les images assombries
for i in range(255):
    # Assombrissement de l'image
    image = Image.eval(image, lambda x: x - 1)
    # Ajout de l'image assombrie à la liste
    images.append(image)

# Création du GIF à partir de la liste d'images
imageio.mimsave("chemin/vers/gif.gif", images, duration=0.05)   
                

