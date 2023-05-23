# Importing Glob Module to iterate through all the files in the directory
import glob
# Importing subprocess module to execute a command
import subprocess
# Importing Sys module
import sys, os
from pathlib import Path

# Specifying the directory for the UI Files
UI_INPUT_PATH = Path("./UI/Layouts")
# Finding all the available UI Files in the given directory
UI_files = glob.glob(str(UI_INPUT_PATH) + "/**/*.ui", recursive=True)
# Specifying the QRC File
QRC_FILE_PATH = [ str(Path(os.getcwd()).joinpath(Path("./UI/Resources/Resources.qrc"))) ]

# Defining function to modify the python compiled ui files for proper importing of the resource
def ImportResource(filename):
    # Initialising the file data
    file_data = ""
    # Adding the following lines at the beginning of each file
    ADD_TEXT = [ f'import sys, os\n', 
                f'from pathlib import Path\n',
                f'resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))\n',
                f'sys.path.append(str(resource_file_path))\n'
    ]
    # Opening the required file
    with open(filename, mode="r") as file:
        # Reading all the lines from the file
        file_data = file.readlines()
    # Adding contents to the file
    file_data = file_data[:1] + ADD_TEXT + file_data[1:]
    # Writing the contents of the file into a new text file
    with open(filename, mode='w') as file:
        # Writing all the lines to the text
        file.writelines(file_data)
        
# Defining function to converting all the `.ui` files into `.py` files
def convertUI(UI_files, resource=False):
    # Iterating through all the UI files found
    for each_file in UI_files:
        # Specifying the input file
        input_file = each_file
        # Fetching the input file name
        input_filename = Path(input_file).name
        # Checking if the file is a resource file
        if resource:
            # Specifying the output file
            output_file = each_file.replace(f"{input_filename}", f"{input_filename[:-4]}_rc.py")
            # Executing the command via system pyside6-rcc resource.qrt -o resource_rc.py
            subprocess.run(["pyside6-rcc", f"{input_file}", "-o", f"{output_file}"])
            
        else:
            # Specifying the output file
            output_file = each_file.replace(f"{input_filename}", f"ui_{input_filename[:-2]}py")
            # Exeucting the command via system
            subprocess.run(["pyside6-uic", f"{input_file}", "-o", f"{output_file}"])
            # Appending the file data
            ImportResource(output_file)

# Converting all the required UI Files
convertUI(UI_files)
# Converting the QRC File
convertUI(QRC_FILE_PATH, True)
# 
# ImportResource(r"D:\AI\AI_Visualizer\UI\Layouts\MainWindow\ui_MainWindow.py")