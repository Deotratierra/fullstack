#!/bin/ruby

require 'mysql2'  # gem install mysql2

USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = 3306
DATABASE_NAME = ""

begin
    con = Mysql2::Client.new(:host => HOST, :port => PORT,
                             :username => USER, :password => PASSWORD,
                             :database => DATABASE_NAME)
    puts con
rescue Mysql2::Error => e
    puts e.errno
    puts e.error
ensure
    con.close if con
end

=begin
Fuentes:
http://zetcode.com/db/mysqlrubytutorial/
http://www.rubydoc.info/gems/mysql2/0.4.9
=end
