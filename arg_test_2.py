import os
import sys

string_object = ' '.join(sys.argv[2])
stripped = string_object.replace("\r"," ").replace("\\", " ")
print(sys.argv[1], stripped)
print(type(stripped))