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

import sublime
import sublime_plugin
import os
import datetime


class MoodleNewFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.new_file()
        syntax = os.path.join(sublime.packages_path(), 'PHP/PHP.tmLanguage')
        view.set_syntax_file(syntax)
        view.run_command('insert_snippet', {
            "contents": self.snippet.replace('{YEAR}', str(datetime.date.today().year))
        })

    def description(self):
        return
        """
        Opens a new window with a template for writing testing instructions.
        """.strip()

    snippet = """<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * ${1:File}.
 *
 * @package    ${2:core}
 * @copyright  {YEAR} ${TM_FULLNAME}
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

${3:defined('MOODLE_INTERNAL') || die();}
$0"""
