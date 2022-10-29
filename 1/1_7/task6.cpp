// Написать программу, которая определяет максимальное число 
// из введённой с клавиатуры последовательности положительных чисел. 
// (длина последовательности неограниченна)

#include <iostream>


using namespace std;

int main()
{
    bool end = true;
    int a,res = INT_MIN;
    do
    {
        a = INT_MIN;
        cout << "Ввежите число или иное чтобы выйти: ";
        cin >> a;
        if(a>res) res = a;
      
    } while (INT_MIN!=a);

    cout << "\n\nНаибольшее число это " << res;
}