# Python SuperBLT Hash Calculator

Latest version v1.0.

## Overview

Python implementation of the [SuperBLT hashing library](https://gitlab.com/SuperBLT/HashLib). Hashing single files is supported as well as hashing folders. Available as a standalone command line executable or as a Python script.

Command line executable built using PyInstaller. Source code for command line version available in [SuperBLT_Hasher_Command_Line.py](https://github.com/fragtrane/Python-SuperBLT-Hash-Calculator/blob/master/Command%20Line/SuperBLT_Hasher_Command_Line.py).

## SuperBLT Hashing Scheme

When hashing a directory, SuperBLT first calculates the SHA-256 hash of all files in the directory and any subdirectories. The path to each file is converted to a lowercase string and the paths are sorted based on the Unicode value of each character in the string. The hashes are converted into hexadecimal strings and concatenated according to the order of the sorted paths. The byte value of the concatenated hash string is hashed again using SHA-256. This result is converted into a hexadecimal string and is taken as the SuperBLT hash value of the directory.

When hashing a single file, SuperBLT first calculates the SHA-256 hash of the file. The resulting hash is converted into a hexadecimal string and the byte value of the string is hashed again using SHA-256. This result is converted into a hexadecimal string and is taken as the SuperBLT hash value of the file.

## Usage (Command Line)

Download [hash.exe](https://github.com/fragtrane/Python-SuperBLT-Hash-Calculator/raw/master/hash.exe) and place it in a folder on your system path, e.g. `System32`.

	C:\Windows\System32

To hash a folder/file, open Command Prompt and type `hash` followed by the path to the folder/file.

	hash C:\Some Folder\That I\Want To Hash

Both absolute and relative paths are supported. Spaces in the path can be parsed without issue so quotation marks are not necessary.

## Usage (Python Script)

Download [Python_SuperBLT_Hash_Calculator_v1.0.zip](https://github.com/fragtrane/Python-SuperBLT-Hash-Calculator/raw/master/Python_SuperBLT_Hash_Calculator_v1.0.zip). All of the functions are contained in `SuperBLT_Hasher.py`; the `testdata` folder only contains some testing data from the SuperBLT hashing library used to verify that the hashes are calculated correctly.

The `SuperBLT_Hash_Dir` function is used to calculate the SuperBLT hash of a folder and takes a path to a folder as its argument.

The `SuperBLT_Hash_File` function is used to calculate the SuperBLT hash of a file and takes a path to a file as its argument.

The `SuperBLT_Hash` function is only used internally for calculating SHA-256 hashes and does not need to be called directly.

## Acknowledgments

This is a Python implementation of the [SuperBLT hashing library](https://gitlab.com/SuperBLT/HashLib). The Java version was used as a reference. The testing data was taken from this library.

## Contact

Steam Group: [steamcommunity.com/groups/frag_pd2](https://steamcommunity.com/groups/frag_pd2)

Reddit: [/u/fragtrane](https://www.reddit.com/user/fragtrane)

## Changelog

**v1.0 - 2019-08-08**

Initial release.