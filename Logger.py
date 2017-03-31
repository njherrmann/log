#!/usr/bin/env python

from __future__ import print_function

from style import STYLE
from datetime import datetime # Gets timestamps
from sys import stderr # Logger prints messages to stderr
  


class Logger(object):
  """A class that logs events for other python applications"""
  
  def __init__(self, name=None, file=stderr):
    """Makes a logger with a name that appears in message timestamps"""
    self.name = name if type(name) == str else None
    self.file = file


  def setFile(self, file):
    self.file = file
  
  
  def _timestamp(self):
    """Returns a header string containing the current timestamp and logger name"""
    return '[%s%s]' % (datetime.now().strftime("%H:%M:%S %Y-%m-%d"), (' ' + self.name) if self.name is not None else '')


  def debug(self, message):
    print(self._timestamp() + STYLE.GREEN+STYLE.BOLD + ' DEBUG  ' + STYLE.NORMAL + str(message), file=self.file)

  def info(self, message):
    print(self._timestamp() + STYLE.BLUE+STYLE.BOLD + ' INFO  ' + STYLE.NORMAL + str(message), file=self.file)

  def warning(self, message):
    print(self._timestamp() + STYLE.YELLOW+STYLE.BOLD + ' WARNING  ' + STYLE.NORMAL + str(message), file=self.file)

  def error(self, message):
    print(self._timestamp() + STYLE.RED+STYLE.BOLD + ' ERROR  ' + STYLE.NORMAL + str(message), file=self.file)

  def critical(self, message):
    print(self._timestamp() + STYLE.RED+STYLE.BOLD + ' CRITICAL  ' + STYLE.NORMAL + str(message), file=self.file)



if __name__ == '__main__':
  log = Logger()
  log.debug('this is a debug message')
  log.info('this is an info message')
  log.warning('this is a warning message')
  log.error('this is an error message')
  log.critical('this is a critical message')