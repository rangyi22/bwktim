#graph_그림.py
import matplotlib.pyplot as plt
import matplotlib.image as img

fname = "D:/Won/Python/fig/Younggirl.png"
nda = img.imread(fname) # An NumPy.ndarray
plt.subplot(2,2,1)
plt.imshow(nda)  # 그림 8.24(a)
plt.colorbar()
# 그림의 크기, 최대치, data type을 알고 싶으면 
print(f'Size of nda = {nda.shape}')
print(f'Max of nda = {nda.max()}')
print(f'dtype of nda = {nda.dtype}')
plt.subplot(2,2,2)
nda1 = nda[0:200,100:200,0]
plt.imshow(nda1)  # 그림 8.24(b)
plt.show()
