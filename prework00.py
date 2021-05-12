

########################################################
# Running through exercises listed in the prework
def product(a, b):
    """Return product of a and b."""
    return a*b


def weekday_name(day_of_week):
    mapdict = {"1": "Sunday",
               "2": "Monday",
               "3": "Tuesday",
               "4": "Wednesday",
               "5": "Thursday",
               "6": "Friday",
               "7": "Saturday",
               }
    if day_of_week in range(1,8):
        return mapdict[str(day_of_week)]
    else:
        return None
weekday_name(7)

# Ref this question for pythonic way of doing it:
# https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
def last_element(lst):
    if lst:
        return lst[-1]
    else:
        return None

last_element([1, 2, 3])
last_element([]) is None

###################################################
# 04
def number_compare(a, b):
    outdict = {
        "opta":'Numbers are equal',
        "optb":'Second is greater',
        "optc":'First is greater',
    }
    if a == b:
        key = "opta"
    elif a < b:
        key = "optb"
    else:
        key = "optc"
    return outdict[key]

number_compare(1, 2)
##################################
def reverse_string(phrase):
    return "".join(sorted(phrase,reverse=True))

reverse_string("hallo")
######################
def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?"""
    return word.lower().count(letter.lower())

single_letter_count("HelLo World", 'L')
########################
from collections import Counter
def multiple_letter_count(phrase):
    """Frequency dict of letters"""
    pcount = Counter(phrase)
    pcd = dict(pcount)
    return pcd

multiple_letter_count("alPhAbeTTat")
############################
# Skip 08_list_maniulation

############################
# palindrome
def is_palindrome(phrase):
    """returns true or false"""
    len2 = len(phrase) / 2
    firsthalf = phrase[leng::-1]
    secondhalf = phrase[leng::1]
    print(leng, firsthalf, secondhalf)

is_palindrome("glenelg")
is_palindrome("steponnopets")


# phrase = "steponnopets"
phrase = "glenelg"
len2 = len(phrase) / 2
bineven = len(phrase) % 2 == 0
firsthalf = phrase[int(len2)-bineven::-1]
secondhalf = phrase[int(len2)::1]
print(len2, firsthalf, secondhalf)

def ispalwalker(phrase):
    len2 = len(phrase) / 2
    for _ in range(int(len2)):
        yield phrase[_] == phrase[-(_+1)]

def ispal(phrase):
    for i, _ in enumerate(ispalwalker(phrase)):
        if _ == True:
            continue
        elif _ == False:
            print("element " + str(i))
            return False
    return True

ispal("stepoinniopets")

####################
def outer():
    n = 1

    def inner():
        nonlocal n
        n = 2
        print(n)
    inner()
    print(n)

outer()
