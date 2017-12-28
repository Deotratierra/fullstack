// ==  Opción 1 (funciona en todos los compiladores):  ==
#ifdef __linux__
#include <unistd.h>
#define sleep(ms) { usleep(ms*1000); }
#endif
#ifdef __WINDOWS__
#include <windows.h>
#define sleep(ms) { Sleep(ms); }
#endif

// ======================================================

// ======= Opción 2 (funciona a partir de C++11): =======

#include <chrono>
#include <thread>

void sleep2(int ms) {
    std::this_thread::sleep_for(std::chrono::milliseconds(ms));
}

// ======================================================

int main() {
    // Ambos valores en milisegundos
    sleep(1000);
    sleep2(1000);

    return 0;
}
