## Sistema de parentesco de elementos en Qt

El sistema de parentesco es una forma conveniente de tratar con objetos en Qt, especialmente widgets. Cualquier objeto que hereda de ``QObject`` puede tener un padre e hijos:

- Cuando un objeto es destruido, todos sus hijos también son destruidos.
- Todos los objetos ``QObject`` tienen métodos ``findChild`` y ``findChildren`` que pueden ser usados para buscar por hijos en un objeto dado.
- Los widgets hijos en un ``QWidget`` aparecen automáticamente dentro del widget padre.

________________________


El siguiente trozo de código crea un ``QPushButton`` dentro de otro:

```cpp
#include <QApplication>
#include <QPushButton>

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    QPushButton button1 ("test");
    QPushButton button2 ("other", &button1);

    button1.show();

    return app.exec();
}
```

_________________________


El siguiente trozo de código despliega un botón dentro de un widget:

```cpp
#include <QApplication>
#include <QPushButton>

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    QWidget window;
    window.setFixedSize(100, 50);

    QPushButton *button = new QPushButton("Hola mundo", &window);
    button->setGeometry(10, 10, 80, 30);

    window.show();
    return app.exec();
}

```