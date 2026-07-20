"""Handles the configuration settings for the logging system, including warning levels, output styling, and silent mode."""

from pylogs import utils


## CONFIGS

_ignore_warnings = False # True=Ignore warnings
_warnings_level = 3 # 0=All, 1=Error, 2=Warnings, 3=Deprecated
_no_style = utils.is_nohup() # True=No color output
_is_silent = False

def set_ignore_warnings(warnings_level: int = 0, ignore: bool = True):
    """
    Enable or disable warning output filtering by level.

    Args:
        warnings_level (int): Minimum warning level to show.
        ignore (bool): Whether to suppress warnings below the level.
    """
    global _ignore_warnings, _warnings_level
    _ignore_warnings = ignore
    _warnings_level = warnings_level

def set_ignore_style(ignore: bool = True):
    """
    Enable or disable coloured output styling.

    Args:
        ignore (bool): Whether to suppress coloured output.
    """
    global _no_style
    _no_style = ignore

def set_silent_mode(silent: bool = True):
    """
    Enable or disable silent mode, which suppresses all output.

    Args:
        silent (bool): Whether to enable silent mode.
    """
    global _is_silent
    _is_silent = silent

