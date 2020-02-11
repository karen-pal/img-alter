from imgalter import mirror_image, drag, retouch, pixelsorting, text_insert
from PIL import Image
import click
import random
import sys


class Executor:
    def __init__(self, funcs, image, frames):
        self.frames = frames
        self.funcs = funcs
        self.image = image

    def execute(self, with_random):
        current_frame = self.image
        image_steps = []
        for func in self.funcs:
            for frame in range(self.frames):
                if with_random is True:
                    rnd_index = random.randrange(0, len(self.funcs))
                    func = self.funcs[rnd_index]
                progress = frame/self.frames
                new_frame = func(current_frame, progress, self.frames)
                image_steps.append(new_frame)
                current_frame = new_frame
        return image_steps


def pixsort(image,progress,frames):
    return pixelsorting(image,progress)


def mirror_diagonal_2(image, progress, frames):
    return mirror_image(image, progress, "diagonal_2")


def mirror_diagonal_1(image, progress, frames):
    return mirror_image(image, progress, "diagonal_1")


def mirror_horiz(image, progress, frames):
    return mirror_image(image, progress, "horizontal")


def mirror_vert(image, progress, frames):
    return mirror_image(image, progress, "vertical")


def my_retouch(image, progress, frames):
    return retouch(image, progress)


def drag_vert(image, progress, frames):
    return drag(image, progress, "vertical")


def drag_horiz(image, progress, frames):
    return drag(image, progress, "horizontal")

def write_text(image,progress,frames):
    return text_insert(image, progress, frames)

funcs = [write_text,write_text,drag_horiz]

@click.command()
@click.argument('in_file', required=1, type=click.Path(exists=True))
@click.option('--randomize', default=True, help='randomize the transformations order, True by default. Set to False for running in order')
@click.argument('out_file', type=click.Path())

def main(in_file, randomize, out_file):
    img = Image.open(click.format_filename(in_file))
    im = img.convert('RGB')
    frames = 35
    images_array = Executor(funcs, im, frames).execute(randomize)
    tmp = images_array.copy()
    images_array.reverse()
    tmp += images_array

    tmp[0].save(click.format_filename(out_file), save_all=True, append_images=tmp[0:], duration=95, loop=0)

if __name__ == '__main__':
    main()
