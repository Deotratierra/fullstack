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


exit 0