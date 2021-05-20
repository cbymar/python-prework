import os
import time

def foo(x):
    x[0] = 99

mylist = [1,2,3]  # mutable

foo(mylist)
print(mylist)

def bar(x):
    x = x + 90

my_var = 3  # immutable
bar(my_var)
print(my_var)

##### Beware using a mutable as a default arg

def store_lower(_dict, _string):
    orig_string = _string  # points to an immutable object
    _string = _string.lower()  # changes that object; necessarily by creating a new object
    _dict[orig_string] = _string  #

d = {}
s = "Hello"

store_lower(d, s)
for k, v in d.items():
    print(k, v)
s = "HIYA"
store_lower(d, s)
s = "ByEEE"
store_lower(d, s)

print(s)
############################################
# context mgr. Use as _: to assign context to a var
"""
with <context-manager>():
    code running with that context
"""
# Create context manager:
import contextlib
@contextlib.contextmanager
def my_context():
    # setup code
    yield  # technically contextmgr is generator yielding a single value
    # teardown code

@contextlib.contextmanager
def database(url):
    db = postgres.connect(url)
    yield db
    db.disconnect

url = ""
with database(url) as my_db:
    course_list = my_db.execute(
        "SELECT * FROM arbitrary_table"
    )

@contextlib.contextmanager
def in_dir(somearbitrarypath):
    """Allows us to do something temporarily in a different path"""
    # save cwd
    old_dir = os.getcwd()
    os.chdir(somearbitrarypath)
    yield
    os.chdir(old_dir)

with in_dir("/Users/myname/"):
    files_in_that_dir = os.listdir()

###################
# example:
# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def acodetimer():
    """
    yields nothing (ie no var, just returns control for execution)
    """
    startcodeexecution = time.time()

    yield  # so that function can execute

    endcodeexecution = time.time()  # take timestamp again
    ### second format
    print('Elapsed: {:.7f}s'.format(endcodeexecution - startcodeexecution))

with acodetimer():
  print('Expect about 2 seconds')
  time.sleep(2.0005)

#################
@contextlib.contextmanager
def open_for_reading_only(filepathname):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  reading_only_file = open(filepathname, mode='r')
  yield reading_only_file
  reading_only_file.close()  # need to close to "exit" the context

with open_for_reading_only('my_file.txt') as my_file_to_read:
  print(my_file_to_read.read())
####################################################
# Nested context
# use nested with statements
# for error handling in a context manager, use try/except/finally
# try yield.
# youtu.be/cSbD5SKwak0
# open/close; lock/release; change/reset; enter/exit; start/stop; setup/teardown; connect/disconnect

###################
# Use the "stock('GE')" context manager
# and assign the result to the variable "generalelectric"
with stockprice("GE") as generalelectric:
    """pass the company to teh stockprice function """
    with open("ge.txt","w") as file_written_out:
        """Open "ge.txt" for writing as file_written_out"""
        for _ in range(10):
            value = generalelectric.price()
            print('Logging ${:.2f} for Thomas Edison Company'.format(value))
            file_written_out.write('{:.2f}\n'.format(value))

#####
def in_da_dir(directory):
    current_dir = os.getcwd()
    os.chdir(directory)

    try:
        yield  # switch to the directory
    finally:
        os.chdir(current_dir)

################
# Functions as objects -- decorators
import numpy as np
np.mean.__doc__

### See function definition if available
# import inspect
# print(inspect.getsource(arbitraryfunction))
############
# Closure arguments:
for _ in my_func.__closure__:
  print(_.cell_contents)

######### DEcorators
# wrapper to change function behavior by changing inputs, outputs, behavior
@double_args
def multiply(a, b):
    """gets args multiplied by 2 via the decorator"""
    return a * b

def double_args(func):
    def wrapper(a, b):
        """Wrapper does whatever we tell it to do"""
        return func(a*2, b*2)
    return wrapper

new_multiply = double_args(multiply)
new_multiply(1,5)

multiply = double_args(multiply)
multiply(3,7)
multiply.__closure__[0].cell_contents

####################
def decoratorfunc(func):
    def wrapper(*args,**kwargs):
        # anything before
        func(*args, **kwargs)  # any changes to make to func or args
        # anything after
    return wrapper

