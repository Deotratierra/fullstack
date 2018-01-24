#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;

string GetEnv( const string & var );

int main(){
    string API_KEY;

    API_KEY = GetEnv("API_KEY");
    cout << API_KEY << endl;

    return 0;

}

// Realmente esta función no es necesaria, pero es más efectiva
// que usar directamente ::getenv (ver la fuente)
string GetEnv( const string & var ) {
     const char * val = ::getenv( var.c_str() );
     if ( val == 0 ) {
         return "";
     }
     else {
         return val;
     }
}

/* Fuente:
https://stackoverflow.com/questions/5866134/how-to-read-linux-environment-variables-in-c
*/
