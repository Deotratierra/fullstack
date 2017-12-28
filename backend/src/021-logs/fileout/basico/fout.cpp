// Biblioteca spdlog:
// https://github.com/gabime/spdlog
#include <spdlog/spdlog.h>

using namespace std;
namespace spd = spdlog;

int main() {

    // Logger de salida a archivo:
    auto logger = spd::basic_logger_mt("nombre_del_logger", "archivo.log");
    logger -> info("¡Bienvenido al logging en arhivos con spdlog!");
    logger -> error("Es muy fácil de utilizar");

	return 0;
}
