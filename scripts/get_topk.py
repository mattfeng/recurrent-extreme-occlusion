#!/usr/bin/env python

'''
Description:
Evaluates the output of a CORnet model for the Vehicle Occlusion dataset.
'''

import argparse

import numpy as np

from tqdm import tqdm

def argkmax(array, k):
    ''' Returns the positions of the top K elements in an array.
    '''
    return array.argsort()[-k:][::-1]

def main(output_weights, output_log, save_file, k):
    fnames = []

    print(f'Reading file names from `{output_log}`...')
    with open(output_log) as f:
        for line in f:
            line = line.strip()
            fnames.append(line)

    print(f'Reading output weights from `{output_weights}`...')
    output = np.load(output_weights)

    assert len(output) == len(fnames), (
        f'Number of output weights ({len(output)})'
        f'does not match number of files ({len(fnames)})!'
        )

    with open(save_file, 'w') as f:
        for weights, fname in zip(output, fnames):
            topk = argkmax(weights, k)
            topk_str = ' '.join(map(str, topk))
            f.write(f'{fname},{topk_str}\n')

    print(f'Done! Saved top {k} results to `{save_file}`.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('output_weights',
        help = 'path to .npy file with the output weights of the CORnet model',
        type = str
        )

    parser.add_argument('output_log',
        help = 'path to .log file with the order of evaluated files',
        type = str
        )

    parser.add_argument('save_file',
        help = 'path to file that saves the top K classes',
        type = str
        )

    parser.add_argument('-k',
        help = 'capture the top K classes',
        type = int,
        default = 5
        )

    args = parser.parse_args()

    main(
        output_weights = args.output_weights,
        output_log = args.output_log,
        save_file = args.save_file,
        k = args.k
        )
