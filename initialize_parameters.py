# set up
import os
import pprint
import voluseg

### set these parameters ###
dir_input = '/scratch/limj2/data/20210603/fish00/4dpf_HuC-h2b-GC7F_MG-vs-NGGU-bright-to-loom_fish00_exp02_20210603_180846/im_CM0'
dir_output = '/scratch/limj2/data/20210603/fish00/4dpf_HuC-h2b-GC7F_MG-vs-NGGU-bright-to-loom_fish00_exp02_20210603_180846/im_CM0_voluseg'
channel_file = os.path.join(dir_input,'ch0.xml')
stack_file = os.path.join(dir_input,'Stack_frequency.txt')
### end set these parameters ###

# get default parameters and set directories
parameters0 = voluseg.parameter_dictionary()
parameters0['dir_input'] = dir_input
parameters0['dir_output'] = dir_output

# retrieve metadata from channel and stack files
parameters0 = voluseg.load_metadata(parameters0, channel_file, stack_file)

# set other parameters as necessary
parameters0['diam_cell'] = 6.0  #  cell_diameter = 6: 100-150k cells, cell_diameter=5: ~300-400k cells
parameters0['n_cells_block'] = 300  # increase block size to reduce blockiness in segments
# parameters0['registration'] = 'none'  # default: run registration
parameters0['parallel_volume']=False  # False if running on local workstation
parameters0['timepoints_type']='periodic'

# create parameter file with metadata
voluseg.step0_process_parameters(parameters0)

# check saved parameters
parameters = voluseg.load_parameters(os.path.join(dir_output, 'parameters.pickle'))
pprint.pprint(parameters)
