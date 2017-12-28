#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    
    from django.core.management import execute_from_command_line
    from django import setup as django_setup
    from django.core.management.commands.runserver import Command as runserver

    django_setup()

    from app import settings

    runserver.default_port = str(settings.PORT_SERVER)
    runserver.default_addr = settings.HOST_SERVER
    runserver.protocol = settings.PROTOCOL_SERVER
    

    execute_from_command_line(sys.argv)
