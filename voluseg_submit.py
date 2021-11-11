#!/usr/bin/env python

# set up
import os
import sys
import time
import pprint
import voluseg

if len(sys.argv) < 2:
    sys.exit('Usage: voluseg_submit.py [output-directory]')

dir_output = sys.argv[1]
file_output = os.path.join(dir_output, 'prepro.output')

#%%

# Get spark context
from pyspark.sql.session import SparkSession
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

with open(file_output, 'w') as fh:
    pprint.pprint(spark.sparkContext._conf.getAll(), fh)

#%%

# load parameters
parameters = voluseg.load_parameters(os.path.join(dir_output, 'parameters.pickle'))
with open(file_output, 'a') as fh:
    pprint.pprint(parameters, fh)

# tic = time.time()
# voluseg.step1_process_volumes(parameters)
# with open(file_output, 'a') as fh:
#     fh.write('step1_process_volumes: %.1f seconds\n'%(time.time() - tic))

# tic = time.time()
# voluseg.step2_align_volumes(parameters)
# with open(file_output, 'a') as fh:
#     fh.write('step2_align_volumes: %.1f seconds\n'%(time.time() - tic))

tic = time.time()
voluseg.step3_mask_volumes(parameters)
with open(file_output, 'a') as fh:
    fh.write('step3_mask_volumes: %.1f seconds\n'%(time.time() - tic))

## Manually define time points
# import os
# import numpy as np
# import h5py
# timeseries_h5_path = os.path.join(parameters['dir_output'], 'mean_timeseries.hdf5')
# new_timepoints = np.arange(0, parameters['volume_names'].shape[0], 20)

# with h5py.File(timeseries_h5_path, 'a') as hf:
#     timepoints_dataset = hf['timepoints']
#     print(f'Old timepoints: {timepoints_dataset[:]}')
#     del hf['timepoints']
#     hf.create_dataset('timepoints', data=new_timepoints)

# with h5py.File(timeseries_h5_path, 'r') as hf:
#     timepoints_dataset = hf['timepoints']
#     print(f'New timepoints: {timepoints_dataset[:]}')

tic = time.time()
voluseg.step4_detect_cells(parameters)
with open(file_output, 'a') as fh:
    fh.write('step4_detect_cells: %.1f seconds\n'%(time.time() - tic))

# shut down spark if not parallel clean
# only on the Janelia cluster
# if not parameters['parallel_clean']:
#     from subprocess import run
#     name_workers = sys.argv[2]
#     run(['bkill','-J',name_workers])

tic = time.time()
voluseg.step5_clean_cells(parameters)
with open(file_output, 'a') as fh:
    fh.write('step5_clean_cells: %.1f seconds\n'%(time.time() - tic))
