#!/home/optimidev/PycharmProjects/GetASH/.venv/bin/python

import os
import sys
import colorama
import argparse
from src.dac.download import download_pkg
from src.uninst.uninstall import remove_pkg

colorama.init(autoreset=True)

def install(pkg_name):
    """Install a package by name."""
    if os.geteuid() != 0:
        print(colorama.Back.RED + " ERROR " + colorama.Back.RESET + " This script must be run with sudo/root.")
        sys.exit(1)
    else:
        download_pkg(pkg_name)

def remove(package_name):
    """Remove a package by name."""
    if os.geteuid() != 0:
        print(colorama.Back.RED + " ERROR " + colorama.Back.RESET + " This script must be run with sudo/root.")
        sys.exit(1)
    else:
        remove_pkg(package_name)

# -------------------------------
# Argument parsing
# -------------------------------
parser = argparse.ArgumentParser(
    description="Source-based Package Manager",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

# Install command
install_parser = subparsers.add_parser("install", help="Install a package")
install_parser.add_argument("package", help="Name of the package to install")

# Remove command
remove_parser = subparsers.add_parser("remove", help="Remove a package")
remove_parser.add_argument("package", help="Name of the package to remove")

args = parser.parse_args()

# -------------------------------
# Command dispatch
# -------------------------------
if args.command == "install":
    install(args.package)

if args.command == "remove":
    remove(args.package)
