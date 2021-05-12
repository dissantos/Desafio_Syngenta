#Na segunda tentativa, tentei trocar os pixels pretos por branco e vice versa
from PIL import Image


#utilizou-se como base o script do desafio anterior
if __name__ == "__main__":
    im = Image.open('Syngenta.bmp')
    im = im.convert('RGB')
    pixels = im.load()
    
    width = im.size[0]
    height = im.size[1]
    
    green_pixel = (96,192,0)
    white_pixel = (255,255,255)
    black_pixel = (0,0,0)    

    for i in range(width):
        for j in range(height):
            if pixels[i,j] == black_pixel:
                pixels[i,j] = white_pixel
    
    im.save('Syngenta2_try2_white.bmp')
    
    im = Image.open('Syngenta.bmp')
    im = im.convert('RGB')
    pixels = im.load()
                
    for i in range(width):
        for j in range(height):
            if pixels[i,j] == white_pixel:
                pixels[i,j] = black_pixel

    im.save('Syngenta2_try2_black.bmp')

    
    pass