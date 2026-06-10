# Rename all files in a specific folder by adding a prefix or date.
import os

target_folder_path = input("Enter the folder path, in which you want to rename files: ").strip()
prefix = input("Enter the prefix, you want to add : ")
list_everything = os.listdir(target_folder_path)

for each in list_everything:
    old_full_path = os.path.join(target_folder_path, each)
    if os.path.isfile(old_full_path):
        if each.startswith(prefix):
            continue
        else:
            new_filename = prefix + each
            new_full_path = os.path.join(target_folder_path, new_filename)
            os.rename(old_full_path, new_full_path)
            print("Successfully renamed.")