@decoratorfunc
def regular_func():
    pass

####
# https://campus.datacamp.com/courses/writing-functions-in-python/more-on-decorators?ex=1
def timer(func):
    """how long"""
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time - t_start
        print("{} took {:.3}".format(func.__name__, t_total))
        return result
    return wrapper

######################
# memoizing is useful for recursion.
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        """Check, assign result to the dict entry for that tuple of positional- & kw-args"""
        if (args, kwargs) not in cache:
            cache[(args, kwargs)] = func(*args, **kwargs)
        #### regardless of seen before or not, return computed result
        return cache[(args, kwargs)]  # this is the computed function result, added to the dict
    return wrapper

@memoize
def longrunning_function(a, b):
    time.sleep(3)
    return a + b

longrunning_function(1000, 1000)
longrunning_function(1001, 1002)

# https://campus.datacamp.com/courses/writing-functions-in-python/more-on-decorators?ex=2
def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result

    # Return the decorated function
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

############################
# maintaining metadata
from functools import wraps
# use @wraps to decorate the wrapper function.
# will return original function via __wrapped__ attr.
##############################
# adding arguments to decorators:
# create a decorator factory
def run_n_times(n):
    def decorator(func):
        """
        returns a wrapper function so that this functionality can be called
        the run_n_times returns this decorator function
        In other words, decorator is a closure, with function and n enclosed in its scope.
        And so is run_n_times; it has decorator in its scope
        """
        def wrapper(*args, **kwargs):
            """this wrapper effects the modified behavior; it is the returned value of decorator"""
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@run_n_times(3)
def print_sum(a, b):
    print(a+b)

###############
# Timeout decorator for long-running functions
import signal
def raise_timeout(*args, **kwargs):
    raise TimeoutError()

signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)
signal.alarm(5)

def timeout_in_5s(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        signal.alarm(5)
        try:
            return func(*args, **kwargs)
        finally:
            signal.alarm(0)
    return wrapper

def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.alarm(n_seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator






#### next up:
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/23961
# Use decorators to cut down on repeated code
# use @property to avoid writing getter setter methods
# Use context managers to maintain state:
# magic methods?

# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/23961
# youtube codereport
# cuDF, cuML, cuGraph   # CUDA allows gpu programming
# cuDF is modeled off pandas.

import reqeusts
import lxml.html as lh
import pandas as pd

# replace for & += 1 with enumerate
# "zip with index"
# avoid ITM.
# for T in tr_elements[1:]:   # step through slices of list.
# T.iterchildren()
# Ternary operator.
# data = int(data) if data.isnumeric() else data
# we can put the ternary statement into the statement of what we're doing with the result of the ternary expr.
# for loops can turn into list comps.
### He treats zip as a transpose function; which it basically is.
# Rapids -- fast training of model.  rapids.ai
# pythonbytes.
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
class Solution:

    def anag(self, x):
        ax = "".join(sorted(list(x)))
        return [ax, x]

    def groupAnagrams(self, strs):
        accumdict = dict()
        for _ in strs:
            anagx = self.anag(_)
            accumdict.setdefault(str(anagx[0]), []).append(str(anagx[1]))
        return list(accumdict.values())

solution = Solution()
solution.groupAnagrams(strs)
x = dict()
x.setdefault()

j = solution.anag("dinnertime")
j[0]
j[1]

x.setdefault(j[0],[]).append(j[1])
print(x)

strs = ["eat","tea","tan","ate","nat","bat"]
for _ in enumerate(strs):
    print(_)
##############################################################
#
%load_ext line_profiler

%lprun -f functionname function_call()

################################################################
# For memory footprint profiling
import sys
import memory_profiler
%load_ext memory_profiler
%mprun -f function function(args, listed, out)
# for mprun, the function must be imported from a file.

#######################################
# df.iterrows()  --> print(index and row)
# don't use iloc for iterating over rows.
# pandas rows are namedtuples; grab them using the .notation... unclear when spaces are present in names
#######################################
# apply for a fcn to a df.  remember to spec axis.

# use pandas df["colname"].values in arithmetic (takes advantage of np)
# range, enumerate, map, zip, itertools, collections, set
# np arrays, lprun, mprun,



