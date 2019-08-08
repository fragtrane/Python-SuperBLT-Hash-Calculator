#Python implementation of the SuperBLT hashing library
#v1.0

import hashlib
import os

#Calculate SHA-256
def SuperBLT_Hash(input_data, directory, BLOCKSIZE = 8192):
    hasher = hashlib.sha256()
    if directory:
        with open(input_data, 'rb') as file:
            buf = file.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(BLOCKSIZE)
    else:
        hasher.update(input_data)
    return hasher.hexdigest()

#Hash file, hash hash
def SuperBLT_Hash_File(file_path):
    hashed = SuperBLT_Hash(file_path, True)
    return SuperBLT_Hash(hashed.encode(), False)

#Hash files, join hashes (ordered by unicode value of directories), hash joined hashes
def SuperBLT_Hash_Dir(input_directory):
    hashes = dict()
    for r, d, f in os.walk(input_directory):
        for file in f:
            file_path = os.path.join(r, file)
            hashes[file_path.lower().encode('utf-8')] = SuperBLT_Hash(file_path, True)
    sorted_keys = sorted(hashes.keys())
    joined_hash = ""
    for key in sorted_keys:
        joined_hash = joined_hash + hashes[key]
    return SuperBLT_Hash(joined_hash.encode(), False)

print("Hashing file: testdata\\base\\base.lua")
print("Result:   " + SuperBLT_Hash_File(r"testdata\base\base.lua"))
print("Expected: " + "23a9bdaef72002c78411e8976d3d85e73be5c3fd977f78f0de53c6815cbe98e9")

print("")

print("Hashing directory: testdata\\base")
print("Result:   " + SuperBLT_Hash_Dir(r"testdata\base"))
print("Expected: " + "77f4d9e3804d345872315a6f0f2a4a19292e50c14a3887f9019fc60bd841a980")
