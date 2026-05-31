*** Unprocessed images and event exclusion criteria ***
The unprocessed images and their associated metadata are found in directories named 'trench_<trench_number>_images'. The pixel to micron conversion for the images in 0.065 micron/pixel.
Lysis events are observed from five different trenches, and each lysis event is given a unique identifier. These are numbered in the order that the lysis events occur, starting with the first trench and continuing the total from the first lysis event in the second trench, and so on. A summary of the lysis timepoints for all events are found in the table '10ms_lysis_fiji_data_summary.csv'. 

*** Generating the raw intensity data ***
Fiji (ImageJ) was used to extract the phase contrast intensity data. This was done by drawing a static region of interest (ROI) over the lysing cell, and using the 'Plot Z-axis Profile' tool to extract the time series of mean phase contrast intensity over the region. Using the Fiji macro 'Macro.ijm', this was repeated for regions around the cell as described in the section below. 

*** Raw intensity data ***
This directory contains the raw data extracted from static masks in Fiji. The raw data file names are in the format lys_XX_Y.csv. Each file gives the mean phase contrast intensity time series data from one lysis event at one mask position.
In the filename, XX is a number, which is the unique cell identifier. Y has one of four values indicating where the intensity was measured.
c: 'cell' or 'centre'. This is data from the mask directly over the cell.
r: 'right'. This is the data from the mask adjacent to the cell, in the side trench directly next to the right side of the cell. Mask translated 1.43 micron (22 pixels) right of the 'cell' mask.
l: 'left'. This is the data from the mask adjacent to the cell, in the side trench directly next to the left side of the cell. Mask translated 1.43 micron (22 pixels) left of the 'cell' mask.
st: 'side trench'. This is data from the mask further to the right of the cell and moved towards the closed end of the trench, and acts as a control. Mask translated 2.15 micron (33 pixels) right of the 'cell' mask and 4.29 micron (66 pixels) towards the closed end of the trench relative to the 'cell' mask. 

*** Data processing and python scripts ***
The final results of the data processing are in the directory 'dataframes', and how they were obtained is explained in this text file and as more detailed comments in the individual python scripts.
If you wish to follow through the code and regenerate all the code-produced data in this directory, run the scripts in the directory 'minimal_data' in numerical order.
If you run into any package version issues, the files 'environment.txt' and 'environment.yml' contain the package versions used to run the code, so that you can see if the relevant package version matches that used by the authors. Note that this is not a minimal environment needed to run the code, and contains other packages which are not relevant. You do not need to install the whole list. 

*** 01_time_adjust_data.py ***
The true imaging interval was slightly longer than 10 ms. This script scales the time axis for each dataset by the true imaging interval found in the image metadata. It also collates the time series intensity profiles taken in different locations into one csv file for each infection. The results are stored in the directory 'lysis_data_time_adjusted'.

*** 02_plot_time_series.py ***
This script outputs time series plots of the output from the first script. The results are stored in the directory 'time_series_plots'.

*** 03_trim_oversized_data.py ***
As the function 'Plot Z-axis Profile' took a long time to run for large image stacks, and because the data will largely be irrelevant for earlier and later regions if the cells are in different positions relative to the mask, images were generally loaded in stacks of 10000. For reasons explained in the script, larger stacks sometimes had to be used, so these were trimmed.

*** 04_time_adjust_approximate_lysis_times.py ***
The file '10ms_lysis_times.csv' contains approximate lysis times obtained by inspection of the images. This script time adjusts the values by the true imaging interval and outputs a new table, '10ms_lysis_times_adjusted.csv', which is an important input in later scripts.

*** 05_lysis_detection_algorithm_testing.py ***
This script develops the algorithm for analysing the breakdown of the cell envelope (cell lysis, starting at the timepoint denoted t5 in the paper and including the events that follow). 
It includes example plots to explain the methods used. 

*** 06_lysis_detection_all_data.py ***
This script applies the algorithm from the fifth script to analyse the breakdown of the cell envelope for all included events (exclusions described in the file '10ms_lysis_fiji_data_summary.csv', and '10ms_lysis_exclusion_tallies.csv').
The output is 'cell_envelope_breakdown_analysis.csv', stored in the 'dataframes' directory.

*** 07_perforation_detection_algorithm_testing.py ***
This script develops the algorithm to detect the start of perforation, when material begins to leak out of the cell. Perforation starts at the timepoint t4 in the paper, and runs until timepoint t5.
It includes example plots to explain the methods used.

*** 08_peforation_detection_all_data.py ***
This script applies the algorithm from the seventh script to calculate the perforation duration for all included events (exclusions described in the file '10ms_lysis_fiji_data_summary.csv', and '10ms_lysis_exclusion_tallies.csv').
The output is 'perforation_analysis.csv', stored in the 'dataframes' directory.

*** 09_plot_perforation_data.py ***
Plot the example time series and perforation violin in figure 5, and the additional perforation time series found in the supplementary information.

*** 10_calculate_stats.py ***
Calculates descriptive statistics of the final results files, which are stored in the dataframes folder