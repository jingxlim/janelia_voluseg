# set up
import os
import pprint
import voluseg

### set these parameters ###
dir_input = '/scratch/limj2/data/20201017/fish02/8dpf_HuC-GCaMP7f-Gfap-rgeco_alldiromr_fish02_exp05_20201017_230842/im_CM1'
dir_output = '/scratch/limj2/data/20201017/fish02/8dpf_HuC-GCaMP7f-Gfap-rgeco_alldiromr_fish02_exp05_20201017_230842/im_CM1_voluseg'
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
parameters0['n_cells_block'] = 200  # increase block size to reduce blockiness in segments
# parameters0['registration'] = 'none'  # default: run registration
parameters0['parallel_volume']=False  # False if running on local workstation
parameters0['timepoints_type']='periodic'
parameters0['t_section'] = 0

# create parameter file with metadata
voluseg.step0_process_parameters(parameters0)

# check saved parameters
parameters = voluseg.load_parameters(os.path.join(dir_output, 'parameters.pickle'))
pprint.pprint(parameters)
