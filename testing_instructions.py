import sublime
import sublime_plugin


class MoodleWriteTestingInstructionsCommand(sublime_plugin.WindowCommand):

    _template = """*Test pre-requisites*

- CURSOR

*Test steps*

# 
"""

    def run(self):
        view = self.window.new_file()
        edit = view.begin_edit()
        view.set_syntax_file('Syntaxes/Testing Instructions.tmLanguage')
        view.insert(edit, 0, self._template)
        region = view.find(r'CURSOR', 0)
        view.erase(edit, region)
        view.sel().clear()
        view.sel().add(sublime.Region(region.begin()))
        view.end_edit(edit)

    def description(self):
        return
        """
        Opens a new window with a template for writing testing instructions.
        """.strip()
