# set up
import os
import pprint
import voluseg

### set these parameters ###
dir_input = '/scratch/limj2/data/raw/20211008/fish01/6dpf_elavl3-gc8f-gfap-jregeco_MG-vs-NGGU-trunc35_fish01_exp03_20211009_004814/im_CM0'
dir_output = '/scratch/im_CM0_voluseg'
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
parameters0['ds'] = 2  # default is 2 | if downsampled already, make sure this matches that
parameters0['diam_cell'] = 6.0  #  cell_diameter = 6: 100-150k cells, cell_diameter=5: ~300-400k cells
parameters0['n_cells_block'] = 200  # increase block size to reduce blockiness in segments
parameters0['registration'] = 'none'  # comment or set to 'medium' to enable default (i.e. run registration)
parameters0['parallel_volume']=False  # False if running on local workstation
parameters0['parallel_clean']=False  # False if running on local workstation
parameters0['timepoints_type']='periodic'
parameters0['t_section'] = 0

# create parameter file with metadata
voluseg.step0_process_parameters(parameters0)

# check saved parameters
parameters = voluseg.load_parameters(os.path.join(dir_output, 'parameters.pickle'))
pprint.pprint(parameters)
