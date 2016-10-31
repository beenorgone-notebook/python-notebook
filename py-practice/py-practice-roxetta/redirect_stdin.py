import sys

class RedirectStdinTo:
	def __init__(self, in_new):
		self.in_new = in_new

	def __enter__(self):
		self.in_old = sys.stdin
		sys.stdin = self.in_new

	def __exit__(self, *args):
		sys.stdin = self.in_old
