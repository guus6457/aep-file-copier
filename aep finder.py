import os
import shutil

def copy_aep_files(download_folder, destination_folder):
    # Check if download folder exists
    if not os.path.exists(download_folder):
        print("Download folder does not exist.")
        return

    # Check if destination folder exists, if not create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get list of files in download folder
    files = os.listdir(download_folder)

    # Filter .aep files
    aep_files = [f for f in files if os.path.isfile(os.path.join(download_folder, f)) and f.endswith('.aep')]

    if not aep_files:
        print("No .aep files found in the download folder.")
        return

    # Copy .aep files to destination folder
    for aep_file in aep_files:
        src = os.path.join(download_folder, aep_file)
        dst = os.path.join(destination_folder, aep_file)
        shutil.copyfile(src, dst)
        print(f"Copied {aep_file} to {destination_folder}")

# Set your download folder path and destination folder path
download_folder = r"C:\Users\Guusv\Downloads"
destination_folder = os.path.join(download_folder, "aep")

# Call the function to copy .aep files
copy_aep_files(download_folder, destination_folder)
