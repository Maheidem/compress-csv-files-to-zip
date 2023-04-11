import os
import zipfile
import argparse
from multiprocessing import Pool, cpu_count


def compress_csv(file_path):
    """
    This function compresses a single .csv file. 
    It creates a zip file with the same name and replaces the original file with the zip file. 
    It then returns the size saved by compressing.
    """
    try:
        original_size = os.path.getsize(file_path)
        zip_file_name = os.path.splitext(file_path)[0] + '.zip'
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(file_path, os.path.basename(file_path))
        os.remove(file_path)
        compressed_size = os.path.getsize(zip_file_name)
        size_saved = original_size - compressed_size
        return size_saved
    except OSError as e:
        print(f"Warning: {file_path} could not be compressed. {e}")
        return 0


def compress_csv_parallel(folder_path, n_cpu=cpu_count()-1):
    """
    This function compresses all .csv files in a given folder path using multiprocessing. 
    It uses the os.walk() method to iterate through the subdirectories and files of the folder path. 
    For each .csv file, it creates a process to compress the file in parallel. 
    It then calculates the total size saved by compressing and prints out a statement for each file,
    as well as a total size saved for all files combined.
    """
    total_size_saved = 0
    file_list = []
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(subdir, file)
                file_list.append(file_path)
    print(f"Foram identificados: {len(file_list)} arquivos para serem compactados.")
    with Pool(n_cpu) as pool:
        results = list(pool.imap(compress_csv, file_list))
    total_size_saved = sum(results)
    total_size_saved_gb = total_size_saved / (1024 ** 3)
    print(f'Total space saved: {total_size_saved_gb:.2f} GB')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', help='Root path for CSV files', required=True)
    parser.add_argument('-n_cpu', help='Number of CPUs to use', required=False)
    args = parser.parse_args()
    root_path = args.path
    n_cpu = int(args.n_cpu)
    print(f'Path: {root_path}')
    print(f'CPUs to use: {n_cpu}')
    print('STARTING')
    compress_csv_parallel(root_path, n_cpu)
