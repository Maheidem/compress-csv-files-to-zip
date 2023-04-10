import os
import zipfile
import argparse
from tqdm import tqdm

def compress_csv(folder_path):
    """
    This function compresses all .csv files in a given folder path. It uses the os.walk() method to iterate through the subdirectories and files of the folder path. For each .csv file, it creates a zip file with the same name and replaces the original file with the zip file. It then calculates the size saved by compressing and prints out a statement for each file, as well as a total size saved for all files combined.
    """
    total_size_saved = 0
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(subdir, file)
                original_size = os.path.getsize(file_path)
                zip_file_name = file.replace('.csv','')
                zip_path = os.path.join(subdir, zip_file_name+'.zip')
                print(f'File: {file_path} - Size: {round((original_size) / (1024 ** 3), ndigits=2)} GB')
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                    zf.write(file_path, file)
                os.remove(file_path)
                compressed_size = os.path.getsize(zip_path)
                size_saved = original_size - compressed_size
                total_size_saved += size_saved
    total_size_saved_gb = total_size_saved / (1024 ** 3)
    print(f'Total space saved: {total_size_saved_gb:.2f} GB')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', help='Root path for CSV files', required=True)
    args = parser.parse_args()
    root_path = args.path
    print('Path: {root_path}')
    print(' -- Starting -- ')
    compress_csv(root_path)