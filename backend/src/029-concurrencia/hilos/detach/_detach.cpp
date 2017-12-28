#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

void dormir(int segundos) {
    this_thread::sleep_for(chrono::seconds(segundos));
}

void contador_interminable() {
    ulong i = 1;
    while (true) {
        cout << i << "\n";
        i += 1;
        dormir(1);
    }
}

int main() {
    thread t1(contador_interminable);
    // Continuar la ejecución en background:
    t1.detach();

    return 0;
}