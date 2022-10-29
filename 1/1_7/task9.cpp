// Создайте структуру с именем student, содержащую поля: 
// фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов). 
// Создать массив из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла. 
// Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
#include <iostream>

using namespace std;

class student{
public:
    student(string FIO, int Num_group, int Grades[5]){
        fio = FIO;
        num_group = Num_group;
        for (int i = 0; i < 5; i++)
        {
            grades[i] = Grades[i];
        }
    }
    string fio;
    int num_group;
    int grades[5];
    
    void show(){
        cout << fio << " " << num_group << " [";
        for (int i = 0; i < 5; i++)
        {
            cout << grades[i];
            if(i!=4){cout << ",";}else{cout << "]";}
        }
        cout << endl;
    }
    float gradesMean(){
        int sum = 0;
        for (int i = 0; i < 5; i++)
        {
            sum = sum + grades[i];
        }
        return sum/5.0;
    }   
    bool grades45(){
        bool res = true;
        for (int i = 0; i < 5; i++)
        {
            if (grades[i]<4)
            {
               res = false;
               break;
            }        
        }
        return res;
    }
};

void bubbleSort(student list[], int listLength)
{
	while(listLength--)
	{
		bool swapped = false;
		
		for(int i = 0; i < listLength; i++)
		{
			if(list[i].gradesMean() > list[i + 1].gradesMean())
			{
				swap(list[i], list[i + 1]);
				swapped = true;
			}
		}
		
		if(swapped == false)
			break;
	}
}

void showList(student list[], int listLength){
    for (int l = 0; l < listLength; l++)
    {
        list[l].show();
    }
}

void show45Grades(student list[], int listLength){
    for (int l = 0; l < listLength; l++)
    {
        student s = list[l];
        if(s.grades45()){
            s.show();
        }
    }
}

int main()
{   
    int Grades[10][5]={
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {5,5,4,4,5},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4},
        {2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4,2+rand()%4}
    };

    student students[10] = {
        student("Чебурашкин",1,Grades[0]),
        student("Евреев",1,Grades[1]),
        student("Тумби",1,Grades[2]),
        student("Сарафанова",2,Grades[3]),
        student("Дарт Вейдер",2,Grades[4]),
        student("Майор Пейн",1,Grades[5]),
        student("Бил Гейтс",1,Grades[6]),
        student("Павел Дуров",2,Grades[7]),
        student("Линус Торвальдс",2,Grades[8]),
        student("Рамзан Кадыров",2,Grades[9])
    };

    showList(students,10);
    cout << endl;

    bubbleSort(students,10);

    showList(students,10);
    cout << endl;

    show45Grades(students,10);
}

