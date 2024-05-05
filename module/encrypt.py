import os
from .author import author
from .files import perform_file_action, formatting_file_name
from .combine_code import combine_ord
from .display import loading_and_clear
from .status_code import status_code
def encrypt(source_file, output_file, pin):
    source_file = f"{author}{perform_file_action(f'{source_file}', 'r')}"
    source_code = combine_ord(f"{source_file[:len(source_file) - int(pin[-1])]}{pin}{source_file[-int(pin[-1]):]}", int(pin[-1]))

    output_file = formatting_file_name(output_file)
    
    os.makedirs("encrypt", exist_ok=True)
    loading_and_clear("Encrypting code...")
    perform_file_action(f"encrypt/{output_file}.txt", "w", source_code)
    status_code("encrypted", "encrypt", output_file, "txt")