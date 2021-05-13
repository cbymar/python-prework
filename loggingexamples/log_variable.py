#!/usr/bin/env python

import logging

root = logging.getLogger()
root.setLevel(logging.INFO)

log_format = "%(asctime)s %(filename)s: %(message)s"
logging.basicConfig(filename="test.log",
	format=log_format)

# When an incident happens:

error_message = "authentication failed"

root.error(f"error: {error_message}")
