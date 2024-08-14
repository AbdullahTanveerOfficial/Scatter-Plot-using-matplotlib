import numpy as np
from matplotlib import pyplot as plt
x=[20,30,45,43,15,87,56,79]
y1=[2,4,7,9,6,9,3,5]
y2=[1,3,5,7,3,9,8,2]
# plt.scatter(x,a)
# plt.show()
plt.title("Scatter plt")

plt.subplot(1,2,1)
plt.scatter(x,y1,marker='*',c='r',s=100)
plt.subplot(1,2,2)
plt.scatter(x,y2,marker='.',c='g',s=100)
plt.show()