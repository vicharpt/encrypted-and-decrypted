from .display import clear, banner
from time import sleep
def status_code(text, folder, output_file, extension):
    clear()
    banner(f"Successfully {text} code\nFile name : {folder}/{output_file}.{extension}")
    sleep(5)