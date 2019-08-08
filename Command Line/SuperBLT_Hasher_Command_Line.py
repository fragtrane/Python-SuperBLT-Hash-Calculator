import hashlib
import os
import sys

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

def SuperBLT_Hash_File(file_path):
    hashed = SuperBLT_Hash(file_path, True)
    return SuperBLT_Hash(hashed.encode(), False)

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

def main():
    args = sys.argv
    args = args[1:]
    if len(args) == 0:
        print("No path specified.")
        return
    elif len(args) == 1:
        file_path = args[0]
    else:
        file_path = " ".join(args)
    
    if not os.path.isabs(file_path):
        file_path = os.path.dirname(os.path.abspath(__file__)) + "\\" + file_path
    
    if not os.path.exists(file_path):
        print("Path does not exist.")
        return
    
    if os.path.isdir(file_path):
        print("BLT folder hash: " + SuperBLT_Hash_Dir(file_path))
    else:
        print("BLT file hash: " + SuperBLT_Hash_File(file_path))

if __name__ == '__main__':
    main()