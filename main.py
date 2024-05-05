import module

def main():
    while True:
        try:
            module.banner("Encrypt & Decrypt Code")
            match module.menu(["Encrypt", "Decrypt"], "Exit"):
                case 1:
                    source_file, output_file, pin, status = module.create("In your directory", "files", "encrypt", "txt")
                    if status: continue
                    else: module.encrypt(source_file, output_file, pin)
                case 2:
                    source_file, output_file, pin, status = module.create("Encrypt", "encrypt", "decrypt", "py")
                    if status: continue
                    else: module.decrypt(source_file, output_file, pin)
                case 0:
                    module.loading_and_clear("Thanks for using my app (^_^)")
                    exit()
                case _:
                    module.loading_and_clear("", error=True, message="Choice not found!")
        except ValueError:
            module.loading_and_clear("", error=True, message="Input invalid!")


if __name__ == "__main__":
    main()