package main

import (
    "os"
    "path"
)

//            Trabajando con rutas en Go

func main() {
    // =================================
    //             os
    // https://golang.org/pkg/os/

    // Obtener el directorio actual
    pwd, _ := os.Getwd()

    // Cambiar de directorio de trabajo
    os.Chdir("../")

    // Crear directorio
    os.Mkdir("directorio", os.ModePerm)

    // Eliminar archivo o directorio
    os.Remove("directorio")

    // Renombrar/mover un archivo
    os.Rename("ejemplo", "ejemplo")

    // =====================================
    //            path
    // https://golang.org/pkg/path/

    // Separar el nombre del archivo de la ruta
    //   al directorio donde se encuentra
    dir, file := path.Split(pwd)
    println(dir, file)

    // Obtener la base de la ruta
    base := path.Base(pwd)
    println(base)

    // Obtener el directorio
    _dir := path.Dir(pwd)
    println(_dir)

    // Obtener la extensión de un archivo
    ext := path.Ext(pwd)
    println(ext)

    // Unir paths añadiendo "/" ó "\" entre ellos
    path_joined := path.Join(dir, file)
    println(path_joined)

    // Saber si un path es absoluto
    isabs = path.IsAbs(pwd)

    // =====================================
}
