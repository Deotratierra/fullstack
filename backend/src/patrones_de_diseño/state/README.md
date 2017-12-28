### Patron Estado (State)
Se utiliza cuando queremos implementar diferentes comportamiento para un objeto según su estado. Básicamente creamos una clase para cada estado que deriven de una clase `Estado`.

El patrón no indica dónde definir las transiciones de un estado a otro. Existenn dos formas de solucionar esto:
- Definiendo las transiciones dentro de la clase `Contexto` (útil cuando el criterio a aplicar es fijo).
- Definiendo las transiciones en las subclases de estados (útil cuando el criterio de transición es dinámico). El incoveniente de esta opción e la dependencia de código entre las subclases.

>Fuentes:
- https://es.wikipedia.org/wiki/State_(patr%C3%B3n_de_dise%C3%B1o)
- https://sourcemaking.com/design_patterns/state/python/1