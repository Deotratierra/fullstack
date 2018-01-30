// Lo más común para empezar un proyecto es ejecutar:
npm init

/* Esto crea un archivo "package.json", el cual contiene
información sobre el proyecto, como el nombre, la descripción
o las bibliotecas a instalar. */

// Para instalar bibliotecas localmente en NodeJS y
// agregarlas al entorno de producción:
npm install --save biblioteca

// Para instalar bibliotecas localmente en NodeJS y
// agregarlas al entorno de desarrollo:
npm install --save-dev <biblioteca>

/* Los paquetes instalados se guardan en una carpeta llamada
"node_modules", en el mismo directorio desde el cual hemos
ejecutado el comando, que se crea automáticamente si no existe.*/

// Para buscar bibliotecas por tag
npm search tag_a_buscar

//==============================================================

// Dentro de un entorno virtual de nodeenv (ver capítulo "virtualenv"),
// para guardar las bibliotecas que hemos instalado en un archivo:
freeze ../prod-requirements.txt

// Para listar las bibliotecas del archivo:
freeze -l ../prod-requirements.txt

//==============================================================
