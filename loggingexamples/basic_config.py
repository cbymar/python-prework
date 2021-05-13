#!/usr/bin/env python

import logging

logging.basicConfig(filename="test.log",
	format="%(filename)s: %(message)s",
	level=logging.DEBUG)

logging.debug("This is just a debug message")
logging.info("This is an informational message; level is info.")
logging.warning("Warning message here")
logging.error("You made an error")
logging.critical("Critical message to read")
