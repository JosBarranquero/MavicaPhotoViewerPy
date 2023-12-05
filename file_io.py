import os
import fnmatch
from datetime import datetime
import shutil
import errors

# File name constants
IMAGE_FILE = "MVC-*.JPG"
DATA_FILE_EXT = ".411" # Mavica internal data files extension

# Source path and image files list
source = None
img_list = None

def initialize(path: str):
    """This function initializes the module, that is, setting the source directory and trying to load its contents"""
    global source
    source = path
    
    file_load()

def file_load():
    """This function loads the images filenames to a list"""
    file_list = os.listdir(source)
    global img_list
    img_list = []

    for file in file_list:
        file = file.upper()
        if fnmatch.fnmatch(file, IMAGE_FILE):
            img_list.append(file)

    # If no image files, disk is empty
    if (len(img_list) == 0):
        raise errors.EmptyDiskError

def file_import(output: str, folder_format: str = "%Y %m %d"):
    """This function imports the images to the output directory, creating a folder based on the images dates"""
    for i in range(len(img_list)):
        # Output directory
        folder_path = os.path.join(output, datetime.fromtimestamp(os.path.getmtime(os.path.join(source, img_list[i]))).strftime(folder_format))

        # Check if file does not exist and create if necessary
        if not (os.path.exists(folder_path)):
            os.makedirs(folder_path)

        # Getting the file name and extension, to check if a file with same name exists
        cur_file, extension = os.path.splitext(os.path.basename(img_list[i]))
        file_duplicate = 1

        # If the file exists, append a number to the file name
        while os.path.exists(os.path.join(folder_path, cur_file + extension)):
            cur_file, extension = os.path.splitext(os.path.basename(img_list[i]))
            cur_file += f" ({file_duplicate})"
            file_duplicate += 1
        try:
            shutil.copy2(os.path.join(source, img_list[i]), os.path.join(folder_path, cur_file + extension))
        except FileNotFoundError:
            raise    # If some file does not exist, something has happened to the disk contents

def file_delete(img_index: int):
    """This function deletes an image and its associated data file"""
    cur_file, extension = os.path.splitext(os.path.basename(img_list[img_index]))

    try:
        os.remove(os.path.join(source, cur_file + extension))
        os.remove(os.path.join(source, cur_file + DATA_FILE_EXT))
    except FileNotFoundError:
        pass    # If some file does not exist, ignore that
    except PermissionError:
        raise   # Disk is write-protected!

def disk_delete():
    """"This function deletes all the images (and their associated data files) on a disk"""
    deleted = False

    img_num = len(img_list)

    if (img_num > 0):
        for i in range(img_num):
            file_delete(i)

        deleted = True

    return deleted
            
if __name__ == "__main__":
    print("This script is not desingned to be standalone.")