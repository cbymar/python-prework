#!/usr/bin/env python

import logging
import logging.config
import yaml

with open("config.yaml", "r") as fileyaml:
	log_cfg = yaml.safe_load(fileyaml.read())

logging.config.dictConfig(log_cfg)

logger = logging.getLogger("dev")
logger.setLevel(logging.INFO)

logger.info("This is an info message to log")
logger.error("This is an ERROR message to log")



