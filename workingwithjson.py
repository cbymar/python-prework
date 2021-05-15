import json
import os
import pathlib
import requests
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-JSON/states.json"
r = requests.get(url)
open("./ignoreland/states.json","wb").write(r.content)
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["js@bogusbs.com","js@boguswp.com"],
            "has_license": false
        },
        {
            "name": "Jane Smith",
            "phone": "614-555-7164",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_string)
print(data)
print(type(data))

for person in data["people"]:
    print(person["name"])

new_string = json.dumps(data, indent=4)
print(new_string)

new_string = json.dumps(data, indent=4, sort_keys=True)
print(new_string)


with open("./ignoreland/states.json") as f:
    data=json.load(f)

for state in data["states"]:
    print(state["name"],state["abbreviation"])

#### Pulling from an API:
# the urlopen(hteurl) is the context manager (context); we call the .read() on that context
# and assign to a variable.  Then use json load-string function to convert to a dict.
urlhere = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
with urlopen(urlhere) as response:
    source = response.read()

data = json.loads(source)

#######################################################
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/23953
# file objects
f = open("./ignoreland/test.txt","r")
print(f.name)
f.close()  # eliminate leaks.
with open("./ignoreland/test.txt","r") as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    f_contents = f.readline()
    print(f_contents)

with open("./ignoreland/test.txt","r") as f:
    for line in f:
        print(line, end="")

with open("./ignoreland/test.txt","r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="|*|")
        f_contents = f.read(size_to_read)

# f.seek() goes to a given character position.
with open("./ignoreland/test2.txt", "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("R")

with open("./ignoreland/test.txt","r") as rf:
    with open("./ignoreland/test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

with open("./ignoreland/comic.png","rb") as rf:
    with open("./ignoreland/comic_copy.png", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

os.listdir("./ignoreland")
x = os.stat("./ignoreland/comic.png")
dir(x)
# from https://stackoverflow.com/questions/55638905/how-to-convert-os-stat-result-to-a-json-that-is-an-object
def stat_to_json(filepath: str) -> dict:
    stat_object = os.stat(filepath)
    return {k: getattr(stat_object, k) for k in dir(stat_object) if k.startswith("st_")}

for _ in ["comic", "comic_copy"]:
    print(stat_to_json("./ignoreland/" + _ + ".png")["st_size"])


