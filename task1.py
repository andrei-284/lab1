import numpy as np
import matplotlib.pyplot as plt
import os
x=np.linspace(0,1,1000)
y=np.power((6*x-2),2)*np.sin(12*x-4)
plt.figure()
plt.plot(x,y,'k-',lw=3)
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'$y(x)=(6x-2)^2 \cdot sin(12x-4)$')
plt.show()
path=os.getcwd()
new_path=path+'/results'
try:
    os.mkdir(newpath)
except:
    pass
os.chdir(new_path)
os.getcwd()
data=zip(x,y)
with open("task_01_307b_Maximkin_17.txt", "w") as txt_file:
    for line in data:
        txt_file.write("{:6.4f}    {:6.4f} \n".format(line[0],line[1]))
txt_file.close()
