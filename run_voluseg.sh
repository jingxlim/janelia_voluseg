#!/bin/bash
source ~/janelia_voluseg/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
n_nodes=5
dir_output=/nrs/ahrens/jing/state_modulation/MG_vs_replayGU/20201101/fish02/9dpf_HuC-GC6F_MG-vs-ReplayGU_fish02_exp02_20201101_214112/im_CM0-voluseg
n_hours=24  ## default: 8
n_tasks=2  ## default: 2
janelia_voluseg_dir=~/janelia_voluseg/voluseg_spark_janelia
bsub -n32 -o /nrs/ahrens/jing/bsub_logs/%J.log $PYSPARK_PYTHON $janelia_voluseg_dir $n_nodes $dir_output $n_hours $n_tasks
