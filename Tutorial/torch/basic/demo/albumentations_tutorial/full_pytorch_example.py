# -*- coding:utf-8 -*-

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch import optim, true_divide
from torch.utils.data import DataLoader
from tqdm import tqdm
import torch.nn.functional as F

import torch
import numpy as np
import cv2
from PIL import Image
import torch.nn as nn
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torch.utils.data import Dataset
import os


class ImageFolder(Dataset):

    def __init__(self, root_dir, transform=None):
        super(ImageFolder, self).__init__()
        self.data = []
        self.transform = transform
        self.class_names = os.listdir(root_dir)
        for index, name in enumerate(self.class_names):
            files = os.listdir(os.path.join(root_dir, name))
            self.data += list(zip(files, [index] * len(files)))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img_file, label = self.data[index]
        root_and_dir = os.path.join(self.root_dir, self.class_names[label])
        image = np.array(Image.open(os.path.join(root_and_dir, img_file)))

        if self.transform is not None:
            augmentations = self.transform(image=image)
            image = augmentations['image']
        return image, label


transform = A.Compose([
    A.resize(width=1920, height=1920),
    A.RandomCrop(width=1280, height=1280),
    A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),
    A.VerticalFlip(p=0.5),
    A.HorizontalFlip(p=0.5),
    A.RGBShift(r_shift_limit=25, g_shift_limit=35, b_shift_limit=25),
    A.OneOf([
        A.Blur(blur_limit=3, p=0.5),
        A.ColorJitter(p=0.5)], p=0.1),
    A.Normalize(mean=[0, 0, 0], std=[1, 1, 1], max_pixel_value=255),
    ToTensorV2()
])

dataset = ImageFolder(root_dir="cat_dogs", transform=transform)
for x,y in dataset:
    print(x.shape)