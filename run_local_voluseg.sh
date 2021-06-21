#!/bin/bash
source ~/janelia_voluseg/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
dir_output=/scratch/limj2/data/20210603/fish00/4dpf_HuC-h2b-GC7F_MG-vs-NGGU-bright-to-loom_fish00_exp02_20210603_180846/im_CM0_voluseg
output_log_path="${dir_output}/$(date +%Y%m%d_%H%M%S).log"
properties_file_path=~/janelia_voluseg/spark_properties_ws1.conf
echo "output log: ${output_log_path}"
nohup $SPARK_HOME/bin/spark-submit --properties-file $properties_file_path ~/janelia_voluseg/voluseg_submit.py $dir_output >> $output_log_path&
