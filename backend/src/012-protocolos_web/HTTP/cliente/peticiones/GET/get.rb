#!/usr/bin/ruby

require "json"

URL = "https://min-api.cryptocompare.com/stats"

# ========================================================
# ---------- SÍNCRONA ------------------------------------ net/http

require "net/http"

def net_http_GET(url)
    url = URI(url)
    begin
        response = Net::HTTP.get_response(url)
    rescue Exception => ex
        puts ex
    else
        if (response.code != "200")
            puts "Error en la petición GET síncrona con net/http."
            puts "Status code == %s" % response.code
            return      
        end
        return response
    end
end

# =======================================================
# ---------- SÍNCRONA ------------------------------------ httparty
# gem install httparty

require "httparty"

def httparty_GET(url)
    begin
        response = HTTParty.get(url)
    rescue Exception => ex
        puts ex
    else
        if (response.success?)
            return response.parsed_response  # <--- En JSON
        else
            puts "Error en la petición GET síncrona con net/http."
            puts "Status code == %s" % response.success?
        end
    end
end


# =======================================================

if __FILE__ == $0
    puts net_http_GET(URL)
    puts httparty_GET(URL)
end

=begin
Fuentes:
http://ruby-doc.org/stdlib-2.4.2/libdoc/net/http/rdoc/Net/HTTP.html
https://stackoverflow.com/questions/6279956/ruby-exceptions-why-else
https://www.twilio.com/blog/2015/10/4-ways-to-parse-a-json-api-with-ruby.html
https://github.com/jnunemaker/httparty
=end
