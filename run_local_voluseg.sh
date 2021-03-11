#!/bin/bash
source ~/janelia_voluseg/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
dir_output=/nrs/ahrens/jing/state_modulation/MG_vs_replayGU/20201101/fish02/9dpf_HuC-GC6F_MG-vs-ReplayGU_fish02_exp02_20201101_214112/im_CM0-voluseg

$SPARK_HOME/bin/spark-submit ~/janelia_voluseg/voluseg_submit.py $dir_output
