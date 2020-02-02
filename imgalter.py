from PIL import Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import numpy as np
import random


#def get_text_to_draw(progress):
#    for i in range(frames*progress):


def text_insert(image,progress,frames):
    font_fname = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
    font_size = 50
    unicode_text =u"def text_insert(image,progress,frames): font_fname = /usr/share/fonts/truetype/freefont/FreeMono.ttf font_size = 200 font = ImageFont.truetype(font_fname, font_size, encoding=unic) img = np.array(image) lx,ly,color= img.shape image0 = Image.fromarray(img) draw = ImageDraw.Draw(image0) text_to_draw=unicode_text[int(frames*progress)%len(unicode_text)] draw.text((random.randrange(lx), random.randrange(ly)), text_to_draw, blue, font=font) print(frames*progress, text_to_draw) return image0"
    font = ImageFont.truetype(font_fname, font_size, encoding="unic")

    img = np.array(image)
    lx,ly,color= img.shape
    image0 = Image.fromarray(img)
    draw = ImageDraw.Draw(image0)
    start = random.randrange((int(frames*progress)%len(unicode_text))+1)
    text_to_draw=unicode_text[start:start*random.randrange(frames*progress+1)]
    draw.text((random.randrange(lx), random.randrange(ly)), text_to_draw, 'black', font=font)
    print(text_to_draw)
    return image0

def mirror_image(image, progress, direction):
    img = np.array(image)
    lx, ly, color = img.shape
    for i in range(lx):
        for j in range(ly):
            if direction == "vertical":
                if j > ly//2:
                    img[i][j] = img[int(j//2-(j-ly)*progress)%lx][i%ly]
                if i<lx//2:
                    img[i][j] =img[int((lx-i))%lx][j]
            elif direction == "horizontal":
                if i > lx//2:
                    img[i][j] = img[j%lx][int(i//2-(i-lx)*progress)%ly]
                else:
                    img[i][j] = img[(ly-i)%lx][j]
            elif direction == "diagonal_1":
                if i < j  and progress > (2/15):
                    img[i][j] = img[j % (int(lx*progress)%lx)][i %(int(ly*progress)%ly)]
                    #img[i][j]=img[int(j*progress)%lx][int(i*progress)%ly]
            elif direction == "diagonal_2":
                if i > j and progress > 0.7:
                    img[i][j] = img[j % (int(lx*progress)%lx)][i% (int(ly*progress)%ly)]
                    img[i][j]=img[int(j**progress)%lx][int(i**progress)%ly]

    return Image.fromarray(img)


def retouch(image, progress):
    # rgb_im = img_file.convert('RGB')
    img = np.array(image)
    lx, ly, color = img.shape
    for i in range(lx):
        for j in range(ly):
            if i % 2 == 0 and j % 2 == 0:
                img[i][j] = [int((i + j)**progress) % 155, i, j]

    return Image.fromarray(img)


def drag(image, progress, orientation):
    img = np.array(image)
    lx, ly, color = img.shape

    if orientation == "horizontal":
        to_drag_x = lx - random.randrange(lx//2)
        for i in range(lx):
            for j in range(ly):
                if abs(i-to_drag_x)>int(lx*.2) and i%2==0:
                    img[i][j] = img[int(to_drag_x*progress)][j]
    elif orientation == "vertical":
        to_drag_y = ly - random.randrange(ly // 2)
        for i in range(lx):
            for j in range(ly):
                if abs(j-to_drag_y)>int(ly*.2)  and j%2==0:
                    img[i][j] = img[i][int(to_drag_y*progress)]
    return Image.fromarray(img)


def pixelsorting(image, progress):
    img = np.array(image)
    lx, ly, color = img.shape

    #select pixels to sort
    to_sort = []
    # to_sort[i][0] pixeles de img[i][rnmd]
    # to_sort[i][j] posicion en la imagen original

    for i in range(lx):
        if i%2==0 and i%4==0 and i%6==0 and i%8==0:
            #x_pos = (i * random.randrange(lx)) % lx
            x_pos = int(((i * random.randrange(lx)) % lx) ** progress*10)%lx
            # x_pos = int(((i * random.randrange(lx)) % lx) * (lx-progress))%lx
            to_sort.append([img[int(x_pos*progress)], x_pos])
    #sort and modify the image
    for i in range(len(to_sort)):
        if i%2==0:
            pixel = -np.sort(-to_sort[i][0])
        else:
            pixel = np.sort(to_sort[i][0])

        x = to_sort[i][1]
        img[x] = pixel

    return Image.fromarray(img)
