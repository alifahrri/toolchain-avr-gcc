import urllib.request
import tarfile
from pathlib import Path

url = "https://github.com/modm-io/avr-gcc/releases/download/v9.2.0/avr-gcc.tar.bz2"
filename = "modm-avr-gcc.tar.bz2"
urllib.request.urlretrieve(url,filename)
tar = tarfile.open("modm-avr-gcc.tar.bz2", "r:bz2")  
tar.extractall("./")
tar.close()

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
path.rmdir()
path = Path("avr-gcc/avr-binutils")
path.rename("avr-binutils")
# Path(filename).unlink()