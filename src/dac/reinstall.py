import colorama
from ..uninst.uninstall import remove_pkg
from .download import download_pkg
colorama.init()

def reinstall(package):
    a = input(colorama.Back.BLUE + " INFO " + colorama.Style.RESET_ALL + "Are you sure this will update the package [yes/no]" + package) #idk if this works --elemental
    if a.lower() == "yes" or a.lower() == "y":
        print(colorama.Back.BLUE + f" INFO " + colorama.Style.RESET_ALL + "Reinstalling " + package)
        remove_pkg(package)
        download_pkg(package)
        print(colorama.Back.BLUE + " INFO " + colorama.Style.RESET_ALL + "Done")
