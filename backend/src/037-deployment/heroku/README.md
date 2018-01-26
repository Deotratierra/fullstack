### Desplegar aplicación en Heroku (Debian/Ubuntu)

- Instalar el cliente de Heroku: `wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh`
- Crear aplicación en Heroku: `heroku create <nombre_de_aplicación>`
- Crear comando de inicialización: `echo "<comando_iniciar_aplicación>" > Procfile`
- [Configurar entorno de ejecución](https://devcenter.heroku.com/articles/python-runtimes): `echo "<entorno>" > runtime.txt`
- Enlazar con git: `git remote add <branch> git@heroku.com:<nombre_de_aplicacion>.git`
- Desplegar: `git push <branch> master`
- Configurar variables de entorno en Heroku (también configurables desde la interfaz gráfica de Heroku): `heroku config:set <VARIABLE>=<valor> --remote <branch>`
- Instalar [addons](https://elements.heroku.com/addons) (también configurables desde la interfaz gráfica de Heroku): `heroku addons:create <addon>`

>Fuentes:
> - https://devcenter.heroku.com/articles/heroku-cli
> - https://realpython.com/blog/python/flask-by-example-part-1-project-setup
> - https://devcenter.heroku.com/articles/python-runtimes