// Написать программу решения квадратного уравнения. 
// Программа должна проверять правильность исходных данных и в случае, 
// если коэффициент при второй степени неизвестного равен нулю, 
// выводить соответствующее сообщение.
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a,b,c = 0;

    cout << "A = ";
    cin >> a;
    cout << "B = ";
    cin >> b;
    cout << "C = ";
    cin >> c;
    cout << a << "x²+" << b << "x+" << c << "=0" << endl;

    if(a==0){
        cout << "Неимеет решения (A = 0)" << endl;
    }else{
        int D =(b*b)-(4*a*c);
        // cout << "Дискриминант:"  << D << endl;
        if(D>0){
            int x1 = (-b+(sqrt(D)))/(2*a);
            int x2 = (-b-(sqrt(D)))/(2*a);
            cout << "x1 = " << x1 << endl;
            cout << "x2 = " << x2 << endl;
        }else if(D == 0){
            int x = (-b)/(2*a);
            cout << "x = " << x << endl;
        }else{
            cout << "Нет корней (D < 0)" << endl;
        }

    }
}