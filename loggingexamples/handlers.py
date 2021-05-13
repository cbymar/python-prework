#!/usr/bin/env python

import logging

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)

fileHandler = logging.fileHandler("test.log")
fileHandler.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.info("This is an information message to be logged")
