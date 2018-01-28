#!/bin/bash

# ====================================================================
                    #     LIMPIEZA     #

# Borramos los archivos de cache
echo "Eliminando los archivos de cache..."
bash scripts/clean/delete_cache_files.sh
if [ $? -gt 0 ]; then
  echo "Error eliminando los archivos de cache."
  exit 1
fi
echo "Eliminados"
echo


# ====================================================================
                #     INFORMACIÓN DEL PROYECTO     #

# Creamos los archivos de metadatos del proyecto
echo "Actualizando los archivos de metadatos..."
python3 scripts/stats/backend_lang_files_perc_chart.py metadata/assets/imgs/backend_lang_files_perc.png
if [ $? -gt 0 ]; then
  echo "Error actualizando los archivos de metadatos."
  exit 1
fi
echo "Metadatos actualizados"
echo

: '
# Obtenemos las urls a checkear en un archivo para testearlas
echo "Obteniendo las urls de todos los archivos del proyecto..."
python3 scripts/checking/extract_urls.py backend/src metadata/assets/data/urls_to_check.json
if [ $? -gt 0 ]; then
  echo "Error obteniendo las urls."
  exit 1
fi
echo "Urls obtenidas"
echo


# ====================================================================
                      #     TESTING     #

# Testeamos todas las urls
echo "Comprobando que todos los links se encuentran en funcionamiento..."
python3 scripts/checking/broken_links.py metadata/assets/data/urls_to_check.json metadata/assets/data/urls_broken.json
if [ $? -gt 0 ]; then
  echo "Error comprobando si los links se encuentran en funcionamiento."
  exit 1
fi

                #     INFORMACIÓN DEL TESTEO     #

python3 scripts/stats/broken_links_advice.py
if [ $? -gt 0 ]; then
  echo "Error notificando la cantidad de links caídos en el README.md principal."
  exit 1
fi
echo
echo "Cantidad de links caídos notificada en el archivo README.md principal."
echo
'
# ====================================================================

exit 0