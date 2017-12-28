## Explicación del patrón visitor

El patrón visitor es implementado usando [multiple dispatching](https://github.com/mondeja/fullstack/tree/master/backend/src/patrones_de_dise%C3%B1o/multiple_dispatch), pero la gente a menudo los confunden debido a que se fijan más en la implementación que en su intención.

Imagina que tienes una clase primaria que es fija, quizas es de un proveedor y no puedes realizar cambios a su jerarquía. Sin embargo, tu intención es que tu quieres añadir nuevos métodos polimórficos a esa jerarquía, lo cual significa que normalmente tienes que añadir algo a la interfaz de la clase base. Así que el dilema está en que necesitas añadir métodos a la clase base, pero no puedes tocarla.

El patrón de sieño que soluciona este tipo de problemas es llamado un "visitor" (visitante en español). Este permite extender la interfaz del primer tipo creando una jerarquía separada de tipo Visitor para virtualizar las operaciones realizadas sobre el tipo primario. El objeto primario simplemente acepta al visitor, entonces llama a la función miembro dinámicamente enlazada.

>Fuente:
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Visitor.html