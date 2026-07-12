"""Deprecated module for echo handling. Use pylogs.echo instead."""

from warnings import warn
from pylogs import echo

warn("The 'echo' module is deprecated. Use 'pylogs.echo' instead.", DeprecationWarning, stacklevel=2)