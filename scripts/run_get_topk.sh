#!/bin/bash

LEVEL=$1

./get_topk.py ~/cornet_r_results/level${LEVEL}_out/CORnet-R_decoder_output_feats.npy ~/cornet_r_results/level${LEVEL}_out/order.log ~/6804_final_project/output/R/level${LEVEL}_top5.csv
