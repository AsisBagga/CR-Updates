import os
# Replacement Strings
replacement = """ 
    This the the string we wish to replace in all the files. 
    Please make sure this is a multiline string and it ends on below line.
"""

# Directory Path to which you want to replace line 0 with replacement string in all the file in the directory.
dirr = "/root/my/directory"

def any(dirr)
    for dname, dirs, files in os.walk(dirr):
        for fname in files:
            fpath = os.path.join(dname, fname)
            og = ""
            with open(fpath, "r") as f:
                r = f.readlines()
                og = r[0]

            with open(fpath, 'r+') as f:
                contents = f.read().replace(og, replacement)
                f.seek(0)
                f.truncate()
                f.write(contents)
                f.close()
if __name__ == '__main__':
    any(dirr)
