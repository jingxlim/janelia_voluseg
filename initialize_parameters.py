# set up
import os
import pprint
import voluseg

### set these parameters ###
dir_input = '/nrs/ahrens/jing/state_modulation/MG_vs_replayGU/20201101/fish02/9dpf_HuC-GC6F_MG-vs-ReplayGU_fish02_exp02_20201101_214112/im_CM0'
dir_output = '/nrs/ahrens/jing/state_modulation/MG_vs_replayGU/20201101/fish02/9dpf_HuC-GC6F_MG-vs-ReplayGU_fish02_exp02_20201101_214112/im_CM0-voluseg'
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
parameters0['diam_cell'] = 5.0

# create parameter file with metadata
voluseg.step0_process_parameters(parameters0)

# check saved parameters
parameters = voluseg.load_parameters(os.path.join(dir_output, 'parameters.pickle'))
pprint.pprint(parameters)
