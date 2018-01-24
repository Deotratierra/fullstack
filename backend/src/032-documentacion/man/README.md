## El manual de Linux
Las páginas *man* (abreviatura de "páginas del manual") son una extensa documentación que viene preinstalada en casi todos los sistemas operativos derivados de UNIX más importantes.

El comando para mostrarlas es `man` y este suele ejecutarse junto a un comando o programa del cual queremos consultar información.

### Comandos
- Mostrar una página del manual: `man <página>`
- Mostrar una breve descripción de una página: `whatis <página>`
- Buscar por páginas del manual por expresión regular: `man -k <palabra>`. O también: `apropos <palabra>`
- Convertir página del manual a PDF: `man -t <página> | ps2pdf - <ruta/al/archivo.pdf>`

#### Colorear las páginas del manual
Añadir el siguiente código al archivo `~/.bashrc` y ejecutar `source ~/.bashrc`:

```
man() {
    env LESS_TERMCAP_mb=$'\E[01;31m' \
    LESS_TERMCAP_md=$'\E[01;38;5;74m' \
    LESS_TERMCAP_me=$'\E[0m' \
    LESS_TERMCAP_se=$'\E[0m' \
    LESS_TERMCAP_so=$'\E[38;5;246m' \
    LESS_TERMCAP_ue=$'\E[0m' \
    LESS_TERMCAP_us=$'\E[04;38;5;146m' \
    man "$@"
}
```

#### Traducir el manual a español
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install manpages-es manpages-es-extra
sudo dpkg-reconfigure locales
```

> Fuentes:
> - https://wiki.archlinux.org/index.php/Man_page_(Espa%C3%B1ol)
> - https://ubuntulife.wordpress.com/2011/03/01/poner-las-paginas-de-man-en-castellano/