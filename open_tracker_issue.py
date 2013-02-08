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
import re
import webbrowser
from tools import process


class MoodleOpenTrackerIssueCommand(sublime_plugin.WindowCommand):

    def run(self, prompt=False):
        window = self.window
        view = window.active_view()
        issue = None

        if not prompt:
            issue = resolveIssueNumber(view, window.folders())

        if prompt or not issue:
            window.show_input_panel('Issue number', '', lambda x: openTrackerIssue(extractIssueNumberFromText(x)), None, None)
        else:
            openTrackerIssue(issue)

    def description(self):
        return
        """
        Opens an issue on Moodle Tracker, reads the MDL from the selected text or current branch.
        """.strip()


def extractIssueNumberFromText(text):
    """Returns an issue number from the text passed"""
    mdl = re.search(r'(MDL(-|_)?)?([0-9]+)', text, re.I)
    if mdl != None:
        return mdl.group(3)
    return None


def openTrackerIssue(number):
    """Opens a tracker issue in a new browser tab"""
    url = 'https://tracker.moodle.org/browse/MDL-%issue%'
    if number:
        webbrowser.open_new_tab(url.replace('%issue%', number))


def resolveIssueNumber(view, folders):
    """Try to find an issue number"""

    issue = None

    # Read from the content of the file.
    if view:
        for region in view.sel():
            if region.empty():
                region = view.word(region)
            word = view.substr(region)
            issue = extractIssueNumberFromText(word)
            if issue != None:
                break

    # Read from the folders.
    if not issue:
        for folder in folders:
            result = process('git symbolic-ref -q HEAD', cwd=folder)
            if result[0] == 0 and result[1] != '':
                issue = extractIssueNumberFromText(result[1])
                if issue != None:
                    break

    return issue
