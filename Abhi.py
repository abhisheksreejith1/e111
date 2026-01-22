import os
import sys
import time

# Attempt to import libraries; provide instructions if they are missing
try:
    import pyfiglet
    from colorama import Fore, Style, init
except ImportError:
    print("Missing required libraries. Please run: pip install pyfiglet colorama")
    sys.exit()

# Initialize Colorama for Windows/Mac/Linux compatibility
init(autoreset=True)

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading_animation():
    """Simple dots animation for a 'pro' software feel."""
    print(Fore.YELLOW + "Initializing system", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

def display_banner(name):
    """Generates and prints the stylized banner."""
    # Create the ASCII art using the 'slant' font
    ascii_banner = pyfiglet.figlet_format(name, font="slant")
    
    print(Fore.CYAN + Style.BRIGHT + "-" * 60)
    print(Fore.GREEN + ascii_banner)
    print(Fore.CYAN + Style.BRIGHT + "-" * 60)
    print(Fore.WHITE + Style.DIM + f"Welcome back, {name} | Session Started: {time.ctime()}")
    print("\n")

def main():
    clear_screen()
    show_loading_animation()
    display_banner("Abishekk")
    
    # Your main code starts here
    print(Fore.WHITE + "System is ready for commands...")

if __name__ == "__main__":
    main()
