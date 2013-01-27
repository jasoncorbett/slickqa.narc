"""
The email responder plugin.  This plugin sends emails whenever a testrun is created / finished.
"""
__author__ = 'jcorbett'

import configparser
import logging

from ..amqp import AMQPConnection

class EmailResponder(object):
    """The email auto responder plugin"""

    def __init__(self, configuration, amqpcon):
        assert(isinstance(configuration, configparser.ConfigParser))
        assert(isinstance(amqpcon, AMQPConnection))
        self.configuration = configuration
        self.amqpcon = amqpcon
        self.logger = logging.getLogger('narc.plugins.email.EmailResponder')
        self.logger.debug("Email Responder initialized with amqp connection url {}", amqpcon.url)

