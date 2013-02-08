#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Moodle bundle for Sublime Text

Copyright (c) 2013 Frédéric Massart - FMCorz.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

http://github.com/FMCorz/SublimeMoodle
"""

import shlex
import subprocess


def process(cmd, cwd=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """Executes a command"""
    if type(cmd) != 'list':
        cmd = shlex.split(str(cmd))
    proc = subprocess.Popen(cmd, cwd=cwd, stdout=stdout, stderr=stderr)
    (out, err) = proc.communicate()
    return (proc.returncode, out, err)
