from PIL import Image


if __name__ == "__main__":
    im = Image.open('Syngenta.bmp')
    #Converte imagem para o modo rgb
    im = im.convert('RGB')
    #Carrega os pixels dela
    pixels = im.load()
    count = 0
    
    width = im.size[0]
    height = im.size[1]
    green_pixel = (96,192,0)
    
    #Após um teste descobri que o pixel verde, em RGB, será dado por (96,192,0)
    for i in range(width):
        for j in range(height):
            if pixels[i,j] == green_pixel:
                count += 1

    print("Green pixel number: ",count)
    pass