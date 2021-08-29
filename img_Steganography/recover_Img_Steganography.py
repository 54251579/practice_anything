from PIL import Image
import math
import sys

def recover_msg(file):
    img = Image.open(file)
    
    width, height = img.size

    bits = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    color_str = ('RED', 'GREEN', 'BLUE')
    try:
        for idx, bit_bin in enumerate(bits):
            for color in range(3):
                    img_save = img.copy()
                    for x in range(width):
                        for y in range(height):
                            pixel_color = img.getpixel((x, y))
                            r, g, b = pixel_color

                            if pixel_color[color]&bit_bin != 0:
                                r, g, b = (0xFF,0xFF,0xFF)
                            else:
                                r,g,b = (0,0,0)
                                
                            img_save.putpixel((x,y), (r,g,b))
                    img_save.save(path+'recover/'+color_str[color]+str(idx)+".png", 'png')
    except KeyboardInterrupt:
        img_save.save(path+color_str[color]+str(idx)+".png", 'png')

path = #path
file = path+'after.png'
recover_msg(file)
print('end')
