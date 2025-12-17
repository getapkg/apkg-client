import shutil
from pathlib import Path
from colorama import Back, Style, Fore

def remove_pkg(package_name):
    """Remove a package completely from /opt."""
    base_dir = Path("/opt") / package_name
    if not base_dir.exists():
        print(Fore.YELLOW + f"[WARNING] Package '{package_name}' is not installed.")
        return False
    try:
        shutil.rmtree(base_dir)
        print(Back.GREEN + " DONE " + Style.RESET_ALL + f" Package '{package_name}' removed successfully.")
        return True
    except Exception as e:
        print(Back.RED + " ERROR " + Style.RESET_ALL + f" Failed to remove '{package_name}': {e}")
        return False
