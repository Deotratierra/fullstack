## Explicación del patrón visitor



Imagina que tienes una clase primaria que es fija, quizas es de un proveedor y no puedes realizar cambios a su jerarquía. Sin embargo, tu intención es que tu quieres añadir nuevos métodos polimórficos a esa jerarquía, lo cual significa que normalmente tienes que añadir algo a la interfaz de la clase base. Así que el dilema está en que necesitas añadir métodos a la clase base, pero no puedes tocarla.

El patrón de diseño que soluciona este tipo de problemas es llamado un "visitor" (visitante en español). Este permite extender la interfaz del primer tipo creando una jerarquía separada de tipo Visitor para virtualizar las operaciones realizadas sobre el tipo primario. El objeto primario simplemente acepta al visitor, entonces llama a la función miembro dinámicamente enlazada.

El patrón visitor te permite implementar diferentes algoritmos sin modificar los objetos en los cuales opera y soporta diferentes acciones por cada tipo de objeto. Es implementado usando [multiple dispatching](https://github.com/mondeja/fullstack/tree/master/backend/src/patrones_de_dise%C3%B1o/multiple_dispatch), ya que cuando un visitor visita otro elemento se realizan dos llamadas a funciones, una para aceptar y otra para visitar, y la función ``visitar`` que es llamada depende del tipo de los dos objetos.

> Fuentes:
- http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Visitor.html
- https://cpppatterns.com/patterns/visitor.html