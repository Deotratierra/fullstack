### Autoenv
"""Si queremos iniciar el entorno automáticamente cada vez que 
entremos en el directorio raíz del proyecto, instalamos autoenv: 
```bash
pip3 install autoenv
echo "source `which activate.sh`" >> ~/.bashrc       # Al menos en Linux
```

- Código Bash para prevenir que autoenv se ejecute en cada subdirectorio de tu proyecto:
```bash
if [ "$(pwd)" == "<RUTA_AL_DIRECTORIO_RAÍZ_DE_TU_PROYECTO>" ]; then
    ... Inicialización del entorno, variables ...
fi
```

>Fuentes:
https://github.com/kennethreitz/autoenv
https://github.com/kennethreitz/autoenv/issues/63