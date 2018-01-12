#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Logger configuration file"""

import os
import logging
from time import time
from datetime import datetime

import tornado.log

from utils.dates import time_until_end_of_day
from utils.loggers import ColorizedStreamHandler

DEFAULT_FORMAT = "%(asctime)s - %(levelname)-8s  %(name)s:%(lineno)d -> %(message)s"
DEFAULT_FORMATTER = logging.Formatter(DEFAULT_FORMAT)

class Logger:
    """Multiple loggers configuration class"""
    tornado_loggers = ["access", "application", "general"]
    custom_loggers = ["database"]

    def __init__(self, config, loop):
        self.config = config
        self.loop = loop

        self.all_logger_names = self.tornado_loggers + self.custom_loggers
        self.all_loggers = []
        
        self._initialize_log_dirs()
        self.set_loggers()
        tornado.log.enable_pretty_logging()
    
    
    def _initialize_log_dirs(self):
        """Creates access, application, general and custom
        directories inside config.LOGS_DIR if doesn't exists"""
        if not os.path.exists(self.config.LOGS_DIR):
            os.mkdir(self.config.LOGS_DIR)

        for logger_name in self.all_logger_names:
            logger_dir = os.path.join(self.config.LOGS_DIR, 
                                      logger_name)
            if not os.path.exists(logger_dir):
                os.mkdir(logger_dir)

    def set_loggers(self):
        """Initialize all loggers"""

        def config_logger(logger_dir, logger):
            """Add handlers and set level for all loggers"""

            # Console handler
            consoleLog = ColorizedStreamHandler()
            consoleLog.setLevel(self.log_level)
            consoleLog.setFormatter(DEFAULT_FORMATTER)
            logger.addHandler(consoleLog)

            # File handler
            filename = self.today_formatted_date() + ".log"
            filepath = os.path.join(self.config.LOGS_DIR, 
                                    logger_dir, filename)
            fileLog = logging.FileHandler(filepath)
            fileLog.setLevel(self.log_level)
            logger.addHandler(fileLog)

            # Logger
            logger.setLevel(self.log_level)
            logger.propagate = False

            return logger

        for logger_dir in self.all_logger_names:
            logger_name = "tornado.%s" % logger_dir if \
                logger_dir in self.tornado_loggers else logger_dir
            logger = config_logger(logger_dir, 
                                   logging.getLogger(logger_name))
            setattr(self, logger_dir, logger)
            self.all_loggers.append(logger)

    @staticmethod
    def today_formatted_date():
        """Return formatted date year-month-day
        to name loggers"""
        now = datetime.now()
        return "{}-{}-{}".format(now.year, now.month, now.day)
    
    @property
    def log_level(self):
        """Return application log level
        (DEBUG if config.DEBUG else INFO)"""
        return logging.DEBUG if self.config.DEBUG else logging.INFO

    def schedule_loggers_filename_updates(self):
        """Calculates next update for change logger filename tomorrow"""
        next_day = datetime.fromtimestamp(self.loop.time()) + time_until_end_of_day()
        self.loop.call_at(next_day.timestamp(), 
                          self.update_loggers_filenames)

    def update_loggers_filenames(self):
        """Callback for update logger filename everyday"""
        for logger in self.all_loggers:
            filename = self.today_formatted_date() + ".log"
            logger_dir = logger.name.split(".")[1] if "." in logger.name \
                else logger.name       # Tornado \ Custom logger
            filepath = os.path.join(self.config.LOGS_DIR, logger_dir, filename)
            self.logger.handler = logging.FileHandler(filepath)
        self.schedule_logger_filename_update(self.loop.time())