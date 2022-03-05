import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])

def estimate_coef(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    x_deviation = x - mean_x
    y_deviation = y - mean_y
    
    x_deviation2 = x_deviation**2
    
    m = (np.sum(x_deviation * y_deviation))/np.sum(x_deviation2)
    c = mean_y - (m * mean_x)
    
    return m,c
	
b = estimate_coef(x,y)
print(f"Estimated coefs:\nb_0 = {b[0]}\nb_1 = {b[1]}")

x_var = float(input("Enter value of x: "))
y_var = (b[0]*x_var)+b[1]
print("Output Y is: ",y_var)

x=np.append(x, x_var, axis=None)
y=np.append(y, y_var, axis=None)

plt.scatter(x,y,color="m", marker="o", s=30)

y_pred = (b[1]*x) + b[0]

plt.plot(x,y_pred, color="g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
