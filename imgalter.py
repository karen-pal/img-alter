from PIL import Image
import numpy as np
import random


def mirror_image(img, progress, direction):
    img = np.array(img)
    lx, ly, color = img.shape

    for i in range(lx):
        for j in range(ly):
            if direction == "vertical":
                if j > ly//2:
                    img[i][j] = img[i][int((j-ly)*progress)//2]
            elif direction == "horizontal":
                if i > lx//2:
                    img[i][j] = img[int((i-lx)*progress)//2][j]
            elif direction == "diagonal_1":
                if i < j and progress > 0:
                    img[i][j] = img[j % (int(lx*progress)%lx)][i %(int(ly*progress)%ly)]
            elif direction == "diagonal_2":
                if i > j and progress > 0:
                    img[i][j] = img[j % (int(lx*progress)%lx)][i% (int(ly*progress)%ly)]

    return Image.fromarray(img)


def retouch(img_file, progress):
    img = np.array(img_file)
    lx, ly, color = img.shape

    for i in range(lx):
        for j in range(ly):
            if i % 2 == 0 and j % 2 == 0:
                img[i][j] = [int((i + j)*progress) % 155, i, j]

    return Image.fromarray(img)


def drag(img, progress, orientation):
    img = np.array(img)
    lx, ly, color = img.shape

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


# definir que intervalos de pixeles modificar
# modificarlos
def pixelsorting(img, progress):
    img = np.array(img)
    lx, ly, color = img.shape

    #select pixels to sort
    to_sort = []
    for i in range(lx):
        if i%2==0 and i%4==0:
            x_pos = (i * random.randrange(lx)) % lx
            to_sort.append([img[int(x_pos*progress)], x_pos])
    #sort and modify the image
    for i in range(len(to_sort)):
        pixel = np.sort(to_sort[i][0])
        x = to_sort[i][1]
        img[x] = pixel

    return Image.fromarray(img)
