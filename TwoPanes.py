import sublime
import sublime_plugin

class TwoPanesCommand(sublime_plugin.WindowCommand):

  def run(self):
    if self.window.num_groups() == 1:
      # open another group
      self.window.run_command('new_pane', {"move": False})
      # goto defintion should open in that group
    elif self.window.num_groups() == 2:
      # do nothing
      pass
    else:
      # do nothing at all
      sublime.status_message("More than two groups is not supported.")
      pass
