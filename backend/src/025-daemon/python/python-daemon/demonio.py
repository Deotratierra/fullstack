#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from daemon import DaemonContext
import sys

sys.stdout.mode = "w+"
sys.stderr.mode = "w+"

with DaemonContext(stdout=sys.stdout):
    print("Hola")