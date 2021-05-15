import requests
import json

r = requests.get("https://xkcd.com/353/")
print(r)
dir(r)
print(r.text)

r = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("./ignoreland/comic.png", "wb") as f:
    f.write(r.content)

print(r.status_code)
print(r.headers)

payload = {"page":2, "count": 25}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.url)

payload = {"username": "bill", "password": "testpw"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.url)
print(r.json())
r_dict = r.json()
print(r_dict["form"])
# look for timing out
r = requests.get("https://httpbin.org/delay/6",
                 timeout=3)

############################################################
# Pathlib tutorial
# os.path
# glob
# shutil
"""
Path, PosixPath, PurePosixPath, PureWindowsPath
"""

import pathlib
import os
import glob
dir(pathlib)

os.getcwd()
pathlib.Path.cwd()
os.path.expanduser("~")

os.environ["HOME"]
os.path.abspath("./ignoreland")

os.mkdir("./ignoreland/notes")
os.listdir(os.path.join("ignoreland"))
pathlib.Path("./ignoreland/notes").touch("anote.txt")
os.listdir(os.path.join("ignoreland","notes"))

all_dir = glob.glob("/Users/christophermartin/DocumentsNoCloud/*.txt")
for file in all_dir:
    print(file)

for root, subdir, files in os.walk(os.path.join(os.path.expanduser("~"))):
    for f in files:
        if f.endswith(".txt"):
            print(f)

# exists
# isdir
os.path.isdir("ignoreland")

# shutil.move()





