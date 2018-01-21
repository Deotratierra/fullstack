## Aserciones

### En diseño por contrato
Las aserciones pueden ser una forma de documentación: la ventaja de usar sentencias de aserción en lugar de aserciones en comentarios es que las primeras pueden ser comprobadas en cada ejecución; si la aserción no se cumple, puede informarse del error. Esto previene que el código y las aserciones se desfasen (un problema que puede ocurrir con las aserciones comentadas).

### Aserciones durante el ciclo de desarrollo
Durante el ciclo de desarrollo, el programador normalmente ejecuta su programa con las aserciones activadas. Cuando una aserción resulta falsa y se produce el correspondiente error, el programador automáticamente recibe un aviso. Muchas implementaciones además detienen la ejecución del programa — esto resulta útil ya que si el programa sigue ejecutándose tras la violación de una aserción, éste entra en un estado corrupto que puede hacer más difícil la localización del problema. De este modo, las aserciones sirven como potente herramienta de depuración.
