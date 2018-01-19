#!/bin/bash

# =======================================================================

: '
Para colorear las salidas en Bash, se usan las secuencias de escape ANSI.
Estas secuencias son a menudo representadas con los caracteres "^[" o "<Esc>",
seguida de otros caracteres. En Bash, el caracter <Esc> se puede obtener
mediante las sintaxis: "\e", "\033" y "x1B".

Para eliminar todos los atributos de formateo se usa: \e[0m
Es útil colocarlo al final de cada sentencia, así los atributos no
seguiran afectando a todo el aspecto de la terminal.

Para parsear las secuencias de escape al mostrar caracteres en Bash se usa:
echo -e

Ejemplos:
'
echo -e "Normal \e[1mNegrita\e[0m"

echo -e "\e[38;5;11m¡\e[38;5;33mHola \e[38;5;199mmundo \e[38;5;118mcoloreado\e[38;5;11m!\e[0m"

: '
Lista completa de secuencias de formateo
https://misc.flogisoft.com/bash/tip_colors_and_formatting
'

# ========================================================================

# Colores

bold=$(tput bold)
underline=$(tput sgr 0 1)
reset=$(tput sgr0)

purple=$(tput setaf 171)
red=$(tput setaf 1)
green=$(tput setaf 76)
tan=$(tput setaf 3)
blue=$(tput setaf 38)


# Cabeceros y logging

e_header() { printf "\n${bold}${purple}==========  %s  ==========${reset}\n" "$@" 
}
e_arrow() { printf "➜ $@\n"
}
e_success() { printf "${green}✔ %s${reset}\n" "$@"
}
e_error() { printf "${red}✖ %s${reset}\n" "$@"
}
e_warning() { printf "${tan}➜ %s${reset}\n" "$@"
}
e_underline() { printf "${underline}${bold}%s${reset}\n" "$@"
}
e_bold() { printf "${bold}%s${reset}\n" "$@"
}
e_note() { printf "${underline}${bold}${blue}Note:${reset}  ${blue}%s${reset}\n" "$@"
}

# --------------------------------------

# Ejemplos de uso

e_header "Soy un cabecero de ejemplo"
e_success "Soy un mensaje de éxito"
e_error "Soy u mensaje de error"
e_warning "Soy un mensaje de advertencia"
e_underline "Soy un texto subrayado"
e_bold "Soy un texto en negrita"
e_note "Soy una nota"

# ==================================================================
