#include <QApplication>
#include <QPushButton>

/** 
 * Ejemplo de aplicación básica en Qt, con un botón dentro
 *   de una ventana.
 **/

int main(int argc, char **argv)
{
	// Objeto encargado de manejar lo relativo a la aplicación,
	//   como los parámetros de entrada o el loop de eventos
	//   https://doc.qt.io/qt-5/qapplication.html
    QApplication app (argc, argv);


    QPushButton button ("¡Hola mundo!");
    button.show();

    // Con la función ``exec`` se lanza el loop de eventos
    return app.exec();
}
