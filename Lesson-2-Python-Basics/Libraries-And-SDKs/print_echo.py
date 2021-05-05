import os
import sys

def echo_name(name):
    print_name = os.system("echo Hello, " + name)
    print(print_name)

name = sys.argv[1]

echo_name(name)

