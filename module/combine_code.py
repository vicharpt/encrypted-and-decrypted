def combine_ord(text, shift):
    return "/".join(str(ord(char) + shift) for char in text)

def combine_chr(text, shift):
    return "".join(chr(int(char) - shift) for char in text.split("/"))