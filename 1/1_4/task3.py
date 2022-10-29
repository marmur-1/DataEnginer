# Найти зависимости представленные в датасете приложенном к заданию.

import numpy as np
import matplotlib.pyplot as plt

age = [] #возвраст
sex = [] #пол
bmi = [] #индекс массы
children = [] #дети
smoker = [] #курит ли
region = [] #регион
charhes = [] #трата на страховку

with open('./dataset_home.txt', mode="r") as file:
    for human in file.readlines():
        h = human.split(',')
        age.append(int(h[0]))
        if h[1] == 'male':
            sex.append(1)
        else:
            sex.append(0)
        bmi.append(float(h[2]))
        children.append(int(h[3]))
        if h[4]=='yes':
            smoker.append(1)
        else:
            smoker.append(0)
        if h[5]=='northwest':
            region.append(0)
        elif h[5]=='northeast':
            region.append(1)
        elif h[5]=='southwest':
            region.append(2)
        elif h[5]=='southeast':
            region.append(3)
        else:
            region.append(4)
        charhes.append(float(h[6]))

age = np.array(age)
sex = np.array(sex)
bmi = np.array(bmi)
children = np.array(children)
smoker = np.array(smoker)
region = np.array(region)
charhes = np.array(charhes)

fig, ax = plt.subplots(5, 6)
ax[0][0].scatter(charhes,age,label="age")
ax[0][1].scatter(charhes,sex,label="sex")
ax[0][2].scatter(charhes,bmi,label="bmi")
ax[0][3].scatter(charhes,children,label="children")
ax[0][4].scatter(charhes,smoker,label="smoker")
ax[0][5].scatter(charhes,region,label="region")
# ax[0][6].scatter(charhes,charhes,label="charhes")

ax[1][0].bar(age,charhes,label="age")
ax[1][1].bar(sex,charhes,label="sex")
ax[1][2].bar(bmi,charhes,label="bmi")
ax[1][3].bar(children,charhes,label="children")
ax[1][4].bar(smoker,charhes,label="smoker")
ax[1][5].bar(region,charhes,label="region")
# ax[1][6].bar(charhes,charhes,label="charhes")

ax[2][0].hist(age,label="age")
ax[2][1].hist(sex,label="sex")
ax[2][2].hist(bmi,label="bmi")
ax[2][3].hist(children,label="children")
ax[2][4].hist(smoker,label="smoker")
ax[2][5].hist(region,label="region")
# ax[2][6].hist(charhes,label="charhes")

ax[3][0].scatter(charhes[age<36],bmi[age<36],  label="age<36")
ax[3][0].scatter(charhes[age>35][age[age>35]<56],bmi[age>35][age[age>35]<56],  label="35<age<56")
ax[3][0].scatter(charhes[age>55],bmi[age>55],  label="age>55")

ax[3][1].scatter(charhes[bmi<21],bmi[bmi<21],  label="bmi<21")
ax[3][1].scatter(charhes[bmi>20][bmi[bmi>20]<41],bmi[bmi>20][bmi[bmi>20]<41],  label="20<age<41")
ax[3][1].scatter(charhes[bmi>40],bmi[bmi>40],  label="bmi>40")

ax[3][2].hist([charhes[smoker==0],charhes[smoker==1]],label="charhes/smoker")

for ar in ax:
    for a in ar:
        a.legend(loc='best', frameon=False)

plt.show()