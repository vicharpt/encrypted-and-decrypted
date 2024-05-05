from .combine_code import combine_chr
def get_pin(code, key):
    pin = []
    i = 0
    count = 0
    while count < key:
        if code[i] == "/":
            count += 1
            if count == key:
                pin.append(code[i + 1 : i + 18][::-1])
                break
        i += 1
    return combine_chr("".join(pin), key)

def input_and_cek_pin():
    while True:
        pin = input("Enter pin (6 digit) >> ")
        if len(pin) == 6 and pin.isdigit():
            if pin[-1] == "0": return f"{pin[:len(pin)-1]}1"
            return pin
        else: print("Pin only numbers and 6 digit!")