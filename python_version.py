import os
import time

files = []

for f in os.listdir("."):
    if f.startswith("."):
        continue
    if not os.path.isfile(f):
        continue

    stat = os.stat(f)

    # On macOS: st_birthtime gives creation time
    created = getattr(stat, "st_birthtime", stat.st_mtime)

    files.append((f, created))

files.sort(key=lambda x: x[1])

for i, (name, _) in enumerate(files, start=1):
    base, ext = os.path.splitext(name)
    newname = f"{i}{ext}"

    if name != newname:
        os.rename(name, newname)
