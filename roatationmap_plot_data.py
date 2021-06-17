import matplotlib.pyplot as plt
import numpy as np
from eddy import rotationmap
from numpy import genfromtxt
import pickle

def plot_data(filename, image_output):
    #Read Data from intermediate file
    with open(filename, 'rb') as cube:
        cube_data = pickle.load(cube)

    # Plot Data
    fig, ax = plt.subplots()
    levels = np.nanpercentile(cube_data.data, [2, 98]) - cube_data.vlsr
    levels = max(abs(levels[0]), abs(levels[1]))
    levels = cube_data.vlsr + np.linspace(-levels, levels, 30)
    im = ax.contourf(cube_data.xaxis, cube_data.yaxis, cube_data.data, levels,
                    cmap=rotationmap.colormap(), extend='both', zorder=-9)
    cb = plt.colorbar(im, pad=0.03, format='%.2f')
    cb.minorticks_on()
    cb.set_label(r'${\rm v_{0} \quad (km\,s^{-1})}$',
                rotation=270, labelpad=15)
    plt.savefig(image_output)

def main(argv):
    if len(argv) != 3:
        raise SystemExit('Usage: %s plot data' % argv[0])
    plot_data(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)