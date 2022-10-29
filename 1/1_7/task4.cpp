// Проверить на чётность введённое с клавиатуры число
#include <iostream>


using namespace std;

int main()
{
    int a = 0;

    cout << "Число: ";
    cin >> a;

    if (a%2 == 0)
    {
        cout << "Чётное" << endl;
    }else
    {
        cout << "Нечётное" << endl;
    }
}