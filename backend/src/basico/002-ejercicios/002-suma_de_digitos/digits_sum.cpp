# include <iostream>
# include <sstream>
using namespace std;

// Definimos la siguiente macro para convertir números a cadenas:
// https://stackoverflow.com/questions/5590381/easiest-way-to-convert-int-to-string-in-c
#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()


string digits_sum(int number){
    int total = 0;
    int rest;
    string response = "";

    while (number != 0) {
        rest = number % 10;
        response += SSTR(rest);

        total += rest;
        number /= 10;
        if (number > 0) { response += " + ";}
    }
    response += " = " + SSTR(total);
    return response;
}

int main(){
    int num1 = 4511, num2 = 369301;

    cout << digits_sum(num1) << endl;
    cout << digits_sum(num2) << endl;
}
