#Nesta primeira tentativa eu pensei em tirar os pixels verdes da imagem, gerando uma imagem apenas com pixels pretos e brancos.
from PIL import Image


#utilizou-se como base o script do desafio anterior
if __name__ == "__main__":
    im = Image.open('Syngenta.bmp')
    im = im.convert('RGB')
    pixels = im.load()
    
    width = im.size[0]
    height = im.size[1]
    green_pixel = (96,192,0)
    black_pixel = (0,0,0)    

    for i in range(width):
        for j in range(height):
            if pixels[i,j] == green_pixel:
                pixels[i,j] = black_pixel

    im.save('Syngenta2_try1.bmp')
    pass