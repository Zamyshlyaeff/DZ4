#  В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени 
# сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с 
# этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном файле грядки.
import random
N=[random.randint(1,10) for i in range(6)]
print(N)

max=0
LFR=0
for i in range(1,len(N)):
    if i==len(N)-1:
        LFR=(N[i-1])+(N[i])+(N[0])
        if LFR>max:
            max==LFR
    elif (N[i-1])+(N[i])+(N[i+1])>max:
        max=(N[i-1])+(N[i])+(N[i+1])
print(max)

