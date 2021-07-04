#!/bin/bash
source ~/janelia_voluseg/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
dir_output=/scratch/limj2/data/20201017/fish02/8dpf_HuC-GCaMP7f-Gfap-rgeco_barcoding_fish02_exp04_20201017_224356/im_CM0_voluseg
output_log_path="${dir_output}/$(date +%Y%m%d_%H%M%S).log"
properties_file_path=~/janelia_voluseg/spark_properties_ws1.conf
echo "output log: ${output_log_path}"
nohup $SPARK_HOME/bin/spark-submit --master local[*] --properties-file $properties_file_path ~/janelia_voluseg/voluseg_submit.py $dir_output >> $output_log_path&
