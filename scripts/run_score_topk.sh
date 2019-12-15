#!/bin/bash

LEVEL=$1
MODEL=$2

./score_topk.py ../output/${MODEL}/level${LEVEL}_top5.csv ../output/${MODEL}/level${LEVEL}_results/

