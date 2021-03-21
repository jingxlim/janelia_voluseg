#!/bin/bash
source ~/janelia_voluseg/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
dir_output=/scratch/limj2/state_modulation/GRAB_NE/20210304/fish03/6dpf_GRABNE_MG-vs-LGGU-fmg_fish03_exp02_20210304_220752/im_CM0_voluseg
output_log_path="${dir_output}/$(date +%Y%m%d_%H%M%S).log"
properties_file_path=~/janelia_voluseg/spark_properties_ws1.conf
echo "output log: ${output_log_path}"
nohup $SPARK_HOME/bin/spark-submit --properties-file $properties_file_path ~/janelia_voluseg/voluseg_submit.py $dir_output >> $output_log_path&
