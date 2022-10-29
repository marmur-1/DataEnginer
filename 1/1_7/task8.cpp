// Необходимо создать двумерный массив 5 х 5. 
// Далее написать функцию, которая заполнит его случайными 
// числами от 30 до 60. Создать еще две функции, которые 
// находят максимальный и минимальный элементы этого 
// двумерного массива.
#include <iostream>

using namespace std;

void fillMas(int mas[5][5]){
    for (int i = 0; i < 5; i++)
    {
        for (int l = 0; l < 5; l++)
        {
            mas[i][l] = 30 + rand() % 31;
            cout << mas[i][l] << "\t";
        }
        cout << endl;
    }
}
int minMas(int mas[5][5]){
    int res = INT_MAX;
    for (int i = 0; i < 5; i++)
    {
        for (int l = 0; l < 5; l++)
        {
            if(mas[i][l]<res) res=mas[i][l];
        }
    }
    return res;
}
int maxMas(int mas[5][5]){
    int res = INT_MIN;
    for (int i = 0; i < 5; i++)
    {
        for (int l = 0; l < 5; l++)
        {
            if(mas[i][l]>res) res=mas[i][l];
        }
    }
    return res;
}

int main()
{
    int mass[5][5];
    fillMas(mass);
    cout << "MIN = " << minMas(mass) << endl;
    cout << "MAX = " << maxMas(mass) << endl;
}

