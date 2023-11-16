"""
JSONofabitch
============

sloppy json parser. messy json parser. error correcting json parser. standarization of low standards

"""

__version__: str = "0.2.0"

from .jsonofabitch import *
__all__ = (
    "loads",
    "dumps",
    "correct",
    "dumpslob",
)

