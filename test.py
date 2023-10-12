from colorama import Fore, Back, Style, init
import sys
import time

init(autoreset=True)

def type(text, delay=0.05, style=Fore.WHITE):
    for char in text:
        sys.stdout.write(style + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
