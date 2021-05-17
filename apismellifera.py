import urllib
import requests
from urllib.request import urlretrieve
import pandas as pd

url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
urlretrieve(url, "red.csv")
df = pd.read_csv('red.csv', sep=';')


#################
pd.DataFrame.hist(df.iloc[:, :1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
####################################################
#
from bs4 import BeautifulSoup
import requests
url = ""
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
# find_all()
for link in soup.find_all("a"):
    print(link.get("href"))
##################
# query string: ?a=avalue

# https://gist.github.com/hugobowne/18f1c0c0709ed1a52dc5bcd462ac69f4
# Initialize Stream listener
listen = MyStreamListener() # from gist definition

# Create your Stream object with authentication
stream = tweepy.Stream(auth, listen)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(["clinton", "sanders", "obama"])

#######################################################################
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = "tweets.txt"

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)  # in-place

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
###################################################################
# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=["text", "lang"])

# Print head of DataFrame
print(df.head())

## XML
import xml.sax
class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        # print(name)
        if self.current == "person":
            print("-----PERSON------")
            print("ID: {}".format(attrs["id"]))

    def characters(self, content):
        """if dealing with a tag that's a name, set to content of item """
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = current

    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))

        elif self.current == "age":
            print("Age: {}".format(self.age))

        elif self.current == "weight":
            print("Weight: {}".format(self.weight))

        elif self.current == "height":
            print("Height: {}".format(self.height))
        self.current = ""

import xml.dom.minidom
# parse xml with dom model
domtree = xml.dom.minidom.parse("data.xml")
group = domtree.documentElement

persons = group.getElementByTagName("person")

for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute("id"):
        print("ID: {}".format(person.getAttribute("id")))
    print("Name: {}".format(person.getElementsByTagName("name")[0].childNodes[0].data))

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setConentHandler(handler)
parser.parse("data.xml")

