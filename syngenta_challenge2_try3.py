#Na terceira tentativa tentei preencher os pixels entre dois pixels verdes com verde, e vendo se sairia alguam outra mensagem. Eu fiz isso da esquerda para direita e de cima para baixo
from PIL import Image


if __name__ == "__main__":
    im = Image.open('Syngenta.bmp')
    im = im.convert('RGB')
    pixels = im.load()
    
    width = im.size[0]
    height = im.size[1]
    green_pixel = (96,192,0)

    draw = 0

    for i in range(width): 
        for j in range(height):
            if pixels[i,j] == green_pixel:
                draw = 1 - draw
            if draw == 1:
                pixels[i,j] = green_pixel


    im.save('Syngenta2_try3_height.bmp')
    
    im = Image.open('Syngenta.bmp')
    im = im.convert('RGB')
    pixels = im.load()
    
    draw = 0

    for i in range(height): 
        for j in range(width):
            if pixels[j,i] == green_pixel:
                draw = 1 - draw
            if draw == 1:
                pixels[j,i] = green_pixel


    im.save('Syngenta2_try3_width.bmp')
    pass