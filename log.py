#!/usr/bin/env python

from Logger import Logger


# Active loggers are stored in a dictionary.
# If getLogger is called with the name of an active l
loggers = {}



def getLogger(name=None):
  if name not in loggers:
    loggers[name] = Logger(name)
  return loggers[name]
