import os
import sys

stripped = sys.argv[2:].replace("\\r"," ").replace("\\", " ")
print(sys.argv[1], stripped)
print(type(stripped))
