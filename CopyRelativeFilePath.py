import sublime
import sublime_plugin

class CopyRelativeFilePathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.file_name()) > 0:
      v = self.view.window().extract_variables()
      if v["file"] and v["folder"]:
        relative_path = v['file'].replace(f"{v['folder']}/", '', 1)
        sublime.set_clipboard(relative_path)
        sublime.status_message("Copied relative file path: %s" % relative_path)



  def is_enabled(self):
      return self.view.file_name() and len(self.view.file_name()) > 0
