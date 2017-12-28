# Utilidades para SublimeText

## Instalar-desinstalar (Ubuntu/Debian):
Instalar:
```sh
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```
>Fuente oficial: https://www.sublimetext.com/docs/3/linux_repositories.html


Desinstalar: `sudo apt-get remove sublime-text`


## Atajos de teclado (Ubuntu/Debian):
- Abrir el control de paquetes: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P<kbd>
- Renderizar markdown en HTML: <kbd>F7</kbd>

_________________________________________________________

## Plugins

Instalar plugins: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P<kbd> --> `**Package Control**: Install Package`

__________________________

### Emmet
Sirve para escribir HTML y CSS más rápido. [Referencia de comandos](https://docs.emmet.io/cheat-sheet/).

##### Comandos básicos
Hay que pulsar la tecla <kbd>Tab</kbd> después de cada comando:

- Estructura HTML5: `html5`
- Clases: `div.container`
- Ids: `div#container`
- Elementos anidados: `nav>ul>li`
- Elementos uno tras otro: `div+p+ul`
- Link CSS:  `link:css`
- Script / (con src): `script` / `script:src`
- Atributos personalizados: `[a='value1' b="value2"]`
- Texto dentro de etiquetas: `a{Click aquí}`

____________________________

### JSFormat
Sirve para formatear el código Javascript y JSON. Para usarlo, pulsar <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>
____________________________

### JSHint
Muy útil, sirve para resaltar los errores en el código Javascript. 

#### Comandos:
- Resalto de errores: <kbd>Alt</kbd> + <kbd>J</kbd> (Linux) o <kbd>Ctrl</kbd> + <kbd>J</kbd> (Windows).
- Saltar al próximo error: <kbd>F4</kbd>
- Volver al error anterior: <kbd>Shift</kbd> + <kbd>F4<kbd>

__________________________

### GitGutter
Muestra pequeños iconos junto a los números de línea mostrando las diferencias con el último commit para Git.

__________________________
