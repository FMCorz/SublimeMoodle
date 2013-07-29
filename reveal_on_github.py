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

import sublime_plugin
import os
import webbrowser


class MoodleRevealOnGithub(sublime_plugin.TextCommand):
    """Opens the file at current line on Github"""

    githuburl = 'https://github.com/[[ACCOUNT]]/moodle/blob/master'
    defaultaccount = 'moodle'

    def run(self, edit, account=None):
        fn = os.path.abspath(os.path.realpath(os.path.expanduser(self.view.file_name())))
        regions = self.view.sel()
        if len(regions) > 1:
            return
        region = regions[0]
        (row, col) = self.view.rowcol(region.begin())

        folders = self.view.window().folders()
        for folder in folders:
            folder = os.path.abspath(os.path.realpath(folder))
            if fn.startswith(folder):
                fn = fn.replace(folder, '')

        account = account if account else self.defaultaccount
        baseurl = self.githuburl.replace('[[ACCOUNT]]', account)
        webbrowser.open_new_tab(baseurl + fn + u'#L' + str(row + 1))

    def is_enabled(self):
        return len(self.view.window().folders()) > 0
