#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by m.galbusera
# Copyright (c) 2014 m.galbusera
#
# License: MIT
#

"""This module exports the Twiglint plugin class."""

from SublimeLinter.lint import Linter


class Twiglint(Linter):

    """Provides an interface to twiglint."""

    syntax = ('twig', 'html (twig)', 'html')
    cmd = 'twig-lint lint'
    version_args = '--version'
    version_re = r'version v(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0.1'
    regex = (
        r'(?ism)KO in [^(]+\(line (?P<line>\d+)\).+?>> \d+ .+?>> (?P<message>[^\r\n]+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'twig'
