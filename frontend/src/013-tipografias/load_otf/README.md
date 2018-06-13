## Cómo cargar fuentes

Para cargar una fuente usamos el selector `@font-face` en CSS. Con este indicamos tanto la ruta de la fuente como el nombre de la familia:

```css
@font-face {
  font-family: "Nombre de la fuente";
  font-style: normal;
  font-weight: normal;
  src: url("ruta/al/archivo/de/fuente.otf") format("opentype");
}

body {
  font-family: "Nombre de la fuente", serif;
}
```