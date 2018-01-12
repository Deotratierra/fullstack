#!/usr/bin/ruby

require "net/smtp"

SENDER = ENV["EMAIL_SENDER"]
PASSWORD = ENV["EMAIL_PASSWORD"]

RECEIVER = ""
SUBJECT = "Email de prueba"
MESSAGE = "Esto es un email de prueba usando la biblioteca %s"

# ============================================================

# ---   OPCIÓN 1   --- net/smtp
# http://ruby-doc.org/stdlib-2.4.2/libdoc/net/smtp/rdoc/Net/SMTP.html

def send_net_smtp(sender, password, receiver, subject, message,
                  host="smtp.gmail.com", port=587, domain="gmail.com")
    _message = <<MESSAGE
From: <#{sender}>
To: <#{receiver}>
Subject: #{subject}

#{message}
MESSAGE

    begin
        smtp = Net::SMTP.new(host, port)
        smtp.enable_starttls
        smtp.start(domain, sender, password, :login) do
            smtp.send_message(_message, sender, receiver)
        end
    rescue Exception => e
        puts "Error enviando un mail con net_smtp"
        puts e.message  
        puts e.backtrace.inspect
    else
        puts "Email enviado correctamente con net_smtp"
    end
end

# ============================================================

# ---   OPCIÓN 2   --- sendgrid
# gem install sendgrid-ruby
# https://github.com/sendgrid/sendgrid-ruby

require 'sendgrid-ruby'
include SendGrid

SENDGRID_API_KEY = ENV["SENDGRID_API_KEY"]

def send_sendgrid(sender, api_key, receiver, subject, message)
    begin
        from = Email.new(email: sender)
        to = Email.new(email: receiver)
        content = Content.new(type: 'text/plain', value: message)
        mail = Mail.new(from, subject, to, content)
        
        sg = SendGrid::API.new(api_key: api_key)
        response = sg.client.mail._('send').post(request_body: mail.to_json)
    rescue Exception => e
        puts "Error enviando un mail con sendgrid"
        puts e.message  
        puts e.backtrace.inspect
    else
        puts "Email enviado correctamente con sendgrid"
    end
end

# ============================================================

if __FILE__ == $0
    send_net_smtp(SENDER, PASSWORD, RECEIVER, SUBJECT, MESSAGE % "net_smtp")
    send_sendgrid(SENDER, SENDGRID_API_KEY, RECEIVER, SUBJECT, MESSAGE % "sendgrid")
end
