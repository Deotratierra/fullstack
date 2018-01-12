#!/usr/bin/ruby

require "net/ssh"  # gem install net-ssh
require "net/sftp" # gem install net-sftp

class SSH
    def initialize(username, password, address)
        @ssh = Net::SSH.start(address, username, :password => password)
    end

    def execute(command)
        output = @ssh.exec!(command)
    end
end

class SFTP
    def initialize(username, password, address)
        @sftp = Net::SFTP.start(address, username, :password => password)
    end

    def upload(filepath_in, filepath_out)
        @sftp.upload!(filepath_in, filepath_out)
    end

    def download(filepath_in, filepath_out)
        @sftp.download!(filepath_in, filepath_out)
    end
end

=begin
Fuentes:
https://github.com/net-ssh/net-ssh
https://github.com/net-ssh/net-sftp

=end
