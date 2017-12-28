// Biblioteca spdlog:
// https://github.com/gabime/spdlog
#include <spdlog/spdlog.h>
/* Instalación en Linux:
git clone https://github.com/gabime/spdlog.git && \
    cd spdlog/include && \
    sudo cp -r spdlog /usr/include/spdlog
*/

// Compilar con sudo y -pthread

using namespace std;
namespace spd = spdlog;

int main() {

    // Logger de salida estandar coloreado:
    auto console = spd::stdout_color_mt("nombre_del_logger");
    console -> info("Bienvenido a spdlog!");
    console -> error("Mensaje de error con argumento {}", 1);  // (Rojo)

    // Ejemplos de formateo
    console -> warn("Padding en los números así {:08d}", 34); // 00000034  (Amarillo)
    console -> critical("Enteros: {0:d}; Hex: {0:x}; Octal: {0:o}; Binario: {0:b}", 13); // (Blanco, fondo rojo)
    console -> info("Decimales: {:03.2f}", 3.1416);  // 3.14
    console -> info("Args {1} {0}", "desordenados", "posicionales");  // Args posicionales desordenados
    console -> info("{:>30}", "Alineado a la derecha");  //        Alineado a la derecha

	return 0;
}
