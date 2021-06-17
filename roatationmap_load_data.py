import matplotlib.pyplot as plt
import numpy as np
from eddy import rotationmap
from numpy import genfromtxt
import pickle

# Load Data from FITS file
def load_data(fits_file, fits_file_dv0, object_name):
    cube = rotationmap(path=fits_file,
                    uncertainty=fits_file_dv0,
                    downsample='beam',
                    clip=2.0)
                    
    #Save Data to intermediate file
    with open(object_name, 'wb') as cube_data:
        pickle.dump(cube, cube_data)

def main(argv):
    if len(argv) != 4:
        raise SystemExit('Usage: %s load fits file' % argv[0])
    load_data(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)