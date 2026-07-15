# Phage-induced cell perforation and lysis
Welcome to the perforation and lysis data and code repository!

## Repository structure
This repository is split into six folders, one for analysis and five for raw data.
Note that this is a joint code and data repository, where the full repository containing
both code and data is stored on ScienceDB. A version containing only code is stored on Github.
The code will not run without the data stored on ScienceDB.

### analysis
This folder contains all analysis relating to perforation and lysis. To run the analysis,
run each Python script in the indicated numerical order. Further explanation of the analysis
is found in analysis/00_read_me.txt.

### trench_x_images 
Raw data is stored in the directories named 'trench_x_images', where x is the trench number. 
The associated experimental metadata is also stored in each directory.


## Installation
To run the code, the following Python installation process is recommended. The required packages
are listed in the environment.yml file. As exact versions are specified, the resulting dependency
network is complex and can cause issues with some versions of the conda installer. The recommended 
process is to use the mamba installer. First install Anaconda or miniconda (https://www.anaconda.com/docs/getting-started/miniconda/system-requirements).
Then, from your terminal or Anaconda prompt, run these commands to first create a mamba installer environment:
```
conda create -n mamba_tool -c conda-forge mamba
conda activate mamba_tool
```
Then, navigate to the same directory as the environment.yml file (repository_inj_ga_tx/), and run:
```
mamba env create environment.yml
conda activate phage_analysis
```
You can now run the scripts from the Anaconda prompt or terminal window with `python <script_name>.py`.


## Plotting code 
The following gives a quick reference to find the code in this repository used to plot various figures in the paper.
    
* analysis/09_plot_perforation_data.py
  * Plots for the perforation time series data and perforation duration violin (fig 5d, 5e).
  * Plot for the perforation time series data showing all events (fig S13).


## Data integrity and preservation 
To ensure the integrity of your download, checksums are provided throughout the repository.
The checksums are generated using a SHA256 hash of each file. The checksums can be verified using the script 00_verify_checksums.py.

To verify your download integrity (assuming you have Python installed), simply run the command `python 00_verify_checksums.py` from a 
terminal or Windows command prompt from the relevant folder. For example, to check your download integrity of your repository_perforation_lysis folder, 
navigate to that folder in the terminal or command prompt window, then run `python 00_verify_checksums.py`. Note that the command may be 
slightly different depending on the operating system (Windows may require `py 00_verify_checksums.py`, 
while macOS may require `python3 00_verify_checksums.py`).

When the repository is first downloaded, the analysis folders will be compressed into zip files.
If the top-level script 00_verify_checksums.py runs and verifies all files correctly, then you can be confident the download has preserved 
the original integrity of the data. If anything does not match, there is some level of corruption. Lower level checksums are provided within each 
zipped analysis folder to allow the source of the corruption to be pinpointed. 


## License
The code used for this project, contained both in the main dataset on ScienceDB and separately on Github, is licensed under an MIT license
(see LICENSE-CODE.txt). The code was developed to operate on the dataset stored on ScienceDB. The image data, metadata, tables and other data stored 
in the dataset on ScienceDB are licensed separately under CC-BY 4.0 (see LICENSE-DATA.txt).

Therefore this work consists of two components under separate licenses:

Data (images, metadata, tables and other data):
Copyright 2026 Charlie Wedd, Ruizhe Li, Temur Yunusov, Aaron Smith, Georgeos Hardo, Michael Hunter, Aparna Kaaraal Mohan, Racha Majed, Diana Fusco, Somenath Bakshi. 
Licensed under CC BY 4.0 - see LICENSE-DATA.txt, https://creativecommons.org/licenses/by/4.0/

Code (analysis scripts):
Copyright 2026 Charlie Wedd, Ruizhe Li, Temur Yunusov, Aaron Smith, Georgeos Hardo, Michael Hunter, Aparna Kaaraal Mohan, Racha Majed, Diana Fusco, Somenath Bakshi. 
Licensed under MIT - see LICENSE-CODE.txt

Unless otherwise indicated, documentation describing the dataset, imaging methodology, and experimental design is covered under the CC BY 4.0 data
license; documentation describing code usage, installation, and software structure is covered under the MIT code license.
