## Tags en git
Git usa dos tipos principales de tags: los ligeros y los anotados.
- Un tag **ligero** es como una rama que no cambia, es simplemente un puntero a un commit específico.
- Un tag **anotado**, sin embargo, es guardado como un objeto en la base de datos de git. Es verificado, contiene el nombre del creador, el email y la fecha, tienen un mensaje asociado... Generalmente se recomienda crear tags anotados así puedes tener disponible este tipo de información.

Los tags no se comparten automáticamente al hacer commit, debe hacerse explícitamente mediante el comando `git push origin <nombre_del_tag>`.


