#!/usr/bin/env python

import logging

main_logger = logging.getLogger('main')
main_logger.setLevel(5)

dev_logger = logging.getLogger('main.dev')

print(main_logger.getEffectiveLevel())
print(dev_logger.getEffectiveLevel())



