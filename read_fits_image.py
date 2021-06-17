import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
from eddy import rotationmap
np.random.seed(123)

def read_fits(fits_file, image_output):
    hdul = fits.open(fits_file, memmap=True)

    data = hdul[0].data

    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.colorbar()
    plt.savefig(image_output)

def main(argv):
    if len(argv) != 3:
        raise SystemExit('Usage: %s read fits file' % argv[0])
    read_fits(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)