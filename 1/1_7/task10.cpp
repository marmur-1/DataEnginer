// Создайте структуру с именем train, содержащую поля: 
// название пункта назначения, номер поезда, время отправления. 
// Ввести данные в массив из пяти элементов типа train, 
// упорядочить элементы по номерам поездов. 
// Добавить возможность вывода информации о поезде, номер которого введен пользователем. 
// Добавить возможность сортировки массив по пункту назначения, 
// причем поезда с одинаковыми пунктами назначения должны быть упорядочены по времени отправления.
#include <iostream>
#include <ctime>

using namespace std;

class train{
public:
    string punct;
    int numb;
    time_t start;
    train(string Punct,int Numb,time_t Start){
        punct = Punct;
        numb = Numb;
        start = Start;
    }

    void show(){
        cout << numb << " \t"<< punct << " \t" << ctime(&start);
    }
};

void bubbleSort(train list[], int listLength)
{
	while(listLength--)
	{
		bool swapped = false;
		
		for(int i = 0; i < listLength; i++)
		{
			if(list[i].numb > list[i + 1].numb)
			{
				swap(list[i], list[i + 1]);
				swapped = true;
			}
		}
		
		if(swapped == false)
			break;
	}
}
void showList(train list[], int listLength){
    for (int l = 0; l < listLength; l++)
    {
        list[l].show();
    }
}
void showByNum(train list[], int listLength, int Num){
    for (int l = 0; l < listLength; l++)
    {
        if(list[l].numb == Num){
            list[l].show();
        }
    }
}
void sortByPunct(train list[], int listLength){
	while(listLength--)
	{
		bool swapped = false;
		
		for(int i = 0; i < listLength; i++)
		{
			if(list[i].punct > list[i + 1].punct)
			{
				swap(list[i], list[i + 1]);
				swapped = true;
			}else if(list[i].punct == list[i + 1].punct){
                if (list[i].start > list[i + 1].start)
                {
                    swap(list[i], list[i + 1]);
                    swapped = true;
                }
            }
		}
		
		if(swapped == false)
			break;
	}
}

int main(){
    train trains[5] = {
        train("ЛЮБЕРЦЫ",5,(time_t)((unsigned int)time(0)+(unsigned int)(500-rand()%1000))),
        train("О.ПАСХИ",1,(time_t)((unsigned int)time(0)+(unsigned int)(500-rand()%1000))),
        train("СТ.НОВАЯ",3,(time_t)((unsigned int)time(0)+(unsigned int)(500-rand()%1000))),
        train("РОДНОЙ ДОМ",2,(time_t)((unsigned int)time(0)+(unsigned int)(500-rand()%1000))),
        train("СТ.НОВАЯ",4,(time_t)((unsigned int)time(0)+(unsigned int)(500-rand()%1000)))
    };

    showList(trains,5);
    cout << endl;

    bubbleSort(trains,5);

    showList(trains,5);
    cout << endl;

    int num = 0;
    cout << "Введите номер поезда: "; cin >> num;
    showByNum(trains,5,num);
    cout << endl;

    sortByPunct(trains,5);
    showList(trains,5);
}