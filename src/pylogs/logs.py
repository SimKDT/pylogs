"""
Module for logging in a log file.

Example usage:
```python
logger = Logger(out_dir=Path(".logs"))
echo.info("This is an info message.")
echo.warning("This is a warning message.")
logger.close()
```
"""

import sys
from pathlib import Path
from datetime import datetime

from pylogs import echo, utils





# used for file logging
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            # Strip ANSI codes when writing to files (keep them for stdout)
            if hasattr(f, 'name') and f.name != '<stdout>':
                f.write(utils.strip_ansi(obj))
            else:
                f.write(obj)
            # f.flush()
    def flush(self) :
        for f in self.files:
            f.flush()

def get_logs_file(out_dir: Path | str) -> Path:
    """
    Retrieves the log file path based on the current timestamp and the specified output directory.

    Args:
        out_dir (Path): The directory where the log file will be saved.

    Returns:
        Path: The path to the log file.
    """
    log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")
    log = Path(out_dir) / log_filename
    return log

def set_logs(log_file: Path | str = get_logs_file(".logs")):
    """
    Sets up logging to a specified log file by redirecting stdout to both the console and the log file.

    Args:
        log_file (Path): The path to the log file.
    """
    log_file = Path(log_file)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    f = open(log_file, 'w')
    sys.stdout = Tee(sys.stdout, f)



class Logger:
    """
    Logger class to setup a new stdout stream that writes to both console and a log file.
    
    Args:
        out_dir (Path): The directory where the log file will be saved.
    """

    instance: 'Logger | None' = None
    """Current active instance of the logger in use."""


    def __init__(self, out_dir: Path | str = ".logs"):
        self.out_dir = Path(out_dir)
        self.log_file = get_logs_file(self.out_dir)
        self.original_stdout = sys.stdout
        set_logs(self.log_file)
        Logger.instance = self

    def close(self):
        """
        Close the logger and restore the original stdout stream.
        """
        sys.stdout = self.original_stdout
        echo.info(f"Logs saved to {self.log_file}")

if __name__ == "__main__":
    out_dir = Path(".logs")
    logger = Logger(out_dir)
    echo.info("This is an info message.")
    echo.warning("This is a warning message.")
    echo.error("This is an error message.")
    logger.close()

    import subprocess
    # run a subprocess to check if running in nohup the is_nohup method works
    print("Is nohup (terminal): ", utils.is_nohup())
    result = subprocess.run([sys.executable, "-c", "import thesis.logs as logs; print(logs.utils.is_nohup())"], capture_output=True, text=True)
    print(f"Is nohup (subprocess nohup): {result.stdout.strip()}")
