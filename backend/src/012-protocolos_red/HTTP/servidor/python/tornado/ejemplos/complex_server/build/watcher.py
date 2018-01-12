#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Autoreload file watcher"""

import os
import sys
from functools import partial
from subprocess import (Popen, PIPE)
import shlex
from pprint import pprint

import tornado.autoreload

class AutoreloadWatcher:
    """Autoreload file watcher"""
    def __init__(self, config):
        self.config = config
        self.watch_files()

    def watch_files(self):
        """Configure files to watch for autoreload
        in debug mode (development)"""
        watching_files = []
        if self.config.DEBUG:
            for folder in self.config.WATCH["folders"]:
                for tree in os.walk(folder):
                    subdir, files = (tree[0], tree[2])
                    for file in files:
                        if file.split(".")[1] in self.config.WATCH["extensions"]:
                            file = os.path.join(subdir, file)
                            tornado.autoreload.watch(file)
                            watching_files.append(file)

        if self.config.WATCH["hook_command"]:
            self.watch_autoreload_hook()

        if self.config.WATCH["debug"]:
            self.show_watching_files(watching_files)

    def watch_autoreload_hook(self):
        """Function to execute before autoreload"""
        def hook(command):
            """Hook function"""
            process = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE)
            while True:
                out = process.stdout.read(1).decode("utf-8", errors="ignore")
                if out == '' and process.poll() != None:
                    break
                if out != '':
                    sys.stdout.write(out)
                    sys.stdout.flush()
            
        command = self.config.WATCH["hook_command"]
        tornado.autoreload.add_reload_hook(partial(hook, command))

    def show_watching_files(self, files):
        """Show watching files if self.config.WATCH["debug"] == True"""
        print("\n=======   WATCHING FILES   =======\n")
        pprint(files)
        print("\n==================================\n")
