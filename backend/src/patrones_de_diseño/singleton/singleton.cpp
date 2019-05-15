#include <iostream>

class Singleton
{
    private:
        /* Aquí será almacenada la instancia. */
        static Singleton* instance;

        /**
         * Constructor privado para prevenir la instanciación.
         *   (significa que ``new Singleton();`` no funcionará).
         */
        Singleton();

    public:
        /* Método estático de acceso a la instancia. */
        static Singleton* getInstance();
};

/* Será inicializada a demanda. */
Singleton* Singleton::instance = 0;

Singleton* Singleton::getInstance()
{
    if (instance == 0)
    {
        instance = new Singleton();
    }

    return instance;
}

Singleton::Singleton()
{}

int main()
{
    //new Singleton(); // No funciona
    Singleton* s = Singleton::getInstance(); // Ok
    Singleton* r = Singleton::getInstance();

    // Comparamos las dos direcciones de memoria
    bool comp = s==r;

    /* Las direcciones deberían ser las mismas. */
    std::cout << s << std::endl;
    std::cout << r << std::endl;
    std::cout << comp << std::endl; // 1
}

/**
 * Fuentes:
 *   - https://gist.github.com/pazdera/1098119
 **/