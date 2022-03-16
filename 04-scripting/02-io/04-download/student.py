from importlib.resources import contents
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as text:
    content = text.open()
    print(contents)


