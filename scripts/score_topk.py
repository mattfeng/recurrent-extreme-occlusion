#!/usr/bin/env python

import argparse
import string
import os

from collections import defaultdict

def parse_imagenet_map(fname):
    imagenet_to_pascal_map = defaultdict(lambda: 'WRONG')
    with open(fname) as f:
        for line in f:
            line = line.strip()
            pascal, imagenet = line.split(',')
            imagenet = imagenet.split(' ')
            for class_idx in imagenet:
                imagenet_to_pascal_map[class_idx] = pascal

    return imagenet_to_pascal_map

def get_class_from_filename(fname):
    fdir, fbase = os.path.split(fname)
    pascal_class = ''.join(filter(lambda x: x in string.ascii_lowercase, fbase.split('_')[2]))
    return pascal_class

def main(topk_file, imagenet_map, save_dir):
    if os.path.exists(save_dir):
        print(f'Save directory `{save_dir}` already exists, aborting...')
        exit(1)

    os.makedirs(save_dir)

    imagenet_to_pascal_map = parse_imagenet_map(imagenet_map)

    top1_correct = defaultdict(int)
    topk_correct = defaultdict(int)

    class_total = defaultdict(int)

    top1_incorrect_list = defaultdict(list)
    topk_incorrect_list = defaultdict(list)
    
    with open(topk_file) as f:
        for line in f:
            line = line.strip()
            fname, topk_str = line.split(',')

            # get the top K ImageNet categories, and the true class
            topk = topk_str.split(' ')
            pascal_class = get_class_from_filename(fname)

            class_total[pascal_class] += 1

            # if the first imagenet cls matches, add to top1
            if imagenet_to_pascal_map[topk[0]] == pascal_class:
                top1_correct[pascal_class] += 1
            else:
                top1_incorrect_list[pascal_class].append((fname, topk_str))
            
            # do the same check for the top k
            for imagenet_cls in topk:
                if imagenet_to_pascal_map[imagenet_cls] == pascal_class:
                    topk_correct[pascal_class] += 1
                    break
            else:
                topk_incorrect_list[pascal_class].append((fname, topk_str))

    # write out general stats
    general_stats_path = os.path.join(save_dir, 'results.dat')
    with open(general_stats_path, 'w') as f:
        for class_name, total_cnt in class_total.items():
            f.write('{},{},{},{}\n'.format(
                class_name,
                total_cnt,
                top1_correct[class_name],
                topk_correct[class_name]
                )
            )

    # write out incorrect classification lists
    for class_name, fname_list in top1_incorrect_list.items():
        incorrect_top1_path = os.path.join(save_dir, f'incorrect_top1_{class_name}.dat')
        print(f'Writing out incorrectly classified files to `{incorrect_top1_path}`.')
        with open(incorrect_top1_path, 'w') as f:
            for fname, topk_str in fname_list:
                f.write(f'{fname},{topk_str}\n')

    for class_name, fname_list in topk_incorrect_list.items():
        incorrect_topk_path = os.path.join(save_dir, f'incorrect_topk_{class_name}.dat')
        print(f'Writing out incorrectly classified files to `{incorrect_topk_path}`.')
        with open(incorrect_topk_path, 'w') as f:
            for fname, topk_str in fname_list:
                f.write(f'{fname},{topk_str}\n')




if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--imagenet_map',
        help = 'path of file containing PASCAL3D+ category map to ImageNet classes',
        type = str,
        default = '/home/ubuntu/6804_final_project/config/pascal_to_imagenet.txt'
        )

    parser.add_argument('topk_file',
        help = 'path of file containing the top K categories for each image',
        type = str
        )

    parser.add_argument('save_dir',
        help = 'directory to save all results to',
        type = str
        )

    args = parser.parse_args()

    main(
        topk_file = args.topk_file,
        imagenet_map = args.imagenet_map,
        save_dir = args.save_dir
        )


