"""
The email responder plugin.  This plugin sends emails whenever a testrun is created / finished.
"""
__author__ = 'jcorbett'

import configparser
import logging
import json

from ..amqp import AMQPConnection

from slickqa import SlickConnection, EmailSystemConfiguration, Testrun
from slickqa import micromodels
from kombu import Consumer, Queue
from kombu.transport.base import Message

class TestrunUpdateMessage(micromodels.Model):
    before = micromodels.ModelField(Testrun)
    after = micromodels.ModelField(Testrun)

class EmailResponder(object):
    """The email auto responder plugin"""

    def __init__(self, configuration, amqpcon, slick):
        assert(isinstance(configuration, configparser.ConfigParser))
        assert(isinstance(amqpcon, AMQPConnection))
        assert(isinstance(slick, SlickConnection))
        self.configuration = configuration
        self.amqpcon = amqpcon
        self.logger = logging.getLogger('narc.plugins.email.EmailResponder')
        self.logger.debug("Email Responder is gathering settings from slick.")
        self.slick = slick
        self.email_settings = self.slick.systemconfigurations(EmailSystemConfiguration).findOne()
        self.configured = False
        if self.email_settings is not None:
            assert(isinstance(self.email_settings, EmailSystemConfiguration))
            if self.email_settings.enabled:
                self.configured = True
                self.logger.debug("Recieved email settings: {}", self.email_settings.to_json())
            else:
                self.logger.info("Email responses have been disabled by email system configuration retrieved from slick.")

        if self.configured:
            self.channel = amqpcon.add_channel()
            self.queue = Queue('narc_testrun_email_response', exchange=amqpcon.exchange, routing_key='update.Testrun', durable=True)
            self.consumer = Consumer(self.channel, queues=[self.queue,], callbacks=[self.testrun_updated,])
            amqpcon.add_consumer(self.consumer)

    def testrun_updated(self, body, message):
        assert(isinstance(message, Message))
        if not message.acknowledged:
            message.ack()
        update = TestrunUpdateMessage.from_dict(body)
        if update.before.finished is False and update.after.finished is True:
            self.logger.info("Testrun with id {} and name {} just finished.", update.after.id, update.after.name)




