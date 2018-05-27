## AWS Amazon

### API de AWS
- [Boto3](https://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html) (py)

### Llaves de seguridad
Al lanzar instancias de Amazon mediante la interfaz gráfica, obtendremos un para de llaves valor para conectarnos a la instancia que hemos creado mediante SSH. Estos pares de llaves pueden compartirse entre varias instancias.

> En Linux es recomendable guardar los pares de llaves criptográficas dentro del directorio `~/.ssh/`.

Al descargar las llaves, debemos denegar los permisos de acceso a usuarios sin privilegios, por lo que ejecutamos `chmod 400 ~/.ssh/mykeypair.pem`.

- Conectarse a una instancia: `ssh -i ~/.ssh/mykeypair.pem ec2-user@{dirección_IP}`


