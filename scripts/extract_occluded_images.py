#!/usr/bin/env python

import argparse
import h5py
import os
import glob
import numpy as np

from PIL import Image
from tqdm import tqdm

def main(difficulty, output_path, data_path):
    if os.path.exists(output_path):
        print(f'`{output_path}` already exists, and cannot be used to save output. Aborting.')
        exit(1)

    print(f'Creating output directory `{output_path}`...')
    os.makedirs(output_path)

    categories = [
        'aeroplane',
        'bicycle',
        'bus',
        'car',
        'motorbike',
        'train'
        ]

    for category in categories:
        print(f'Extracting occluded images for category `{category}`')
        test_images_path = os.path.join(
            data_path,
            f'{category}{difficulty}'
            )
        test_images = sorted(glob.glob(f'{test_images_path}/*.mat'))

        for idx, test_image_path in enumerate(tqdm(test_images)):
            # get the output file name
            img_dir, img_base = os.path.split(test_image_path)
            img_base_root, _ = os.path.splitext(img_base)

            # read in the MATLAB file, and get the image
            img_h5 = h5py.File(test_image_path, 'r')
            img = np.transpose(img_h5['record/img'].value, (2, 1, 0))

            # save the image using PIL
            img_pil = Image.fromarray(img)
            output_img_path = os.path.join(
                output_path,
                f'occluded_test_{category}{difficulty}_{img_base_root}.png'
                )
            img_pil.save(output_img_path)

    print('Done!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('difficulty',
        help = 'difficulty of occlusion',
        choices = [
            'ONE',
            'TWO',
            'THREE',
            'FOUR',
            'FIVE',
            'SIX',
            'SEVEN',
            'EIGHT',
            'NINE'
            ],
        type = str
        )

    parser.add_argument('output_path',
        help = 'path to directory to save the extracted occluded images to',
        type = str
        )

    parser.add_argument('--data_path',
        help = 'path to base directory of vehicle occlusion dataset',
        type = str,
        default = '/home/ubuntu/datasets/occ'
        )

    args = parser.parse_args()

    main(
        difficulty = args.difficulty,
        output_path = args.output_path,
        data_path = args.data_path
        )
