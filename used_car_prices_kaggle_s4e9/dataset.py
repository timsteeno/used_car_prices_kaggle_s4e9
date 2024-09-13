import os
import subprocess
import zipfile

def download_and_extract_data():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Set the data directory to be one level up from the current script
    data_dir = os.path.join(current_dir, '..', 'data', 'raw')
    zip_file = os.path.join(data_dir, 'playground-series-s4e9.zip')
    
    if not os.path.exists(zip_file):
        os.makedirs(data_dir, exist_ok=True)
        try:
            subprocess.run(['kaggle', 'competitions', 'download', '-c', 'playground-series-s4e9', '-p', data_dir], 
                           check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading data: {e.stderr}")
            return

        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
        except zipfile.BadZipFile:
            print("Error: The downloaded file is not a valid zip file.")
            return
    else:
        print("File already exists. Skipping download.")

if __name__ == "__main__":
    download_and_extract_data()