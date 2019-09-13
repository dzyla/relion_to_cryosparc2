import easygui

# input and output files. If don't have the easygui just provide the name
file = open(easygui.fileopenbox(), 'r')
# file = '/mnt/data/relion/particle.star'

# output file. Change the name if needed
output = open('coordinates_particles.star', 'w')

# extract only X Y and name of the micrograph
for handler in ['data_', 'loop_', '_rlnCoordinateX #1', '_rlnCoordinateY #2', '_rlnMicrographName #3']:
    print(handler, file=output)

# Do the loop through the star file
# It is important to check at which positions are CoordinateX and CoorinateY (usually 0 and 1).
# Depending on the stage from which particles will be extracted it is required to check where is exactly column
# _rlnMicrographName.
_rlnMicrographName_column = 8

# here .MRC or .mrc
_file_extension = '.mrc'

# here depends on the stage from cryosparc2. If doesn't work check the error message from Cryosparc2
_cryosparc_extension = '_patch_aligned_doseweighted.mrc'

for line in file:
    line_split = line.replace('\n', '').split()

    if len(line_split) > 8:
        print(line_split[0], line_split[1],
              line_split[_rlnMicrographName_column].split('/')[-1].replace(_file_extension, _cryosparc_extension),
              file=output)
