import sublime
import sublime_plugin
import re


class uniqCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        try:
            content = self.view.substr(sublime.Region(0, self.view.size()))
            re_content = re.sub(r'(?m)^([^\r\n]*)$([\s\S]*?)(?:(?:\r?\n|\r)\1$)+', r'\1\2', content)
            regions = sublime.Region(0, self.view.size())
            self.view.sel().clear()
            self.view.replace(edit, regions, re_content)

        except Exception as e:
            print(e.message)