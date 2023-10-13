


from PIL import Image
import imageio # pip install imageio


screen = Image.open("image/image_main.jpg")

images = []
images.append(screen)

# Boucle po25ur créer les images assombries
for i in range(128):   #128 car je diminue de x la couleur r; b; v et comme la couleur max est banc 255 
    
    screen = Image.eval(screen, lambda x: x - 2)  # Assombrissement de l'image
    images.append(screen)
    


imageio.mimsave("./image/image_main_snake.gif", images, duration=0.05)

