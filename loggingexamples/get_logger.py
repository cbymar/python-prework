#!/usr/bin/env python

import logging
import sys

"""
Creates a new logger using getLogger()
Requires a handler for the output file and a format
This new logger is called main, and I set the level to DEBUG
And I add custom messages for each level of the logger.  
"""

main = logging.getLogger("main")
main.setLevel(logging.DEBUG)

handler = logging.FileHandler("my.log")

format = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
handler.setFormatter(format)

main.addHandler(handler)

main.info("info message")
main.critical("a critical message")
main.debug("just a debug message")
main.warning("a warning message")
main.error("an error")
