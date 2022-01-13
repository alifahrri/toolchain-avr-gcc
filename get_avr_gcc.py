import urllib.request
import tarfile
from distutils.dir_util import copy_tree
from pathlib import Path

url = "https://github.com/modm-io/avr-gcc/releases/download/v9.2.0/avr-gcc.tar.bz2"
filename = "avr-gcc.tar.bz2"
urllib.request.urlretrieve(url,filename)
tar = tarfile.open(filename, "r:bz2")  
tar.extractall("./")
tar.close()
Path(filename).unlink()

# on avr gcc 9.2.0, the structure is:
# avr-gcc
#  | avr-binutils
#     | avr
#     | bin
#     | share
#  | avr-gcc
#     | avr
#     | bin
#     | include
#     | lib
#     | libexec
#     | share
path = Path("avr-gcc/avr-gcc").absolute()
parent_dir = path.parents[1]
for inner_path in path.iterdir():
    inner_path.rename(parent_dir/inner_path.name)
copy_tree("avr-gcc/avr-binutils/avr/", "avr/")
copy_tree("avr-gcc/avr-binutils/bin/", "avr/bin/")
copy_tree("avr-gcc/avr-binutils/share/", "share/")

import shutil
shutil.rmtree('avr-gcc')

import subprocess
subprocess.call(["tar", "-cvjSf", "toolchain-avr-gcc.tar.bz2", "."])