#%%
import numpy as np
import matplotlib.pyplot as plt
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t+1, 'r--', t, t**2, 'bs', t, t**2.5, 'g^')
plt.show()

#%%