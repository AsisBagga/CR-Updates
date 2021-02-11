import os
# Replacement Strings
replacement = """ Replacemenent string, make sure this is a multiline string and it ends on below line
"""
# Directory Path to which you want to replace line 0 with replacement string on ALL THE FILES!
dirr = "/root/my/directory"
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
