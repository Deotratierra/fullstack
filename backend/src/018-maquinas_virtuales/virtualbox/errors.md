## Errores comunes

### Fallo al cambiar de dispositivo de almacenamiento
Mensaje de error:
```
Cannot register the hard disk "..." {ca2bdc6a-a487-4e57-9fcd-509d0c31d86d} because a hard disk "..." with UUID {ca2bdc6a-a487-4e57-9fcd-509d0c31d86d} already exists.
```

- Solución: `vboxmanage internalcommands sethduuid "</ruta/al/archivo/de/nuestro/dispositivo/de/almacenamiento/virtual.ext>"`

>Tras ejecutar el comando anterior debe aparecer: `UUID changed to: ...`

_________________________________________________