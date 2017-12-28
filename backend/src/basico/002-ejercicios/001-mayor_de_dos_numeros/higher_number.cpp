#include <iostream>
using namespace std;

int mayor(int a, int b);

int main(){
    int num1 = 3, num2 = 5;
    cout << mayor(num1, num2);    
    
    return 0;
}

int mayor(int a, int b){
    if (a >= b){ return a; }
    else { return b; }
}
    
    
    
