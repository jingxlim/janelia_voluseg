#!/bin/bash
source ~/janelia_voluseg/.bashrc_voluseg
mkdir $SPARK_LOG_DIR
properties_file_path=~/janelia_voluseg/spark_properties_ws1.conf

# no need final slash
dir_outputs=(

    # /scratch/limj2/data/20201017/fish02/8dpf_HuC-GCaMP7f-Gfap-rgeco_barcoding_fish02_exp04_20201017_224356/im_CM1_voluseg
    # /scratch/limj2/data/20201017/fish02/8dpf_HuC-GCaMP7f-Gfap-rgeco_alldiromr_fish02_exp05_20201017_230842/im_CM0_voluseg
    /scratch/im_CM0_voluseg
    # /scratch/limj2/data/raw/20211008/fish01/6dpf_elavl3-gc8f-gfap-jregeco_MG-vs-NGGU-trunc35_fish01_exp03_20211009_004814/im_CM0_voluseg
)

for dir_output in "${dir_outputs[@]}"
do
 
    output_log_path="${dir_output}/$(date +%Y%m%d_%H%M%S).log"
    echo "output log: ${output_log_path}"

    setsid $SPARK_HOME/bin/spark-submit --master local[*] --properties-file $properties_file_path ~/janelia_voluseg/voluseg_submit.py $dir_output >> $output_log_path&
    wait

done

echo "All datasets processed!"
