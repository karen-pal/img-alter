from PIL import Image
import numpy as np
import random


def load_image(img_file):
    img = np.array(Image.open(img_file))
    return img


def save_image(nparray, filename):
    im = Image.fromarray(nparray)
    im.save(filename)


def mask_image(img_file, shape):
    img = load_image(img_file)
    lx, ly, color = img.shape

    for i in range(lx):
        for j in range(ly):
            if shape == "full":
                img[i][j] = [i % 256, j % 256, (i + j) % 256]
            elif shape == "circle":
                if (i - lx/2)**2 + (j - ly/2)**2 > lx*ly/4:
                    img[i][j] = [i % 256, j % 256, (i + j) % 256]
            elif shape == "rectangle":
                if i < lx*.2 or i > lx - lx*.2 or j < ly*.2 or j > ly - ly*.2:
                    img[i][j] = [i % 256, j % 256, (i + j) % 256]

    save_image(img, "withmask_"+shape+img_file)


def mirror_image(img_file, direction):
    img = load_image(img_file)
    lx, ly, color = img.shape

    for i in range(lx):
        for j in range(ly):
            if direction == "vertical":
                if j > ly//2:
                    img[i][j] = img[i][j-ly//2]
            elif direction == "horizontal":
                if i > lx//2:
                    img[i][j] = img[i-lx//2][j]
            elif direction == "diagonal_1":
                if i < j:
                    img[i][j] = img[j % lx][i % ly]
            elif direction == "diagonal_2":
                if i > j:
                    img[i][j] = img[j % lx][i % ly]

    save_image(img, "mirror_"+direction+img_file)


def retouch(img_file):
    img = load_image(img_file)
    lx, ly, color = img.shape

    for i in range(lx):
        for j in range(ly):
            if i % 2 == 0 and j % 2 == 0:
                img[i][j] = [(i + j) % 155, i, j]

    save_image(img, "retouch_"+img_file)


def drag(img_file, orientation):
    img = load_image(img_file)
    lx, ly, color = img.shape

    if orientation == "horizontal":
        to_drag_x = lx - random.randrange(lx//2)
        for i in range(lx):
            for j in range(ly):
                if i > to_drag_x:
                    img[i][j] = img[to_drag_x][j]
    elif orientation == "vertical":
        to_drag_y = ly - random.randrange(ly // 2)
        for i in range(lx):
            for j in range(ly):
                if j > to_drag_y:
                    img[i][j] = img[i][to_drag_y]

    save_image(img, "drag_"+orientation+img_file)


# mirror_image("abel.jpg", "diagonal_1")
# mirror_image("abel.jpg", "diagonal_2")
# mask_image("angery.jpg", "full")
# mask_image("angery.jpg", "circle")
# mask_image("angery.jpg", "rectangle")
# mirror_image("abel.jpg", "horizontal")
# mirror_image("abel.jpg", "vertical")
# retouch("angery.jpg")
drag("abel.jpg", "horizontal")
drag("abel.jpg", "vertical")
