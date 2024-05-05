import os
from time import sleep
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner(title):
    clear()
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def menu(choice, list_0):
    for i, m in enumerate(choice, 1):
        print(f"{i}.{m}")
    print(f"0.{list_0}")
    print("-" * 50)
    return int(input("Your choice >> "))

def loading_and_clear(text, error=False, message=""):
    if error:
        print(f"Error : {message}")
        sleep(2)
    else:
        print(text)
        sleep(2)
        clear()
