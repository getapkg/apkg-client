import subprocess
from pathlib import Path

import colorama
from colorama import Fore, Style

def run_dac(base_dir: Path):
    """
    Run compile.sh inside the given directory.
    Returns True if successful, False otherwise.
    """
    compile_sh = base_dir / "compile.sh"

    if not compile_sh.exists():
        print(Fore.RED + "[ERROR] compile.sh not found")
        print("Please contact the package maintainer.")
        return False

    # Make sure the script is executable
    compile_sh.chmod(0o755)

    try:
        print(colorama.Back.BLUE + " INFO " + colorama.Style.RESET_ALL + " Handing the rest of the process to the package installer.")
        subprocess.run(
            ["./compile.sh"],
            cwd=base_dir,
            check=True
        )
        print(Fore.GREEN + "[SUCCESS] compile.sh finished")
        return True
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[ERROR] Compilation failed ({e.returncode})")
        return False
