## Ejemplo de herencia de clases en Qt

En el siguiente ejemplo, creamos un widget heredando de la clase ``QWidget`` y le añadimos un simple botón con el texto ``"¡Hola mundo!"``.

### ``main.cpp``

```cpp
#include <QApplication>
#include "window.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    Window window;
    window.show();

    return app.exec();
}
```

### ``window.h``

```cpp
#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>

class QPushButton;
class Window : public QWidget
{
public:
    explicit Window(QWidget *parent = 0);
private:
    QPushButton *m_button;
};

#endif // WINDOW_H

```

### ``window.cpp``

```cpp
#include "window.h"
#include <QPushButton>

Window::Window(QWidget *parent) :
 QWidget(parent)
 {
 // Establece el tamaño del widger
 setFixedSize(100, 50);

 // Creamos el botón y lo posicioamos
 m_button = new QPushButton("¡Hola mundo!", this);
 m_button->setGeometry(10, 10, 80, 30);
}

```