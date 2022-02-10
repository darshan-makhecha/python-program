import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.3, 0.6, 0.9]
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
