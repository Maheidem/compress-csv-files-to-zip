# Zip CSV in Folders

This is a Python script that compresses all .csv files in a given folder path using multiprocessing. For each .csv file, it creates a process to compress the file in parallel. It then calculates the total size saved by compressing and prints out a statement for each file, as well as a total size saved for all files combined.

## Prerequisites

To run this script, you will need:

- Python 3.6 or higher installed
- The following Python libraries installed:
  - `argparse`
  - `multiprocessing`
  - `os`
  - `zipfile`

## Usage

1. Clone this repository or download the `zip_csv_in_folders.py` file.
2. Open a terminal window and navigate to the folder containing the `zip_csv_in_folders.py` file.
3. Run the script with the following command:  
  3.1  `python zip_csv_in_folders.py -path "/path/to/csv/files" -n_cpu 4`  
  3.2  Replace `/path/to/csv/files` with the root path of the folder containing the .csv files you want to compress.  
  3.3  Replace `4` with the number of CPUs you want to use (optional). If not specified, the script will use all available CPUs except one.  
4. Wait for the script to finish compressing all .csv files in the specified folder and subfolders.
5. The script will print a statement for each file, as well as a total size saved for all files combined.

Note: This script will replace the original .csv files with the compressed .zip files. If you want to keep the original files, make sure to create a backup before running the script.

## Arguments

The `zip_csv_in_folders.py` script accepts the following arguments:

- `-path`: The root path of the folder containing the .csv files you want to compress (required).
- `-n_cpu`: The number of CPUs to use for parallel processing (optional). If not specified, the script will use all available CPUs except one.


1. Main point 1
2. Main point 2
3. Main point 3
   3.1 Sub-point A
   3.2 Sub-point B
      3.2.1 Sub-sub-point 1
      3.2.2 Sub-sub-point 2
   3.3 Sub-point C
4. Main point 4

