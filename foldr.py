import sublime
import sublime_plugin

class FoldrNextCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    current = self.view.sel()[0]
    regions = self.view.folded_regions()
    next_fold_idx = 0
    # test

    if regions:
      for idx, region in enumerate(regions):
        if region.contains(current):
          next_fold_idx = idx + 1
          break

      if len(regions) < next_fold_idx + 1:
          next_fold_idx = 0

      self.view.sel().clear()
      self.view.sel().add(regions[next_fold_idx])
      self.view.show(self.view.sel()[0])
