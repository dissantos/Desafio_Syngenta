#Na ultima tentativa que pensei, tentei utilizar de técnicas de estegonografia LSB. Essa técnica consiste em esconder a mensagem nos bits menos significativos de cada byte (pixel) da imagem
#Ao juntarmos 8 desses bit menos significativos montamos um byte que deverá representar uma letra da mensagem
from PIL import Image


if __name__ == "__main__":
    im = Image.open('Syngenta.bmp')
    count = 0
    byte_array = []
    byte = []
    #percorre pixel a pixel da imagem e monta-se os bytes com os bits menos significativos
    for pixel in im.getdata():
        byte.append(pixel%2)
        count+=1
        if count % 8 == 0:
            byte_array.append(byte)
            byte = []

    pixel_array = []
    #transforma o array de bits em um byte
    for byte in byte_array:
        out = 0
        for bit in byte:
            out = (out << 1) | bit
        pixel_array.append(out)

    message = []
    for pixel in pixel_array:
        if pixel != 0:
            if (chr(pixel) >= 'A' and chr(pixel) <= 'Z') or (chr(pixel) >= 'a' and chr(pixel) <= 'z'):
                message.append(chr(pixel))
    
    print(message)
    pass