#!/usr/bin/ruby

# ====================================================================

#####   SUBPROCESO SIMPLE   #####

def simple_call(command)
    begin
        system(command)
    rescue Exception => e
        puts e.message  
        puts e.backtrace.inspect
    end
end

# ====================================================================

#####   SUBPROCESO CON SALIDA   #####
# http://www.rubydoc.info/stdlib/core/IO.popen

def stdout_call(command)
    begin
        IO.popen(command) do |pipe|
            $response = pipe.gets
        end
    rescue Exception => e
        puts "Error recogiendo la salida del comando %s" % command
        puts e.message  
        puts e.backtrace.inspect
        return
    end

    if (not $response)
        puts "Error recogiendo la salida del comando %s" % command
        return
    end
    return $response
end

# ====================================================================

if __FILE__ == $0
    puts simple_call("date") # true
    puts stdout_call("date")

end
