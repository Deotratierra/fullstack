#!/usr/bin/ruby

require 'csv'

# ====================================================

#####   CREAR ARCHIVOS CSV   #####

CSV.open('fichero.csv', 'w') do |csvfile|
    csvfile << ["campo1", "campo2", "campo3"]
    csvfile << ["hola", 8, "valorfinal"]
end

# ====================================================

#####   LEER ARCHIVO CSV   #####

$count, $content = 0, []
CSV.foreach('fichero.csv', col_sep: ',', converters: :numeric) do |row|
    if ($count == 0)
        $headers = row.inspect
    else
        $content.push(row.inspect)
    end
    $count += 1
end

puts $headers, $content

# ====================================================


=begin
Fuentes:
https://www.sitepoint.com/guide-ruby-csv-library-part/
http://ruby-doc.org/stdlib-2.0.0/libdoc/csv/rdoc/CSV.html
=end
