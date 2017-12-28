#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Logger utils"""

import sys
import logging

import colorama
colorama.init(autoreset=True)

class ColorizedStreamHandler(logging.StreamHandler):
    """Colored outputs logging"""
    color_map = {
        logging.DEBUG: colorama.Style.DIM + colorama.Fore.LIGHTCYAN_EX,
        logging.INFO: colorama.Fore.WHITE,
        logging.WARNING: colorama.Fore.LIGHTYELLOW_EX,
        logging.ERROR: colorama.Fore.LIGHTRED_EX,
        logging.CRITICAL: colorama.Back.RED + colorama.Fore.WHITE +  colorama.Style.BRIGHT,
    }

    def __init__(self, stream=sys.stdout, color_map=None):
        logging.StreamHandler.__init__(self,
                                       colorama.AnsiToWin32(stream).stream)
        if color_map:
            self.color_map = color_map

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        if self.is_tty:
            # Don't colorize a traceback
            parts = message.split('\n', 1)
            parts[0] = self.colorize(parts[0], record)
            message = '\n'.join(parts)
        return message

    def colorize(self, message, record):
        try:
            return (self.color_map[record.levelno] + message)
        except KeyError:
            return message