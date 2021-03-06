# CMSC6950_Project
Course project for CMSC6950 Spring 2021

Software Package: eddy https://github.com/richteague/eddy

eddy implements several methods for extracting kinematical information from astronomical observations of Doppler shifted molecular line emission in protoplanetary disks. The package further implements methods to fit a first moment map that is a frequently used analysis in the study of protoplanetary disks, typically used to constrain the mass of the central star and extract geometrical properties.

**Khalid Ibne Hasan**

## Software Setup
Considering you already have a Conda installation, please install the following packages inside the Conda environment:
```
pip install astro-eddy==1.2.2
```
```
pip install bettermoments==1.2.1
```
```
pip install celerite
```
```
pip install astropy
```

## Reproducing Workflow
If you want to reproduce the workflow, download the repository, install the packages inside conda environment and run the following command to generate all the necessary files:
```
make
```
To delete all other files except the Python scripts:
``` 
make clean
```
Delete all the datasets and pdf
``` 
make deepclean
```
