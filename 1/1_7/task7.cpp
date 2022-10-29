// Написать программу, которая выводит таблицу значений функции 
// y=-2 * x^2 - 5 * x - 8 
// в диапазоне от –4 до +4, с шагом 0,5

#include <iostream>

using namespace std;

int main()
{
    float x = -4;
    float y = 0;
    while (x<=4)
    {
        y = (-2*(x*x)) - (5*x) - 8;
        cout << "X=" << x << "\tY="<< y << endl;
        x = x + 0.5;
    }
    
}