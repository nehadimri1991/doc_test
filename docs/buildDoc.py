# pylint: skip-file
# type: ignore

import os

os.system("sphinx-apidoc -f -o . ../optihood")
# os.system('make clean')
os.system("make html")
# os.system('make pdf')
# os.system('sphinx-build -b pdf ../pytrnsys')
