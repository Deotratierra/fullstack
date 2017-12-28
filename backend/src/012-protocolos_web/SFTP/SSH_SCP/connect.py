#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip3 install paramiko
from paramiko import SSHClient, AutoAddPolicy, WarningPolicy

conn = SSHClient()
conn.set_missing_host_key_policy(AutoAddPolicy())

class SSH:
    """Conexión con una máquina remmota mediante SSH"""
    def __init__(self, username, password, address):
        conn.connect(address,username=username, 
                              password=password)
        self.ssh = conn

    def execute(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return (stdout.readlines(), stderr.readlines())

class SFTP:
    """Conexión con una máquina remota mediante SFTP"""
    def  __init__(self, username, password, address):
        conn.connect(address,username=username,
                              password=password)
        self.ftp = conn.open_sftp()

    def upload(self, filepath_in, filepath_out):
        self.ftp.put(filepath_in, filepath_out)
        return True

    def download(self, filepath_in, filepath_out):
        self.ftp.get(filepath_in, filepath_out)
        return True