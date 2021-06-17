import matplotlib.pyplot as plt
import numpy as np
from eddy import rotationmap
from numpy import genfromtxt
import pickle
import csv
 
def fit_map_plot(filename): 
    with open(filename, 'rb') as cube:
        cube_data = pickle.load(cube)

    params = {}

    params['x0'] = 0
    params['y0'] = 1
    params['PA'] = 2
    params['mstar'] = 3
    params['vlsr'] = 4

    p0 = [0.0, 0.0, 151., 0.65, 2.8e3]

    params['inc'] = 6.8     # degrees
    params['dist'] = 60.1   # parsec

    percentiles = cube_data.fit_map(p0=p0, params=params, nwalkers=16, nburnin=200, nsteps=100, plots="mask", returns="dict")

    print("Source Center (x0, y0): ", (percentiles['x0'], percentiles['y0']))
    print("Position angle of the disk (PA): ", percentiles['PA'])
    print("Stellar Mass (MSTAR): ", percentiles['mstar'])
    print("Systemic Velocity (VLSR): ", percentiles['vlsr'])

    with open(filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Source Center (x0, y0)", "Position angle of the disk (PA)", "Stellar Mass (MSTAR)", "Systemic Velocity (VLSR)"])
        writer.writerow([(percentiles['x0'], percentiles['y0']), percentiles['PA'], percentiles['mstar'], percentiles['vlsr']])

def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s plot data' % argv[0])
    fit_map_plot(argv[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)