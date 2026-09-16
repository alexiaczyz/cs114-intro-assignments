#!/usr/bin/env python
# coding: utf-8

# In[30]:


import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from typing import Callable 
from typing import Sequence 

## Write the functions here
def clamp(array:npt.NDArray)->npt.NDArray:
    """
    adapting the clamp from class takes in array and clamps between a min and max 
    """
    return np.where(array<0, 0, np.where(array>1,1,array))

def brighten(img:npt.NDArray)->npt.NDArray:
    """
    brightens img 
    """
    array =img+0.25
    e=clamp(array)
    return e

def darken(img:npt.NDArray)->npt.NDArray:
    """
    darkens img
    """
    array =img-0.25
    e=clamp(array)
    return e

def mirror(img:npt.NDArray)->npt.NDArray:
    """
    horizontally mirrors img
    """
    return img[:,::-1]

def mirror_vertical(img:npt.NDArray)->npt.NDArray:
    """
    vertically mirrors img
    """
    return img[::-1,:]

def gamma_up(img:npt.NDArray)->npt.NDArray:
    """
    every value is increased in img
    """
    array=img*1.25
    r=clamp(array)
    return r

def gamma_down(img:npt.NDArray)->npt.NDArray:
    """
    every value is decreaced in img
    """
    array=img*0.8
    t=clamp(array)
    return t
def normalize(img:npt.NDArray)->npt.NDArray:
    """
    normalizes img to have values 0 to 1 
    """
    minn=img.min()
    maxx= img.max()
    assert maxx>minn
    
    shift=img-minn
    return shift/shift.max()

def image_edit(output_filename:str,input_filename:str,edits:Sequence[Callable])->npt.NDArray:
    """
    takes an input_filename of an image and applies edits to it. then gives output_filename
    """
    img= plt.imread(input_filename)
    gray=img[:,:,:3].mean(axis=-1)
    for edit in edits:
        gray= edit(gray)
        
    plt.imsave(output_filename, gray, cmap="gray")
    return gray


## Here are some tests. Add your own tests as well; don't just count on ours!
assert np.all(
    np.abs(image_edit("tmp.png", "digit.png", [brighten]) - plt.imread("digit-brighten.png")[:, :, :3].mean(axis=-1)) < 0.01
), "digit.png brightened"
assert np.all(
    np.abs(image_edit("tmp.png", "gregor.png", [
        mirror, mirror_vertical, gamma_up, normalize, gamma_down, normalize,
        brighten, normalize, darken, normalize, gamma_up, normalize,
        gamma_down, normalize, brighten, normalize, darken, normalize
    ]) - plt.imread("gregor-botched.png")[:, :, :3].mean(axis=-1)) < 0.01
), "gregor.png botched"

SAMPLE_INPUT = np.array([[0.0, 0.2], [0.9, 1.0]])
SAMPLE_INPUT_2 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

assert np.all(
    np.abs(mirror(SAMPLE_INPUT.copy()) - np.array([[0.2, 0.0], [1.0, 0.9]])) < 0.001
), "Sample mirrored"
assert np.all(
    np.abs(mirror(SAMPLE_INPUT_2.copy()) - np.array([[0.3, 0.2, 0.1], [0.6, 0.5, 0.4]])) < 0.001
), "Sample 2 mirrored"
assert np.all(
    np.abs(mirror_vertical(SAMPLE_INPUT.copy()) - np.array([[0.9, 1.0], [0.0, 0.2]])) < 0.001
), "Sample mirrored vertically"
assert np.all(
    np.abs(mirror_vertical(SAMPLE_INPUT_2.copy()) - np.array([[0.4, 0.5, 0.6], [0.1, 0.2, 0.3]])) < 0.001
), "Sample 2 mirrored vertically"
assert np.all(
    np.abs(brighten(SAMPLE_INPUT.copy()) - np.array([[0.25, 0.45], [1.0, 1.0]])) < 0.001
), "Sample brightened"
assert np.all(
    np.abs(brighten(SAMPLE_INPUT_2.copy()) - np.array([[0.35, 0.45, 0.55], [0.65, 0.75, 0.85]])) < 0.001
), "Sample 2 brightened"
assert np.all(
    np.abs(darken(SAMPLE_INPUT.copy()) - np.array([[0.0, 0.0], [0.65, 0.75]])) < 0.001
), "Sample darkened"
assert np.all(
    np.abs(darken(SAMPLE_INPUT_2.copy()) - np.array([[0.0, 0.0, 0.05], [0.15, 0.25, 0.35]])) < 0.001
), "Sample 2 darkened"
assert np.all(
    np.abs(gamma_up(SAMPLE_INPUT.copy()) - np.array([[0.0, 0.25], [1.0, 1.0]])) < 0.001
), "Sample gamma up"
assert np.all(
    np.abs(gamma_up(SAMPLE_INPUT_2.copy()) - np.array([[0.125, 0.25, 0.375], [0.5, 0.625, 0.75]])) < 0.001
), "Sample 2 gamma up"
assert np.all(
    np.abs(gamma_down(SAMPLE_INPUT.copy()) - np.array([[0.0, 0.16], [0.72, 0.8]])) < 0.001
), "Sample gamma down"
assert np.all(
    np.abs(gamma_down(SAMPLE_INPUT_2.copy()) - np.array([[0.08, 0.16, 0.24], [0.32, 0.40, 0.48]])) < 0.001
), "Sample 2 gamma down"
assert np.all(
    np.abs(normalize(SAMPLE_INPUT.copy()) - np.array([[0.0, 0.2], [0.9, 1.0]])) < 0.001
), "Sample normalized"
assert np.all(
    np.abs(normalize(SAMPLE_INPUT_2.copy()) - np.array([[0.0, 0.2, 0.4], [0.6, 0.8, 1.0]])) < 0.001
), "Sample 2 normalized"


