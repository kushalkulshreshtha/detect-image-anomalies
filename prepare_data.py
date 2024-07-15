#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from multiprocessing import Pool, cpu_count
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import cv2
import glob
from itertools import chain
import random


# In[3]:


num_images = 2000


# In[4]:


def add_crack(image_path, save_path, thickness=2):
    # Load the image
    image = Image.open(image_path).convert("RGB")
    open_cv_image = np.array(image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    # Draw a crack line
    height, width, _ = open_cv_image.shape
    start_point = (np.random.randint(0, width), np.random.randint(0, height))
    end_point = (np.random.randint(0, width), np.random.randint(0, height))
    color = (1, 1, 1)  # white crack
    cv2.line(open_cv_image, start_point, end_point, color, thickness)

    # Convert back to PIL format and save
    cracked_image = Image.fromarray(open_cv_image[:, :, ::-1])
    cracked_image.save(save_path)

def add_fade(image_path, save_path):
    image = Image.open(image_path).convert("RGB")
    faded_image = image.filter(ImageFilter.GaussianBlur(radius=3))
    faded_image.save(save_path)

def add_smudge(image_path, save_path):
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    for _ in range(2):
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        draw.ellipse((x-10, y-10, x+10, y+10), fill="grey", outline="grey")
    image.save(save_path)

def process_image(image_path):
    base_filename = os.path.basename(image_path).split('.')[0]

    choice = np.random.randint(1,4)
    if choice == 1:
        add_crack(image_path, f'flawed_images/cracked_{base_filename}_{random.randint(0, 10000)}.jpg')
    
    elif choice == 2:
        add_fade(image_path, f'flawed_images/faded_{base_filename}_{random.randint(0, 10000)}.jpg')
    
    else:
        add_smudge(image_path, f'flawed_images/smudged_{base_filename}_{random.randint(0, 10000)}.jpg')


# In[ ]:


if __name__ == "__main__":

    files = []
    folders = glob.glob('Logo-2K+/*/*/*')
    for folder in folders:
        path = os.path.join(os.getcwd(), folder)
        image_list = glob.glob(path + "\\*.jpg")
        files.append(image_list)
    
    images = list(chain(*files))
    image_paths = np.random.choice(images, size = num_images, replace = False)
    print(f'read {len(images)} images; saving {len(image_paths)} images')
    
    if not os.path.exists('original_images'):
        os.makedirs('original_images')
        print('created folder named original images')
    
    for path in image_paths:
        image = Image.open(path).convert("RGB")
        base_filename = os.path.basename(path).split('.')[0] + str(random.randint(0, 1000))
        image.save(f'original_images/train_{base_filename}.jpg')
    print('saved images')
    
    # Create output directory if it doesn't exist
    if not os.path.exists('flawed_images'):
        os.makedirs('flawed_images')

    for path in image_paths:
        process_image(path)
    print('created flawed images')

