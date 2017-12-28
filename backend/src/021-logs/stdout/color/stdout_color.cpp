#include <spdlog/spdlog.h>

using namespace std;
namespace spd = spdlog;

int main() {

    // Logger de salida estandar coloreada:
    auto console = spd::stdout_color_mt("nombre_del_logger");
    console -> info("¡Bienvenido al logger de salida estándar coloreada de spdlog!");
    console -> error("Mensaje de error (en rojo)");
    console -> warn("Mensaje de advertencia (en amarillo)");
    console -> critical("Error crítico (en blanco con fondo rojo)")

    return 0;
}