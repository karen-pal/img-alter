from PIL import Image
import numpy as np
import random


def mirror_image(image, direction):
    img = np.array(image)
    lx, ly = img.shape
    #llamar modulo nim
    # img = nim_aux.mirror_image(img, lx, ly, progress, direction)
    for i in range(lx):
        for j in range(ly):
            if direction == "vertical":
                if j > ly//2:
                    img[i][j] = img[i][int((j-ly))//2]
            elif direction == "horizontal":
                if i > lx//2:
                    img[i][j] = img[int((i-lx))//2][j]
            elif direction == "diagonal_1":
                if i < j:
                    #img[i][j] = img[j % (int(lx*progress)%lx)][i %(int(ly*progress)%ly)]
                    img[i][j]=img[int(j)%lx][int(i)%ly]
            elif direction == "diagonal_2":
                if i > j:
                    img[i][j] = img[j % (int(lx)%lx)][i% (int(ly)%ly)]
                    #img[i][j]=img[int(j**progress)%lx][int(i**progress)%ly]

    return Image.fromarray(img)


def retouch(image):
    print("Entre")
    # rgb_im = img_file.convert('RGB')
    img = np.array(image)
    lx, ly = img.shape
    for i in range(lx):
        for j in range(ly):
            if i % 2 == 0 and j % 2 == 0:
                print(i,j,img[i][j])
                img[i][j] = (i + j) % 155

    return Image.fromarray(img)

"""
def drag(image, progress orientation):
    img = np.array(image)
    lx, ly = img.shape

    if orientation == "horizontal":
        to_drag_x = lx - random.randrange(lx//2)
        for i in range(lx):
            for j in range(ly):
                if i > to_drag_x:
                    img[i][j] = img[int(to_drag_x*progress)][j]
    elif orientation == "vertical":
        to_drag_y = ly - random.randrange(ly // 2)
        for i in range(lx):
            for j in range(ly):
                if j > to_drag_y:
                    img[i][j] = img[i][int(to_drag_y*progress)]
    return Image.fromarray(img)

"""
def pixelsorting(image):
    img = np.array(image)
    lx, ly = img.shape

    #select pixels to sort
    to_sort = []
    # to_sort[i][0] pixeles de img[i][rnmd]
    # to_sort[i][j] posicion en la imagen original

    for i in range(lx):
        if i%2==0 and i%4==0 and i%6==0 and i%8==0:
            x_pos = (i * random.randrange(lx)) % lx
            #x_pos = int(((i * random.randrange(lx)) % lx) ** progress*10)%lx
            # x_pos = int(((i * random.randrange(lx)) % lx) * (lx-progress))%lx
            to_sort.append([img[int(x_pos)], x_pos])
    #sort and modify the image
    for i in range(len(to_sort)):
        if i%2==0:
            pixel = -np.sort(-to_sort[i][0])
        else:
            pixel = np.sort(to_sort[i][0])

        x = to_sort[i][1]
        img[x] = pixel

    return Image.fromarray(img)
