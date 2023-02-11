import matplotlib.pyplot as plt
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
plt.style.use('seaborn')
ax.scatter(x_values,y_values, c='orange')
ax.set_title("Square Numbers", fontsize=30)
ax.set_ylabel("Square of Value", fontsize=16)
ax.set_xlabel("Value", fontsize=16)

ax.tick_params(axis='both')
plt.show()

