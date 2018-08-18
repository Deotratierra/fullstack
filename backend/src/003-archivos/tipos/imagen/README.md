## Formatos de imagen

- [Introducción a los formato de imagen](https://github.com/mondeja/fullstack/tree/master/backend/src/003-archivos/tipos/imagen/formats/intro.md)

### Utilidades

#### `.gif`
- [Conversor `.mp4` a `.gif`](https://mp4togif.online/es/)
- [Recortar `.gif`](http://gifgifs.com/es/crop/)

______________________


### Resolución de una imagen

La resolución de una imagen nos da información de la cantidad de píxeles que la describen. Se suele medir en píxeles por pulgada (ppi del inglés pixels per inch) y nos indica la cantidad de píxeles que caben en una pulgada. La pulgada es una medida inglesa que equivale a 2,54 cm, para que todos nos entendamos, serían los píxeles que caben en 6,45 cm². Este concepto es muy importante ya que determina la calidad y el tamaño que va a ocupar una imagen. La resolución normal que se utiliza en Internet es 72 ppi, esto nos indica que en 2,54 cm² hay 72 x 72 píxeles, osea 5.184. Si aumentamos la resolución tendremos más píxeles por pulgada y por lo tanto tendremos más información, más calidad y ocupará más nuestra imagen.


### Dimensiones de píxel
Las dimensiones de píxel nos da información del tamaño de la imagen. Este tamaño viene expresado en número de píxeles horizontales y número de píxeles verticales. Imaginaros que queremos escanear una imagen de 254 cm x 254 cm (equivale a 100 pulgadas x 100 pulgadas), a una resolución de 150 ppi. Queremos saber en términos de dimensiones de píxel cual va a ser su tamaño, lo único que tenemos que hacer es multiplicar el ancho y el alto de la imagen impresa por la resolución. Nos daría una imagen de 15.000 x 15.000 px.


### Profundidad de píxel
La profundidad de píxel o también llamada profundidad de color nos proporciona la cantidad de información de color que puede almacenar cada píxel en bits. Esto quiere decir que si tenemos una profundidad de píxel de 1, podremos almacenar 2 elevado a 1 valores posibles o sea 2 valores. Estas imágenes se llaman binarias y cada píxel puede ser blanco 0 o negro 1.  A continuación os muestro una tabla con la profundidad de color donde podemos ver diferentes tipos de archivos.

_______________________

#### Fuentes:
- https://programarfacil.com/podcast/44-tratamiento-de-imagenes-con-javascript/