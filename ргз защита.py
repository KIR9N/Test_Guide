import numpy as np
import matplotlib.pyplot as plt
import math
import random as r
a= r.randint(0, 10)
marks=list(map(int,open('txtkirill.txt','r').read().split('\n'))) 
sum_marks = [0,0,0,0,0,a] 
for i in range(5):
    for x in marks:
        if x == i+1:
            sum_marks[i] += 1
if sum_marks[0]+sum_marks[2]+sum_marks [1]+sum_marks[3]>4:
  print('Программа не работает')
else:
  print('Программа работает')
print(sum_marks)
fig, axis = plt.subplots(1, 2)
axis[0].bar([1,2,3,4,5,6],sum_marks,width= 0.4)
axis[1].bar([1,2,3,5,4,6],sum_marks,width= 0.4,tick_label=[1,2,3,4,5,6])
plt.show()
