import os
import shutil

# Path of the desktop folder
desktop_path = os.path.expanduser("C:/Users/ezsahar/OneDrive - Ericsson/Desktop")
print('desktop path:', desktop_path)

# Dictionary containing the folder names and their corresponding file extensions
folders = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"}   
}

# Create the subfolders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
     original_file_path = os.path.join(desktop_path, file_name)
     if os.path.isfile(original_file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    # print(original_file_path, destination_folder)
                    shutil.move(original_file_path, destination_folder)