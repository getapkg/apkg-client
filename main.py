#!/usr/bin/python3

# + ---------------------------------------------+
# (C) APKG Contributors 2025-2026
#     APKG-Client
# + ---------------------------------------------+

#
# This code sucks, you know it and I know it.
# Move on and call me an idiot later.
# P.S. please do not take the bincode treatment
# on me for this code, if you do -- there's no reason
# for me to live then like it is already
#                                         - OptimiDev
import os
import sys
import colorama
import argparse
from src.dac.download import download_pkg
from src.dac.reinstall import reinstall
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
    prog="apkg",
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

update_parser = subparsers.add_parser("update", help="Update a package")
update_parser.add_argument("package", help="Name of the package to update")

#idk if this works --elemental
reinstall_parser = subparsers.add_parser("reinstall", help="Reinstall a package")
reinstall_parser.add_argument("package", help="Name of the package to reinstall")

apkgupdate_parser = subparsers.add_parser("apkg-update", help="Update APKG")

args = parser.parse_args()

# -------------------------------
# Command dispatch
# -------------------------------
if args.command == "install":
    install(args.package)

if args.command == "remove":
    remove(args.package)

if args.command == "update":
    reinstall(args.package)

#idk if this works --elemental
if args.command == "reinstall":
    reinstall(args.package)
