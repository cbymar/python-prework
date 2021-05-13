import logging

####
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/23950
log = logging.getLogger("mylogger")
log.info("Nice to know: %s", value)
logging.warning("warning message")
log.exception("OH NO!")
log.debug("the %(counter)d item is %(item)s.",
          {
              "counter": cnt,
              "item": item,
          })

# Logger, LogRecord, Handler, Formatter
# Root logger
# Simple config options are available.  Idea is we can do it very simply.



