// Написать программу, которая сравнивает два введённых с клавиатуры числа. 
// Программа должна указать, какое число больше или, если числа равны, вывести соответствующее сообщение.
#include <iostream>

using namespace std;

int main()
{
    int a = 15;
    int b = 20;

    cout << "A = ";
    cin >> a;
    cout << "B = ";
    cin >> b;

    if (a>b)
    {
        cout << a << " > " << b << endl;
    }else if (a<b)
    {
        cout << a << " < " << b << endl;
    }else
    {
        cout << a << " = " << b << endl;
    }
}