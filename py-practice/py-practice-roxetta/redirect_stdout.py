class RedirectStdoutTo:
  def __init__(self, out_new):
    self.out_new = out_new

  def __enter__(self):
    self.out_old = sys.stdout
    sys.stdout = self.out_new

  def __exit__(self, *args):
    sys.stdout = self.out_old
