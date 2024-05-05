from .display import banner, menu
from .files import files
from .display import loading_and_clear
from .files import file_exist
from .pin import input_and_cek_pin

true = lambda: "", "", "", True

def create(title, list_dir, dir_name, extension):
    banner(f"List File ({title})")
    list_files = files()
    if not list_files[list_dir]:
        loading_and_clear("No list file in your diretory")
        return true
    source_file = menu(list_files[list_dir], "Back")
    if source_file == 0: return true
    elif source_file > len(list_files[list_dir]):
        loading_and_clear("", error=True, message="list file not found!")
        return true
    while True:
        output_file = input("Enter output file >> ")
        if output_file != "" and file_exist(list_files[dir_name], output_file, extension):
            file_name = [file_name for file_name in list_files[dir_name] if output_file in file_name]
            replace_content = input( f"({file_name[0]}) is not Empty!!!\nReplace content? (y/n) >> ").lower()== "y"
            if replace_content: break
            else: continue
        else: break
    pin = input_and_cek_pin()
    if output_file == "":
        default_number = len([file for file in list_files[dir_name] if "default" in file])
        output_file = f"default({default_number+1})"
    
    return list_files[list_dir][source_file - 1], output_file, pin, False