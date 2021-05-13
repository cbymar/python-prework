#!/usr/bin/env python

import logging

"""When we set exc_info to true, the stack trace is included."""

log_format = "%(asctime)s %(filename)s: %(message)s"
logging.basicConfig(filename="test.log", format=log_format)

vals = [1, 2]

try:
	print(vals[4])

except Exception as e:
	logging.error("an exception occurred", exc_info=True)


