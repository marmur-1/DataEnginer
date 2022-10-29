// Написать программу, которая выводит таблицу квадратов десяти первых положительных чисел.
#include <iostream>


using namespace std;

int main()
{
    cout << "\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\v\n";
    for (int i = 1; i < 10; i++)
    {
        cout << i;
        for (int s = 0; s < 10; s++)
        {
           int c = stoi(to_string(i) + to_string(s));
           c = c*c;
           cout << "\t" << c;
        }
        cout << "\v\n";
    }
    
}