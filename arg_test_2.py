import os
import sys

string_object = ''.join(sys.argv[2])
stripped = string_object.replace('\\r',"").replace('\\n','\n')
pkg_name = os.environ['PACKAGE_NAME']
print(sys.argv[1], stripped)
print(pkg_name)
#print(type(stripped))
