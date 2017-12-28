#!/usr/bin/ruby

require "mongo"  # gem install mongo

USER, PASSWORD = "", ""
HOST, PORT = "", ""

DATABASE_NAME = ""
BASE_URI = ""

client = Mongo::Client.new("mongodb://%s:%s@%s:%d/%s" % [USER, PASSWORD, HOST, PORT, DATABASE_NAME])

db = client.DATABASE_NAME

=begin
Modelo de ruta en mlab.com:

mongodb://<dbuser>:<dbpassword>@ds119395.mlab.com:19395/<dbname>

------------------------------------------------

Ejemplo de conexión para la ruta anterior:

USER, PASSWORD = <dbuser>, <dbpassword>
HOST, PORT = "ds119395.mlab.com", 19395
DATABASE_NAME = <dbname>
=end

# =====================================================

=begin
Fuente:
https://docs.mongodb.com/ruby-driver/master/quick-start/
=end
