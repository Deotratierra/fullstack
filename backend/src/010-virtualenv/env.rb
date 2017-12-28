#!/usr/bin/ruby

=begin

Con rbenv podemos instalar diferentes versiones de
Ruby en el ordenador y elegir que versión usar en
nuestros proyectos. Para instalarlo y conocer cómo
usarlo, podemos encontrar toda la información en:
https://github.com/rbenv/rbenv

=end

# ---- COMANDOS ÚTILES -----

# Para listar todas las versiones que podemos instalar:
rbenv install -list

# Para instalar una version:
rbenv install <version>

# Para establecer una versión globalmente en el sistema:
rbenv global <version>

# Para establecer una versión en el directorio local:
rbenv local <version>

# Para listar las versiones instaladas (con * la actual):
rbenv versions


