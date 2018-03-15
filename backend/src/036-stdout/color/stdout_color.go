package main

import (
    "fmt"
    "github.com/fatih/color"
)

func main() {  // Añade una nueva línea automáticamente
    color.Cyan("Imprime texto en %s", "celeste")
    color.Blue("Imprime texto en azul")
    color.Red("Rojo")
    color.Green("Verde")

    // Crea un nuevo objeto de color
    c := color.New(color.FgCyan).Add(color.Underline)
    c.Println("Imprime celeste con subrayado")
    //      Mezclando estilos
    d := color.New(color.FgCyan, color.Bold)
    d.Printf("Esto imprime celeste en %s\n", "negrita")

    // Con colores de fondo
    blue := color.New(color.FgBlue)
    blue.Add(color.Bold)
    whiteBg := blue.Add(color.BgWhite)
    whiteBg.Println("Texto azul con fondo blanco.")

    // Create a custom print function for convenience
    yellow := color.New(color.BgYellow).PrintfFunc()
	red := color.New(color.FgRed).PrintfFunc()
	yellow("¡Atención!\n")
	red("Error: %s\n", "Bomba en el disco duro.")

	// Mezclar cadenas coloreadas con otras sin colorear
	// SprintFunc()
    _yellow := color.New(color.FgYellow).SprintFunc()
    _red := color.New(color.FgRed).SprintFunc()
    fmt.Printf("Esto es una %s y esto es un %s.\n",
    	       _yellow("advertencia"), _red("error"))


    // Fuente:
    // https://github.com/fatih/color
}
