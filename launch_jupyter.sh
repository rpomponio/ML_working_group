#!/bin/bash

## functions are not exported by default to be made available in subshells
source /Users/pomponir/opt/anaconda3/etc/profile.d/conda.sh

conda activate my-torch

cd ~/Documents/Software/ML_working_group/

jupyter notebook

