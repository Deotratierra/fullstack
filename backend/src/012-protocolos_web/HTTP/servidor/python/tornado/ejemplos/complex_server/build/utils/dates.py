#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Date utils"""

from datetime import time, datetime, timedelta

def time_until_end_of_day(date=None):
    """Get timedelta until end of day on
    the datetime passed, or current time."""
    if date is None:
        date = datetime.now()
    tomorrow = date + timedelta(days=1)
    return datetime.combine(tomorrow, time.min) - date + timedelta(seconds=.01)
