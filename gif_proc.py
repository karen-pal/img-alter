from gifalter import mirror_image, retouch, pixelsorting
from PIL import Image, ImageSequence
import click
import random
import sys


class Executor:
    def __init__(self, funcs, gif):
        list_of_frames = []
        self.funcs = funcs
        for frame in ImageSequence.Iterator(gif):
            list_of_frames.append(frame)
        self.frames=list_of_frames


    def execute(self, with_random):
        image_steps = []
        for i in range(len(self.frames)):
            for func in self.funcs:
                if with_random is True:
                    rnd_index = random.randrange(0, len(self.funcs))
                    func = self.funcs[rnd_index]
                new_frame = func(self.frames[i])
                image_steps.append(new_frame)
                #current_frame = new_frame
        return image_steps


def pixsort(image):
    return pixelsorting(image)


def mirror_diagonal_2(image):
    return mirror_image(image,"diagonal_2")


def mirror_diagonal_1(image):
    return mirror_image(image, "diagonal_1")


def mirror_horiz(image):
    return mirror_image(image,"horizontal")


def mirror_vert(image):
    return mirror_image(image,"vertical")


def my_retouch(image):
    return retouch(image)

funcs = [my_retouch]

@click.command()
@click.argument('in_file', required=1, type=click.Path(exists=True))
@click.option('--randomize', default=True, help='randomize the transformations order, True by default. Set to False for running in order')
@click.argument('out_file', type=click.Path())

def main(in_file, randomize, out_file):
    img = Image.open(click.format_filename(in_file))
    images_array = Executor(funcs, img).execute(randomize)
    print(len(images_array))
    print(type(images_array))
    tmp = images_array.copy()
    images_array.reverse()
    tmp += images_array

    tmp[0].save(click.format_filename(out_file), save_all=True, append_images=tmp[1:], duration=95, loop=0)

if __name__ == '__main__':
    main()
