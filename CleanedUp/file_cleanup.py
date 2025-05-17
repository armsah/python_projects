import os

folder_original = 'C:/Users/ezsahar/OneDrive - Ericsson/Desktop/PythonCourse'
folder_destination = 'C:/Users/ezsahar/OneDrive - Ericsson/Desktop/PythonCourse/CleanedUp'
os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)
    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)
