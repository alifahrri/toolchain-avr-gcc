# Toolchain AVR GCC

Modern C++ Toolchain for AVR-GCC with PlatformIO.

## Installation

1. Get the tarball from `Assets` under [`Releases`](https://github.com/alifahrri/toolchain-avr-gcc/releases) tab, for example `toolchain-avr-gcc.tar.bz2`.
2. In your `platformio.ini`, override `toolchain-atmelavr`:
```
platform_packages = 
    toolchain-atmelavr@file://toolchain-avr-gcc.tar.bz2
```