SAMPLE_INPUT_3 = np.array([[1.0, 0.5], [0.4, 0.5]])
SAMPLE_INPUT_4 = np.array([[0.3, 0.4], [0.4, 0.5]])

assert np.all(
    np.abs(mirror(SAMPLE_INPUT_3.copy()) - np.array([[0.5, 1.0], [0.5, 0.4]])) < 0.001
)
assert np.all(
    np.abs(mirror(SAMPLE_INPUT_4.copy()) - np.array([[0.4, 0.3], [0.5, 0.4]])) < 0.001
)
assert np.all(
    np.abs(mirror_vertical(SAMPLE_INPUT_3.copy()) - np.array([[0.4, 0.5], [1.0, 0.5]])) < 0.001
)
assert np.all(
    np.abs(mirror_vertical(SAMPLE_INPUT_4.copy()) - np.array([[0.4, 0.5], [0.3, 0.4]])) < 0.001
)
assert np.all(
    np.abs(brighten(SAMPLE_INPUT_3.copy()) - np.array([[1.0, 0.75], [0.65, 0.75]])) < 0.001
)
assert np.all(
    np.abs(brighten(SAMPLE_INPUT_4.copy()) - np.array([[0.55, 0.65], [0.65, 0.75]])) < 0.001
)
assert np.all(
    np.abs(darken(SAMPLE_INPUT_3.copy()) - np.array([[0.75, 0.25], [0.15, 0.25]])) < 0.001
)
assert np.all(
    np.abs(darken(SAMPLE_INPUT_4.copy()) - np.array([[0.05, 0.15], [0.15, 0.25]])) < 0.001
)
assert np.all(
    np.abs(gamma_up(SAMPLE_INPUT_3.copy()) - np.array([[1.0, 0.625], [0.5, 0.625]])) < 0.001
)
assert np.all(
    np.abs(gamma_up(SAMPLE_INPUT_4.copy()) - np.array([[0.375, 0.5], [0.5, 0.625]])) < 0.001
)
assert np.all(
    np.abs(gamma_down(SAMPLE_INPUT_3.copy()) - np.array([[0.8, 0.4], [0.32, 0.4]])) < 0.001
)
assert np.all(
    np.abs(gamma_down(SAMPLE_INPUT_4.copy()) - np.array([[0.24, 0.32], [0.32, 0.4]])) < 0.001
)
assert np.all(
    np.abs(
        normalize(SAMPLE_INPUT_3.copy())- np.array([[1.0, 0.1666667], [0.0, 0.1666667]])) < 0.001
)
assert np.all(
    np.abs(normalize(SAMPLE_INPUT_4.copy())- np.array([[0.0, 0.5], [0.5, 1.0]])) < 0.001
)
assert np.all(
    np.abs(normalize(SAMPLE_INPUT_4.copy())- np.array([[0.0, 0.5], [0.5, 1.0]])) < 0.001
)
assert np.all(
    np.abs(clamp(SAMPLE_INPUT))- np.array([[0.0, 0.2], [0.9, 1.0]])) < 0.001
#print(clamp(SAMPLE_INPUT_3))
assert np.all(
    np.abs(clamp(SAMPLE_INPUT_3)- np.array([[1.0, 0.5], [0.4, 0.5]])) < 0.001
)


#print("doge-mirror_vertical.png", "doge-of-venice.png", [mirror_vertical])


assert np.all(
    np.abs(image_edit("doge-mirror_vertical.png", "doge-of-venice.png", [mirror_vertical]) - plt.imread("doge-mirror_vertical.png")[:, :, :3].mean(axis=-1)) < 1.01
), "test"

assert np.all(
    np.abs(image_edit("doge-gamma_up.png", "doge-of-venice.png", [mirror_vertical]) - plt.imread("doge-gamma_up.png")[:, :, :3].mean(axis=-1)) < 1.01
), "test 2"


# In[ ]:




