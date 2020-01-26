from PIL import Image, ImageSequence
import numpy as np
im=Image.open("mia.gif")
frames=[]
for frame in ImageSequence.Iterator(im):
    frame_as_array=np.array(frame)
    for i in range(frame_as_array.shape[0]):
        frame_as_array[i][0]+=1
    frames.append(Image.fromarray(frame_as_array))
frames[0].save("miagif2.gif",save_all=True,append_images=frames[1:],duration=95,loop=0)
