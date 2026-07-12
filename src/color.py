"""Deprecated module for color handling. Use pylogs.color instead."""

from warnings import warn
from pylogs import color

warn("The 'color' module is deprecated. Use 'pylogs.color' instead.", DeprecationWarning, stacklevel=2)