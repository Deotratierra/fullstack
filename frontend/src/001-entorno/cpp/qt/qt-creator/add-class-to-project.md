## Añadir clase a un proyecto en Qt Creator

1. Vamos a ``File`` > ``New File or Project`` > ``C++`` > ``C++ Class``.
2. En los campos indicamos, para este ejemplo, los siguientes valores:
    - **Class name**: ``Window``
    - **Base class**: ``QWidget``
    - **Header file**: ``window.h``
    - **Source file**: ``window.cpp``
    - **Path**: ``/ruta/al/directorio/de/tu/proyecto``

Te aparecerá el archivo ``window.h`` en la carpeta ``Headers`` y el ``window.cpp`` en la carpeta ``Sources``. 

### Plantilla de clase

Si abres el archivo ``window.h`` podrás ver que Qt Creator crea automáticamente una plantilla de clase. Nota que hay nuevos elementos en el header:

- La macro ``Q_OBJECT``.
- Dos nuevas categorías de métodos: señales (**``signals``**) y slots púbicos (**``public slots``**).

#### ``window.h``

```cpp
#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>

class WIndow : public QWidget
{
    Q_OBJECT
public:
    explicit WIndow(QWidget *parent = nullptr);

signals:

public slots:
};

#endif // WINDOW_H
```