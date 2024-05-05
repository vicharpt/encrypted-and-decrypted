import os
from glob import glob
from datetime import datetime as dt
def files():
    return {
        "files": [file for file in glob(f"*.py") if file != os.path.basename(__file__)],
        "encrypt": [file.replace("encrypt\\", "") for file in glob("encrypt/*.txt")] if [dir for dir in os.listdir() if "encrypt" in dir] else [],
        "decrypt": [file.replace("decrypt\\", "") for file in glob("decrypt/*.py")] if [dir for dir in os.listdir() if "decrypt" in dir] else []
    }

def file_exist(list_files, output_file, extension):
    for file_name in list_files:
        if file_name[len(file_name) - (len(output_file) + (len(extension)+1)) :] == f"{output_file}.{extension}": return True
    return False

def formatting_file_name(output_file):
    return f"{dt.now().strftime('%Y_%m_%d')}_create_{output_file}"

def perform_file_action(file, mode, code=""):
    with open(file, mode) as f:
        return f.write(code) if mode == "w" else f.read()