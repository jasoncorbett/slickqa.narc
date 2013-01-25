"""
The main program for narc.  This contains both the daemon's main, and the control script main.
"""
__author__ = 'jcorbett'

import sys
import argparse
import configparser
import logging

from . import configuration
from . import amqp
from slickqa import SlickConnection

restart = False
keep_going = True

def validate_slick_connection(slick):
    assert(isinstance(slick, SlickConnection))

def validate_amqp_connection(amqpcon):
    assert(isinstance(amqpcon, amqp.AMQPConnection))

def initialize_logging(configuration):
    assert(isinstance(configuration, configparser.ConfigParser))
    logfile = configuration['Logging'].get('logfile', '/var/log/narc.log')
    level = configuration['Logging'].get('level', 'DEBUG')
    stdout = configuration['Logging'].getBoolean('stdout', False)
    format = configuration['Logging'].get('format', '[{process:<6}|{asctime}|{levelname:<8}|{name}]: {message}')
    dateformat = configuration['Logging'].get('dateformat', '%x %I:%M:%S %p')
    handlers = []
    if stdout:
        handlers.append(logging.StreamHandler())
    logging.basicConfig(filename=logfile, level=level, format=format, datefmt=dateformat, handlers=handlers)

def setup(options):
    """This method gets everything ready.  It loads configuration, initializes logging, initializes the connection
    to slick and the amqp broker.

    Note that it does not validate the slick or amqp connection, only sets up the configuration.
    """

def main(args=sys.argv):
    # parse command line
    parser = argparse.ArgumentParser(description="respond to slick events.")
    parser.add_argument('-c', '--config', )
    # sub main:
    #   load configuration
    #   configure logging
    #   initialize connection
    #   load plugins
    #   while not stop:
    #     connection.drain_events(timeout)
    pass

def ctlmain(args=sys.argv):
    pass
