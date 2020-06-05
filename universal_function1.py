import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,3*np.pi,num=100)
y=np.sin(x)
plt.xlabel("Domain of sin(x)", color="red")
plt.ylabel("Range of sin(x)",color="red")
plt.title("Sin Graph", color="green")
plt.plot(x,y)
plt.show()
