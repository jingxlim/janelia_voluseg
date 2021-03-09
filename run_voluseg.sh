#!/bin/bash
source ~/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
n_nodes=5
dir_output=/nrs/ahrens/jing/state_modulation/MG_vs_replayGU/20201101/fish02/9dpf_HuC-GC6F_MG-vs-ReplayGU_fish02_exp02_20201101_214112/im_CM0-voluseg
n_hours=  ## default: 8
n_tasks=  ## default: 2
bsub -n32 -o /nrs/ahrens/jing/bsub_logs/%J.log /groups/ahrens/home/limj2/anaconda3/envs/python37/bin/python janelia_voluseg/voluseg_spark_janelia $n_nodes $dir_output
