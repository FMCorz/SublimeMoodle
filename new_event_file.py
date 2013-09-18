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


class MoodleNewEventFileCommand(sublime_plugin.WindowCommand):

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
 * ${1:the_component} ${2/_/ /} event.
 *
 * @package    ${1:the_component}
 * @copyright  {YEAR} ${TM_FULLNAME}
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

namespace \${1:the_component}\\event;
defined('MOODLE_INTERNAL') || die();

/**
 * ${1:the_component} ${2/_/ /} event class.
 *
 * @package    ${1:the_component}
 * @copyright  {YEAR} ${TM_FULLNAME}
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */
class ${2:thing_happened} extends \\core\\event\\base {

    /**
     * Returns description of what happened.
     *
     * @return string
     */
    public function get_description() {
        // return "XXXXX";
    }

    /**
     * Legacy event data if get_legacy_eventname() is not empty.
     *
     * @return \\stdClass
     */
    // protected function get_legacy_eventdata() {
    //     \$eventdata = new \\stdClass();
    //     return \$eventdata;
    // }

    /**
     * Return the legacy event name.
     *
     * @return string
     */
    // public static function get_legacy_eventname() {
    //     return 'XXXXX';
    // }

    /**
     * Return the legacy event log data.
     *
     * @return array|null
     */
    // public function get_legacy_logdata() {
    //     return array();
    // }

    /**
     * Return localised event name.
     *
     * @return string
     */
    public static function get_name() {
        // return get_string('event_${2}', '${1:the_component}');
    }

    /**
     * Get URL related to the action
     *
     * @return \\moodle_url
     */
    public function get_url() {
        // return new \\moodle_url('/XXXXX/YYYYY.php', array());
    }

    /**
     * Init method.
     *
     * @return void
     */
    protected function init() {
        $0// \$this->data['crud'] = 'c';
        // \$this->data['level'] = self::LEVEL_OTHER;
        // \$this->data['objecttable'] = 'XXXXX';
    }

    /**
     * Custom validation.
     *
     * @throws \\coding_exception
     * @return void
     */
    // protected function validate_data() {
    //     if (!isset(\$this->other['XXXXX'])) {
    //        throw new \\coding_exception('The XXXXX need to be set in \$other.');
    //     }
    // }

}
"""
