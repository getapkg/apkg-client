import requests
import zipfile
from pathlib import Path
from colorama import Fore, Style, init, Back
from . import compile_dac
import os

init(autoreset=True)

DEF_MIRROR = "http://localhost:3000/releases/0.1/"
PACKAGES_URL = DEF_MIRROR + "packages.json"

def fetch_packages():
    """Fetch packages.json from the mirror."""
    try:
        r = requests.get(PACKAGES_URL)
        r.raise_for_status()
        return r.json().get("packages", {})
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to fetch packages.json: {e}")
        return None

def download_pkg(package_name):
    """Download, extract, compile, and cleanup a package."""
    packages = fetch_packages()
    base_dir = Path("/opt") / package_name
    if not packages:
        return False

    if package_name not in packages:
        print(Fore.RED + f"[ERROR] Package '{package_name}' not found")
        return False

    if base_dir.exists() and any(base_dir.iterdir()):
        print(Back.GREEN + " INFO " + Style.RESET_ALL +
              f" Package '{package_name}' is already installed at {base_dir}")
        return True

    maintainer_name = packages[package_name].get("maintainer_name", "Unknown")
    maintainer_email = packages[package_name].get("maintainer_email", "Unknown")
    print(Back.CYAN + " INFO " + Style.RESET_ALL +
          f" Installing '{package_name}' maintained by {maintainer_name} <{maintainer_email}>")


    file_name = packages[package_name]["file"]
    url = DEF_MIRROR + file_name

    base_dir = Path("/opt") / package_name
    zip_path = base_dir / "file.zip"


    base_dir.mkdir(parents=True, exist_ok=True)

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(zip_path, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
    except Exception as e:
        print(Back.RED + " ERROR " + Style.RESET_ALL + f" Failed to download: {e}")
        return False
    try:
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(base_dir)
    except Exception as e:
        print(Back.RED + " ERROR " + Style.RESET_ALL + f" Failed to extract ZIP: {e}")
        return False

    # Remove the ZIP after extraction
    try:
        os.remove(zip_path)
    except Exception as e:
        print(Back.YELLOW + " WARNING " + Style.RESET_ALL + f" Failed to remove file.zip: {e}")

    # Run compile script
    print(Fore.YELLOW + "[INFO] Compiling...")
    success = compile_dac.run_dac(base_dir)

    if success:
        print(Back.GREEN + " DONE " + Style.RESET_ALL + "[SUCCESS] Installation complete")
    else:
        print(Fore.RED + "[ERROR] Installation failed")

    return success
