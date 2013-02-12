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

settings = sublime.load_settings('SublimeMoodle.sublime-settings')


class MoodleWriteTestingInstructionsCommand(sublime_plugin.WindowCommand):

    _syntax = 'Jira.tmLanguage'

    def run(self):
        view = self.window.new_file()

        here = os.path.dirname(os.path.realpath(__file__))
        syntax = os.path.join(here, self._syntax)
        if os.path.isfile(syntax):
            view.set_syntax_file(syntax)

        view.run_command('insert_snippet', {"contents": settings.get('testing_instructions_snippet')})

    def description(self):
        return
        """
        Opens a new window with a template for writing testing instructions.
        """.strip()
