// Написать программу, которая проверяет является ли год високосным.
#include <iostream>

using namespace std;

int main()
{
    int year = 2000;

    cout << "Введите год: ";
    cin >> year;

    if (year%4 == 0)
    {
        cout << "Високостный год" << endl;
    }else
    {
        cout << "Не високостный год" << endl;
    }
}