"""
Utility module for the pylogs library, providing simple helper functions.
"""

import re, sys


def is_nohup() -> bool:
    """
    Check if the script is running under nohup or with redirected output.

    For example:
    ```bash
    nohup python script.py &
    ```
    
    Returns:
        bool: True if stdout is not connected to a terminal (nohup or redirected), False otherwise.
    """
    return not sys.stdout.isatty()


def strip_ansi(text: str) -> str:
    """
    Remove ANSI color and formatting codes from text.

    Args:
        text (str): The input string potentially containing ANSI codes.

    Returns:
        str: The input string with ANSI codes removed.
    """
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    return ansi_escape.sub('', text)