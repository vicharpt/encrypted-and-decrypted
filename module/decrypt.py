import os
from .pin import get_pin
from .files import perform_file_action
from .display import loading_and_clear
from .combine_code import combine_chr
from .status_code import status_code
def decrypt(source_file, output_file, pin):
    pin_verified = get_pin(perform_file_action(f"encrypt/{source_file}", "r")[::-1][:60], int(pin[-1]))
    if pin != pin_verified:
        return loading_and_clear("", error=True, message="Wrong pin")

    source_file = combine_chr(perform_file_action(f"encrypt/{source_file}", "r"), int(pin[-1]))
    source_code = source_file[: len(source_file) - (int(pin[-1]) + 6)] + source_file[-int(pin[-1]) :]

    os.makedirs("decrypt", exist_ok=True)
    loading_and_clear("Generate code...")
    perform_file_action(f"decrypt/{output_file}.py", "w", source_code)
    status_code("generated", "decrypt", output_file, "py")