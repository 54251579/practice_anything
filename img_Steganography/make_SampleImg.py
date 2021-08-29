from PIL import Image
import math

def make_msg(file):
    img = Image.open(file)
    select_bit = int(input('select bit to modulate : '))
    select_color = int(input('select color to modulate\n1: Red\t2: Green\t3: Blue\tselect : '))
    width, height = img.size

    bits = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    color_str = ('RED', 'GREEN', 'BLUE')

    img_save = img.copy()
    
    for x in range(width):
        for y in range(height):

            pixel_color = img.getpixel((x, y))
            r, g, b = pixel_color

            if select_color == 1:
                r = r&(~bits[select_bit])
            elif select_color == 2:
                g = g&(~bits[select_bit])
            elif select_color == 3:
                b = b&(~bits[select_bit])
            img_save.putpixel((x,y), (r,g,b))

    img_save.save(path+color_str[select_color-1]+str(select_bit)+".png", 'png')

path = # path
file = path+'Sample.png'
make_msg(file)
print('end')
