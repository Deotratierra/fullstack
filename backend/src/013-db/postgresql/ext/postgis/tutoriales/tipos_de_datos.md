## Tipos de datos en PostGIS

Los objetos GIS soportados por PostGIS son un superset de las características simples definidas por el Consorcio OpenGIS (OGC), pudiendo trabajar con todos los objetos y funciones expecificados en el documento de especificación [Simple Feature Access](http://www.opengeospatial.org/standards/sfs), aunque PostGIS extiende el estándar para soportar `3DZ`, `3DM` y coordenadas `4D`.

### OpenGIS WKB y WKT
La especificación OpemGIS define dos formas estándar de expresar objetos espaciales: la forma *Well-Known Text* (WKT) y la *Well-Known Binary* (WKB). Ambas incluyen información sobre el tipo de objeto y las coordenadas que forman dicho objeto.

Ejemplos de representaciones de texto (WKT) de las características de los objetos espciales son las siguientes:

- `POINT(0 0)`
- `LINESTRING(0 0,1 1,1 2)`
- `POLYGON((0 0, 4 0,4 4,0 0),(1 1,2 1,2 2,1 2,1 1))`
- `MULTIPOINT((0 0),(1 2))`
- `MULTILINESTRING((0 0,1 1,1 2),(2 3,3 2,5 4))`
- `MULTIPOLYGON(((0 0,4 0,4 4,0 4,0 0),(1 1,2 1,2 2,1 2,1 1)), ((-1 -1,-1 -2,-2 -2,-2 -1,-1 -1)))`
- `GEOMETRYCOLLECTION(POINT(2 3),LINESTRING(2 3,3 4))`
