#%%
import scipy.signal as sig

img = [[1,2,3],
       [4,5,6],
       [7,8,0]]
kernel = [[0,1],
          [-1,2]]

result = sig.convolve2d(kernel,img)

print(result)
#%%